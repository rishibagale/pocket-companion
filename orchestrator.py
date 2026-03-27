import json
import os
import re
from enum import Enum, auto
from stt import STT
from llm import LLM
from tts import TTS

class State(Enum):
    LISTENING = auto()
    THINKING = auto()
    SPEAKING = auto()
    PAUSED = auto()

class Orchestrator:
    def __init__(self, stt: STT, llm: LLM, tts: TTS, config: dict):
        self.stt = stt
        self.llm = llm
        self.tts = tts
        self.config = config
        self._state = None
        self.state = State.LISTENING
        self.messages = []
        self.memory_file = "memory.json"
        
        self._load_memory()

    @property
    def state(self):
        return self._state
        
    @state.setter
    def state(self, new_state):
        if self._state == new_state:
            return
        self._state = new_state
        print(f"[{new_state.name}]")

    def _load_memory(self):
        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, 'r', encoding='utf-8') as f:
                    self.messages = json.load(f)
            except Exception:
                self.messages = []
        else:
            self.messages = []

    def _save_memory(self):
        with open(self.memory_file, 'w', encoding='utf-8') as f:
            json.dump(self.messages, f, indent=2)

    def _trim_memory(self):
        max_turns = self.config.get("memory_turns", 20)
        max_messages = max_turns * 2
        if len(self.messages) > max_messages:
            self.messages = self.messages[-max_messages:]

    def clear_memory(self):
        self.messages = []
        if os.path.exists(self.memory_file):
            try:
                os.remove(self.memory_file)
            except Exception:
                pass

    def set_voice(self, voice: str):
        self.config["voice"] = voice

    def pause(self):
        self.state = State.PAUSED

    def resume(self):
        self.state = State.LISTENING

    def run_turn(self, user_input: str):
        text_lower = user_input.lower().strip()
        text_punct_stripped = re.sub(r'[^\w\s]', '', text_lower)
        
        if text_punct_stripped == "stop listening":
            self.pause()
            return
            
        if text_punct_stripped in ["start listening", "resume"]:
            self.resume()
            return
            
        if text_punct_stripped == "clear memory":
            self.clear_memory()
            self.state = State.SPEAKING
            self.tts.speak("Memory cleared.")
            self.state = State.LISTENING
            return
            
        if text_punct_stripped.startswith("change voice to "):
            new_voice = text_punct_stripped.replace("change voice to ", "").strip().title()
            self.set_voice(new_voice)
            self.state = State.SPEAKING
            self.tts.speak(f"Voice changed to {new_voice}.", voice=new_voice)
            self.state = State.LISTENING
            return

        if text_punct_stripped == "what model are you using":
            model_name = self.config.get("model", "unknown")
            self.state = State.SPEAKING
            self.tts.speak(f"I am using the {model_name} model.")
            self.state = State.LISTENING
            return

        self.messages.append({"role": "user", "content": user_input})
        self._trim_memory()
        self._save_memory()

        system_msg = [{"role": "system", "content": self.config.get("system_prompt", "You are a helpful assistant.")}]
        full_messages = system_msg + self.messages
        
        self.state = State.THINKING
        
        buffer = ""
        full_response = ""
        
        try:
            for chunk in self.llm.stream(full_messages):
                buffer += chunk
                full_response += chunk
                
                splits = re.split(r'([.!?\n]+)', buffer)
                if len(splits) > 1:
                    complete_text = "".join(splits[:-1])
                    remainder = splits[-1]
                    
                    clean_sentence = complete_text.strip()
                    if clean_sentence:
                        self.state = State.SPEAKING
                        self.tts.speak(clean_sentence)
                    buffer = remainder
            
            if buffer.strip():
                self.state = State.SPEAKING
                self.tts.speak(buffer.strip())
                
        except Exception as e:
            print(f"Error during LLM stream: {e}")
            self.state = State.SPEAKING
            self.tts.speak("Sorry, I encountered an error checking my brain.")

        self.messages.append({"role": "assistant", "content": full_response})
        self._trim_memory()
        self._save_memory()
        
        self.state = State.LISTENING
