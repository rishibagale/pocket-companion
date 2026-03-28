@echo off
echo Setting up Pocket Companion...
echo.

echo 1. Installing standard requirements...
pip install -r requirements.txt

echo.
echo 2. Installing KittenTTS...
pip install https://github.com/KittenML/KittenTTS/releases/download/0.8.1/kittentts-0.8.1-py3-none-any.whl

echo.
echo 3. Creating config file...
if not exist config.json (
    copy config.example.json config.json
    echo Created config.json
) else (
    echo config.json already exists
)

echo.
echo 4. Downloading all offline models (this may take a while)...
python download_models.py

echo.
echo Setup Complete! 
echo Make sure Ollama is running in the background, then you can start the application with:
echo python main.py
pause
