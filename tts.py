import numpy as np
import sounddevice as sd

class TTS:
    def __init__(self, config: dict):
        self.config = config
        self.speaking = False
        try:
            from kittentts import KittenTTS
            self.model = KittenTTS(model_name="KittenML/kitten-tts-mini-0.8")
        except ImportError:
            raise ImportError("Error: KittenTTS not installed. Please run: pip install https://github.com/KittenML/KittenTTS/releases/download/0.8.1/kittentts-0.8.1-py3-none-any.whl")

    def speak(self, text: str, voice: str = None):
        self.speaking = True
        try:
            # Use provided voice or fallback to config default
            target_voice = voice if voice else self.config.get("voice", "Luna")
            
            # Generate audio points (assuming it returns numpy array)
            audio = self.model.generate(text, voice=target_voice)
            
            # KittenTTS mini has a 24000 Hz sample rate
            sd.play(audio, samplerate=24000)
            sd.wait()
        finally:
            self.speaking = False
