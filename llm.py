import requests
import json
from typing import Generator

class LLM:
    def __init__(self, config: dict):
        self.config = config
        self.chat_url = "http://localhost:11434/api/chat"
        self.tags_url = "http://localhost:11434/api/tags"

    def check_connection(self) -> bool:
        try:
            response = requests.get(self.tags_url, timeout=2.0)
            return response.status_code == 200
        except requests.RequestException:
            return False

    def stream(self, messages: list[dict]) -> Generator[str, None, None]:
        if not self.check_connection():
            raise ConnectionError("Error: Ollama is not running. Start it with: ollama serve")
            
        payload = {
            "model": self.config.get("model", "llama3.2"),
            "messages": messages,
            "stream": True
        }
        
        try:
            with requests.post(self.chat_url, json=payload, stream=True) as response:
                response.raise_for_status()
                for line in response.iter_lines():
                    if line:
                        data = json.loads(line.decode('utf-8'))
                        if "message" in data and "content" in data["message"]:
                            yield data["message"]["content"]
                        
                        if data.get("done"):
                            break
        except requests.RequestException as e:
            raise ConnectionError(f"Error connecting to Ollama: {e}")
