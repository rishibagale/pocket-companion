# Frequently Asked Questions (FAQ)

### 1. Is my data sent to the cloud?
**No.** Pocket Companion is built with a strict offline-first philosophy. Once you download the models using the setup scripts, zero network requests are made. Your `memory.json` conversation file stays strictly on your hard drive.

### 2. Can I run this on a Raspberry Pi or IoT Device?
**Yes, on heavy IoT edge devices.** You can run this cleanly on a Raspberry Pi 4/5 (2GB RAM or higher model) or NVIDIA Jetson Nano. 
However, you **cannot** run this on tiny microcontrollers like an ESP32 or Arduino, because they do not have enough RAM (requires ~1.2 GB RAM total) nor a compatible 64-bit OS.

### 3. Why are the responses slow to generate?
Local AI generation depends heavily on your CPU and RAM speed. If it's taking too long:
- Ensure no heavy background processes are running.
- Drop to a smaller LLM. In `config.json`, change the model to `gemma3:1b` or even `qwen2.5:0.5b` (make sure you `ollama pull` it first).
- Use a faster, quantized model structure.

### 4. How do I change the text-to-speech voice?
You can either say "change voice to [Name]" while talking to the companion, or shut down the application and modify the `"voice"` key in `config.json`. Available KittenTTS voices include Luna, Bella, and others listed in the KittenML documentation.

### 5. My microphone isn't being detected, what do I do?
The application relies on `sounddevice`. Check that your default system recording device is set correctly. On Linux, ensure `portaudio` and `alsa-utils` are installed properly.
