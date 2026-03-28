# Pocket Companion

Fully offline voice AI companion — speak naturally, get spoken replies. Runs on any device, no internet required.

![Python](https://img.shields.io/badge/python-3.12-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Offline](https://img.shields.io/badge/runs-offline-brightgreen)

![Demo](demo.gif)

## Quick start (1-Click Setup)

For compact / low-memory devices (2GB - 4GB RAM), we provide a one-shot setup script which fetches the recommended `gemma3:1b` model, the STT models, and the TTS models automatically.

### Windows
```batch
git clone https://github.com/rishibagale/pocket-companion
cd pocket-companion
setup.bat
```

### Linux / macOS
```bash
git clone https://github.com/rishibagale/pocket-companion
cd pocket-companion
chmod +x setup.sh
./setup.sh
```

**Manual Installation:**
```bash
pip install -r requirements.txt
pip install https://github.com/KittenML/KittenTTS/releases/download/0.8.1/kittentts-0.8.1-py3-none-any.whl
cp config.example.json config.json
python download_models.py
python main.py
```

## How it works

Pocket Companion uses a local speech-to-text engine to transcribe audio, securely passes the transcription into an offline Ollama language model, and plays the response continuously using KittenTTS. For an overview of how these modules fit together, see the [Architecture Diagram](architecture.md).

## Requirements

- **OS:** Windows / macOS / Linux
- **Python:** 3.12+
- **Ollama:** Installed and running locally
- **Hardware Minimum:** 2GB RAM (see model recommendations below)

## IoT Device Compatibility

This project works natively on "heavy" IoT edge devices (Single Board Computers) since the combined offline models take ~1.2 GB RAM, but the models are far too large to execute on microcontrollers. 

**✅ Supported IoT Devices:** 
Requires an SBC with a 64-bit architecture (ARM64) and at least 2GB RAM running Linux.
- Raspberry Pi 4 / Raspberry Pi 5 (2GB/4GB/8GB)
- NVIDIA Jetson Nano
- Orange Pi / Rock Pi / Mini PCs

**❌ Unsupported IoT Devices:**
Microcontrollers with only kilobytes or megabytes of RAM do not have the capacity or OS support to run these models locally.
- ESP32, ESP8266, Arduino boards, Raspberry Pi Pico
- *Alternative:* If you want to use cheap $5 WiFi chips like the ESP32 as a "smart speaker", you must run Pocket Companion on a central server (like a Raspberry Pi 4) and use the ESP32 to stream microphone audio over Wi-Fi.

## Installation

1. Clone the repository and install requirements.
2. Install KittenTTS directly from GitHub releases via the `pip` command outlined in Quick start.
3. Start the Ollama server and pull a compatible model.
4. Copy `config.example.json` to `config.json` and adjust as necessary.

## Configuration

The AI behavior and application properties run from `config.json`:

| Field | Description |
|---|---|
| `voice` | Name of the KittenTTS voice to use |
| `model` | Exact name of the Ollama model for inference |
| `language` | STT transcription language |
| `system_prompt` | Instructions establishing the AI personality and constraints |
| `memory_turns` | Number of previous conversant exchanges retained in context |
| `tts_speed` | Speech output speed |
| `stt_model` | Faster-whisper base model size |
| `silence_threshold` | Minimum volume threshold to listen for |
| `silence_seconds` | Seconds elapsed before an utterance is parsed |
| `sample_rate` | Audio input sample rate (Hz) |

## Choosing a model

Ensure you pull the correct local LLM depending on your device specs:

| Your device               | Recommended model     | Command                       |
|---------------------------|-----------------------|-------------------------------|
| Phone / old laptop (2GB)  | `gemma3:1b` (~815MB)  | `ollama pull gemma3:1b`       |
| Basic laptop (4GB)        | `llama3.2:1b`         | `ollama pull llama3.2:1b`     |
| Normal laptop (8GB)       | `llama3.2` (3B)       | `ollama pull llama3.2`        |
| Good laptop (16GB+)       | `mistral`             | `ollama pull mistral`         |

## Voice commands

Control the application by speaking directly to it:

| Say                         | What happens                          |
|-----------------------------|---------------------------------------|
| "stop listening"            | Companion pauses, stops transcribing  |
| "start listening"           | Resumes from pause                    |
| "clear memory"              | Wipes conversation history            |
| "change voice to Luna"      | Switches TTS voice at runtime         |
| "what model are you using"  | Companion speaks the current model    |

## Contributing

We welcome contributions to Pocket Companion. See the [CONTRIBUTING.md](CONTRIBUTING.md) guide for guidelines on opening issues and PRs.

## License

MIT © 2026 rishibagale
