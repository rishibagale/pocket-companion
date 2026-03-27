import numpy as np
import sounddevice as sd
from faster_whisper import WhisperModel

class STT:
    def __init__(self, config: dict):
        self.config = config
        self.sample_rate = self.config.get("sample_rate", 16000)
        self.silence_threshold = self.config.get("silence_threshold", 0.01)
        self.silence_seconds = self.config.get("silence_seconds", 1.2)
        model_size = self.config.get("stt_model", "base.en")
        
        # Load the WhisperModel once in __init__
        self.model = WhisperModel(model_size, device="cpu", compute_type="int8")

    def record(self) -> np.ndarray:
        chunk_size = 1024
        # Calculate how many silent frames we need
        frames_needed = int(self.silence_seconds * self.sample_rate / chunk_size)
        silent_frames = 0
        
        audio_buffer = []
        
        # Open a sounddevice.InputStream at config["sample_rate"], mono, float32
        with sd.InputStream(samplerate=self.sample_rate, channels=1, dtype='float32', blocksize=chunk_size) as stream:
            while True:
                chunk, overflowed = stream.read(chunk_size)
                # chunk is a 2D numpy array (chunk_size, 1)
                audio_buffer.append(chunk)

                # calculate RMS for the chunk
                rms = np.sqrt(np.mean(chunk**2))
                
                if rms < self.silence_threshold:
                    silent_frames += 1
                else:
                    silent_frames = 0
                    
                if len(audio_buffer) > frames_needed and silent_frames >= frames_needed:
                    break

        audio_data = np.concatenate(audio_buffer, axis=0).flatten()
        return audio_data

    def transcribe(self, audio: np.ndarray) -> str:
        # Pass the numpy audio array directly to faster_whisper
        language = self.config.get("language", "en")
        segments, info = self.model.transcribe(
            audio, 
            language=language,
            vad_filter=True, 
            beam_size=1
        )
        
        text = "".join(segment.text for segment in segments)
        return text.strip()

    def listen(self) -> str:
        try:
            audio = self.record()
            # If nothing was detected effectively, return empty
            if len(audio) == 0:
                return ""
            return self.transcribe(audio)
        except sd.PortAudioError as e:
            print(f"Error accessing microphone. Please check permissions and connection. Details: {e}")
            return ""
