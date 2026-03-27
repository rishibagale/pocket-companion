# Pocket Companion

Fully offline voice AI companion — speak naturally, get spoken replies. Runs on any device, no internet required.

![Python](https://img.shields.io/badge/python-3.12-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Offline](https://img.shields.io/badge/runs-offline-brightgreen)

![Demo](demo.gif)

## Quick start

```bash
git clone https://github.com/rishibagale/pocket-companion
cd pocket-companion
pip install -r requirements.txt
pip install https://github.com/KittenML/KittenTTS/releases/download/0.8.1/kittentts-0.8.1-py3-none-any.whl
ollama pull gemma3:1b
cp config.example.json config.json
python main.py
```

## How it works

Pocket Companion uses a local speech-to-text engine to transcribe audio, securely passes the transcription into an offline Ollama language model, and plays the response continuously using KittenTTS. For an overview of how these modules fit together, see the [Architecture Diagram](architecture.md).

## Requirements

- **OS:** Windows / macOS / Linux
- **Python:** 3.12+
- **Ollama:** Installed and running locally
- **Hardware Minimum:** 2GB RAM (see model recommendations below)

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
