# Changelog

All notable changes to this project are documented here.
Format based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

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
