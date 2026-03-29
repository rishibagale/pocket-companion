# Contributing to Pocket Companion

Thanks for your interest. Here's everything you need to know.

## Reporting bugs

Open an issue and include:
- Your OS, Python version, and available RAM
- The exact command you ran and the full error output
- Which Ollama model you are using

## Suggesting features

Open an issue with the label `enhancement`. Describe the use case, not just
the feature — "I want X because Y" is much more useful than "add X".

## Submitting a PR

1. Fork the repo
2. Create a branch: `git checkout -b feature/your-thing`
3. Make focused changes — one concern per PR
4. Test functionality on fresh setups using `setup.bat` (Windows) or `./setup.sh` (macOS/Linux)
5. Test: `python main.py` must run without errors
6. Open a PR against `main` with a clear description of what changed and why

## Code style

- Python 3.12, PEP 8, max line length 88
- Type hints on all public methods
- No circular imports — stt.py, llm.py, tts.py must not import each other
- Comments only on non-obvious logic
- Functions under 40 lines

## What's out of scope for now

These are not in the roadmap for v0.x and PRs for them will be closed:
- GUI / web interface
- Wake word detection
- Cloud LLM fallback
- Docker / containers
- Multi-user profiles

Open an issue to discuss before starting large changes.
