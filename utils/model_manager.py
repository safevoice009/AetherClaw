import requests
import time

from utils.telegram_notify import notify
from utils.voice import speak

LM_STUDIO = "http://localhost:1234"


def check_model():

    try:

        r = requests.get(f"{LM_STUDIO}/v1/models")

        if r.status_code == 200:

            models = r.json()["data"]

            if models:
                return models[0]["id"]

    except Exception:

        return None


def wait_for_model():

    print("[ModelManager] checking model")

    last_model = None

    while True:

        model = check_model()

        if model:

            if model != last_model:

                msg = f"Model active: {model}"

                print("[ModelManager]", msg)

                notify(msg)

                speak(msg)

                last_model = model

            return model

        print("[ModelManager] waiting for model to load")

        time.sleep(5)



from utils.model_manager import wait_for_model

wait_for_model()
plan = planner(goal)


