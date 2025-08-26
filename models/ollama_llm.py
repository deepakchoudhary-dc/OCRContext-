import requests
import json

class OllamaLLM:
    def __init__(self, model='qwen3:1.7b', host='http://localhost:11434'):
        self.model = model
        self.host = host

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
            response = requests.post(url, json=payload)
            response.raise_for_status()
            result = response.json()
            return result.get('response', '')
        except json.JSONDecodeError as e:
            print(f"JSON decode error: {e}")
            print(f"Response text: {response.text}")
            return "Error: Could not parse LLM response"
        except Exception as e:
            print(f"Error during LLM query: {e}")
            return f"Error: {str(e)}" 