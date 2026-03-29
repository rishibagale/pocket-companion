# Changelog

All notable changes to this project are documented here.
Format based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Added
- ROADMAP.md: updated to reflect the new feature approvals
- README.md: added placeholder for missing demo.gif

### Fixed
- error handling: prevented bare exceptions across main.py, orchestrator.py, and download_models.py
- config contract: added explicit pip install instructions to tts.py failure mode

## [0.2.0] — 2026-03-29

### Added
- Automated 1-Click setup scripts for Windows (`setup.bat`) and Linux/macOS (`setup.sh`)
- Standalone python model downloader script (`download_models.py`)
- New comprehensive documentation suite (`architecture.md`, `ROADMAP.md`, `FAQ.md`)
- Detailed IoT Device compatibility matrix in `README.md`

### Changed
- `CONTRIBUTING.md` updated with emphasis on automated configuration over manual steps

## [0.1.0] — 2026-03-27

### Added
- Voice input via faster-whisper (base.en, fully offline)
- Local LLM inference via Ollama (default model: gemma3:1b)
- Text-to-speech via KittenTTS with 8 voice options
- Persistent conversation memory across sessions (memory.json)
- Sentence-level LLM streaming for low-latency spoken responses
- State machine: LISTENING / THINKING / SPEAKING / PAUSED
- Voice commands: clear memory, change voice, pause, resume
- Fully configurable via config.json (voice, model, personality, speed)
- Tiered model support from gemma3:1b (phones) to mistral (16GB laptops)
