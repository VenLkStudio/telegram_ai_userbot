import requests

def AI_ollama_api_send(url_ollama, prompt_text):
    ollama_url = f"http://{url_ollama}:11434/api/generate"
    data = {
        "model": "llama3.1",  
        "prompt": prompt_text,
        "stream": False
    }

    response = requests.post(ollama_url, json=data)

    if response.status_code == 200:
        reply = response.json()
        # print("Ответ модели:", reply['response'])
        return reply['response']
    else:
        print(f"Ошибка: {response.status_code} - {response.text}")
