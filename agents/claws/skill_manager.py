import os
import importlib.util

SKILL_FOLDER = "skills"


def skill_path(name):

    return os.path.join(SKILL_FOLDER, f"{name}.py")


# -----------------------------
# check if skill exists
# -----------------------------

def skill_exists(name):

    return os.path.exists(skill_path(name))


# -----------------------------
# save new skill
# -----------------------------

def save_skill(name, code):

    os.makedirs(SKILL_FOLDER, exist_ok=True)

    path = skill_path(name)

    with open(path, "w", encoding="utf-8") as f:
        f.write(code)

    return path


# -----------------------------
# load skill dynamically
# -----------------------------

def load_skill(name):

    path = skill_path(name)

    if not os.path.exists(path):

        raise FileNotFoundError(f"Skill {name} not found")

    spec = importlib.util.spec_from_file_location(name, path)

    module = importlib.util.module_from_spec(spec)

    spec.loader.exec_module(module)

    return module


# -----------------------------
# list available skills
# -----------------------------

def list_skills():

    if not os.path.exists(SKILL_FOLDER):
        return []

    files = os.listdir(SKILL_FOLDER)

    return [f.replace(".py", "") for f in files if f.endswith(".py")]