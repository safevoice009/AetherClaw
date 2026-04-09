\"\"\"
AetherClaw AetherNexus (Skill Manager)
Dynamically manages and injects tactical capabilities into the AetherFlow loop.
\"\"\"

import os
import importlib.util

SKILL_FOLDER = "skills"


def skill_path(name):
    """Resolves the physical address of a tactical skill."""
    return os.path.join(SKILL_FOLDER, f"{name}.py")


def skill_exists(name):
    """Verifies the availability of a specific cognitive capability."""
    return os.path.exists(skill_path(name))


def save_skill(name, code):
    """Crystallizes a new capability into the AetherNexus repository."""
    os.makedirs(SKILL_FOLDER, exist_ok=True)
    path = skill_path(name)

    with open(path, "w", encoding="utf-8") as f:
        f.write(code)
    
    log(f"New capability crystallized at Nexus endpoint: {name}")
    return path


def load_skill(name):
    """Dynamically integrates a tactical skill into the active swarm session."""
    path = skill_path(name)

    if not os.path.exists(path):
        log(f"Capability Exception: Nexus endpoint {name} unavailable.")
        raise FileNotFoundError(f"Skill {name} not found")

    log(f"Activating capability: {name}...")
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    return module


def list_skills():
    """Inventories all synchronized capabilities within the AetherNexus."""
    if not os.path.exists(SKILL_FOLDER):
        return []

    files = os.listdir(SKILL_FOLDER)
    return [f.replace(".py", "") for f in files if f.endswith(".py")]


def log(message):
    """Internal AetherNexus logger."""
    try:
        from datetime import datetime
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[AETHER-CORE] {timestamp} | {message}")
    except:
        print(f"[AETHER-CORE] {message}")