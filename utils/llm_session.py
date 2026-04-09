import requests
import time
import os

API_URL = os.getenv("LLM_API_URL", "http://localhost:1234/v1/chat/completions")
MODEL_NAME = os.getenv("LLM_MODEL_NAME", "phi-4-mini-instruct")

session = None


def get_session():

    global session

    if session is None:
        session = requests.Session()

    return session


def ask_llm(prompt, temperature=0.2, max_tokens=2000, model=None):
    """Executes a request to the AetherNexus intelligence layer."""
    s = get_session()
    
    # Dynamic model selection
    target_model = model if model else MODEL_NAME

    payload = {
        "model": target_model,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": temperature,
        "max_tokens": max_tokens
    }

    try:
        r = s.post(API_URL, json=payload, timeout=600)
        r.raise_for_status()
        return r.json()["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"[AETHER-CORE] Nexus Communication Error: {e}")
        raise
