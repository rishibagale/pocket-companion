import sys
import os
import json
import time

from stt import STT
from llm import LLM
from tts import TTS
from orchestrator import Orchestrator, State

def load_config():
    if not os.path.exists("config.json"):
        sys.exit("Error: config.json not found. Copy config.example.json to config.json and edit it.")
    with open("config.json", "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    config = load_config()
    
    try:
        if not LLM(config).check_connection():
            print("Warning: Ollama connection could not be established immediately, proceeding anyway.")
    except Exception:
        pass

    llm = LLM(config)
    if not llm.check_connection():
         sys.exit("Error: Ollama is not running. Start it with: ollama serve")

    try:
        tts = TTS(config)
    except Exception as e:
        sys.exit(f"{e}")
        
    stt = STT(config)
    
    orchestrator = Orchestrator(stt=stt, llm=llm, tts=tts, config=config)

    print("\nAI Companion initialized. You can start speaking.")
    
    try:
        while True:
            if orchestrator.state == State.PAUSED:
                time.sleep(0.1)
                continue

            if orchestrator.state == State.SPEAKING:
                time.sleep(0.05)
                continue

            text = stt.listen()

            if not text or len(text.strip()) < 3:
                continue

            print(f"You: {text}")
            orchestrator.run_turn(text)
            
    except KeyboardInterrupt:
        print("\nGoodbye.")
        orchestrator._save_memory()
        sys.exit(0)

if __name__ == "__main__":
    main()
