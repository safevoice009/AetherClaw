import requests

def get_messages(token):

    url = f"https://api.telegram.org/bot{token}/getUpdates"

    r = requests.get(url)

    return r.json()