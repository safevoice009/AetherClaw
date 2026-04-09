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


def ask_llm(prompt, temperature=0.2, max_tokens=800):

    s = get_session()

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": temperature,
        "max_tokens": max_tokens
    }

    r = s.post(API_URL, json=payload, timeout=600)

    r.raise_for_status()

    return r.json()["choices"][0]["message"]["content"]