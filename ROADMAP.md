# Roadmap

Pocket Companion is currently in the `v0.x` pre-release phase. Below is a high-level roadmap of intended features prioritizing privacy and offline availability.

### v0.x Phase (Current)
- [x] Basic STT -> LLM -> TTS loop
- [x] Persistent conversational memory
- [x] Runtime voice commands ("stop listening", "change voice")
- [x] Installer scripts for lightweight/IoT environments
- [ ] Add streaming transcription chunks for zero-latency turn-taking
- [ ] Automated memory pruning to prevent context overflow 

### v1.0 Release
- [ ] Full streaming audio pipeline (interrupting the companion by talking over them)
- [ ] Multi-lingual localized prompting
- [ ] Integration of Vision models (if camera hardware is present)

### Out of Scope
The following features are **not** planned:
- Web-based GUI
- Cloud LLM API fallbacks (e.g. OpenAI keys)
- Web searching / internet access tools
