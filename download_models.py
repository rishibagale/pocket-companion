import os
import sys
import subprocess
import json

def main():
    print("Welcome to Pocket Companion Model Downloader")
    print("This script will download all necessary offline models for 2-4GB RAM devices.")
    print("Models to be downloaded:")
    print("1. STT: faster-whisper (base.en)")
    print("2. TTS: KittenTTS (KittenML/kitten-tts-mini-0.8)")
    print("3. LLM: gemma3:1b (via Ollama)")
    print("-" * 50)
    
    # 1. STT
    print("\n--- 1. Downloading Speech-to-Text Model ---")
    try:
        from faster_whisper import WhisperModel
        print("Downloading 'base.en' model. This may take a moment...")
        # Instantiating the model forces the download 
        WhisperModel("base.en", device="cpu", compute_type="int8")
        print("STT model downloaded successfully.")
    except ImportError:
        print("[!] faster-whisper not installed. Please run: pip install -r requirements.txt")
    except Exception as e:
        print(f"[!] Error downloading STT model: {e}")

    # 2. TTS
    print("\n--- 2. Downloading Text-to-Speech Model ---")
    try:
        from kittentts import KittenTTS
        print("Downloading 'KittenML/kitten-tts-mini-0.8' model...")
        KittenTTS(model_name="KittenML/kitten-tts-mini-0.8")
        print("TTS model downloaded successfully.")
    except ImportError:
        print("[!] KittenTTS not installed. Please follow the README to install it.")
    except Exception as e:
        print(f"[!] Error downloading TTS model: {e}")

    # 3. LLM
    print("\n--- 3. Downloading LLM via Ollama ---")
    model_name = "gemma3:1b"
    
    # Optional: read from config if it exists
    if os.path.exists("config.json"):
        try:
            with open("config.json", "r") as f:
                config = json.load(f)
                if "model" in config:
                    model_name = config["model"]
        except Exception:
            pass

    print(f"Pulling '{model_name}' from Ollama...")
    print("Note: This step requires Ollama to be installed and running in the background.")
    try:
        subprocess.run(["ollama", "pull", model_name], check=True)
        print(f"LLM model '{model_name}' downloaded successfully.")
    except FileNotFoundError:
        print("[!] Ollama is not installed or not in PATH. Please install Ollama from https://ollama.com/")
        print("Once installed and running, you can rerun this script or manually run: ollama pull", model_name)
    except subprocess.CalledProcessError:
        print(f"[!] Failed to pull {model_name}. Is the Ollama app running?")
        
    print("-" * 50)
    print("\nDownload process complete! If there were no errors, you can now run main.py completely offline.")

if __name__ == "__main__":
    main()
