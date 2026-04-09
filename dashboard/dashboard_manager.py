import os
from datetime import datetime

COMPONENT_FOLDER = "dashboard/components"
LOG_FILE = "logs/dashboard_changes.log"


def component_path(name):

    return os.path.join(COMPONENT_FOLDER, f"{name}.py")


def add_component(name, code):

    os.makedirs(COMPONENT_FOLDER, exist_ok=True)

    path = component_path(name)

    with open(path, "w", encoding="utf-8") as f:
        f.write(code)

    log_change(f"Component added: {name}")

    return path


def modify_component(name, code):

    path = component_path(name)

    if not os.path.exists(path):
        raise FileNotFoundError("Component not found")

    with open(path, "w", encoding="utf-8") as f:
        f.write(code)

    log_change(f"Component modified: {name}")

    return path


def log_change(message):

    os.makedirs("logs", exist_ok=True)

    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} - {message}\n")