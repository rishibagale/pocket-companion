# Roadmap

Pocket Companion is currently in the `v0.x` pre-release phase. Below is a high-level roadmap of intended features prioritizing privacy and offline availability.

## Feature roadmap (approved future work)

### v0.2.0
- `logger.py` — structured logging to companion.log with log rotation, replacing all print statements in orchestrator
- Interrupt support — user can speak while TTS is playing to cut it off
- `--voice` and `--model` CLI flags in main.py to override config at launch

### v0.3.0
- Wake word detection — listen passively, only activate on trigger phrase (use pvporcupine or a simple keyword spotter)
- `ROADMAP.md` — public roadmap file so contributors know what is planned

### v0.4.0
- Optional minimal GUI — tkinter window showing live transcript, mute button, voice selector dropdown
- Auto-updater — check GitHub releases API for new version on startup, notify user if one exists (read-only, never auto-install)

## Out of scope (do not implement)
The following features are **not** planned:
- Cloud LLM fallback
- Docker / containers
- Multi-user profiles
- Web interface
- Any feature requiring a network call to an external server
