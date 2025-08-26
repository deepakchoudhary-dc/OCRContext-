import requests
import json
import os

class OllamaLLM:
    def __init__(self, model='qwen3:1.7b', host=None):
        self.model = model
        self.host = host or os.getenv('OLLAMA_HOST', 'http://localhost:11434')

    def generate(self, prompt, system=None):
        url = f'{self.host}/api/generate'
        payload = {
            'model': self.model,
            'prompt': prompt,
            'stream': False  # Disable streaming to get a single JSON response
        }
        if system:
            payload['system'] = system
        
        try:
            response = requests.post(url, json=payload, timeout=10)
            response.raise_for_status()
            result = response.json()
            return result.get('response', '')
        except requests.exceptions.ConnectionError:
            return "🔄 Demo Mode: Local LLM (Ollama) not available. This would normally provide AI-powered answers based on your document content. For full functionality, run locally with Ollama."
        except requests.exceptions.Timeout:
            return "⏱️ LLM request timed out. The model may be loading or unavailable."
        except json.JSONDecodeError as e:
            print(f"JSON decode error: {e}")
            print(f"Response text: {response.text}")
            return "Error: Could not parse LLM response"
        except Exception as e:
            print(f"Error during LLM query: {e}")
            return f"Error: {str(e)}" 