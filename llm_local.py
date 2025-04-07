import requests

def call_local_llm(prompt, model="codellama"):
    url = "http://localhost:11434/api/generate"
    response = requests.post(url, json={
        "model": model,
        "prompt": prompt,
        "stream": False 
    })
    if response.status_code == 200:
        return response.json()["response"].strip()
    else:
        return f"Error: {response.status_code} - {response.text}"
