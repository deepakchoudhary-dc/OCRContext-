import requests
import json

class OllamaLLM:
    def __init__(self, model='qwen3:1.7b', host='http://localhost:11434'):
        self.model = model
        self.host = host

    def generate(self, prompt, system=None):
        # Check if running in cloud environment
        if not self._is_ollama_available():
            return "This demo is running in a cloud environment. Local LLM (Ollama) is not available. Please run locally for full functionality."
        
        url = f'{self.host}/api/generate'
        payload = {
            'model': self.model,
            'prompt': prompt,
            'stream': False  # Disable streaming to get a single JSON response
        }
        if system:
            payload['system'] = system
        
        try:
            response = requests.post(url, json=payload, timeout=30)
            response.raise_for_status()
            result = response.json()
            return result.get('response', '')
        except requests.exceptions.ConnectionError:
            return "Error: Cannot connect to Ollama. Please ensure Ollama is running locally."
        except requests.exceptions.Timeout:
            return "Error: Ollama request timed out. The model may be loading."
        except json.JSONDecodeError as e:
            print(f"JSON decode error: {e}")
            print(f"Response text: {response.text}")
            return "Error: Could not parse LLM response"
        except Exception as e:
            print(f"Error during LLM query: {e}")
            return f"Error: {str(e)}"
    
    def _is_ollama_available(self):
        try:
            response = requests.get(f'{self.host}/api/tags', timeout=5)
            return response.status_code == 200
        except:
            return False 