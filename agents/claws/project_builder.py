"""
AetherClaw Project Builder
Responsible for architecting the file structure and managing the AetherShell execution state.
"""

import os
from .workspace_guard import ensure_workspace_path, check_file_size
from .execution_sandbox import run_in_sandbox

# Root directory for all AetherClaw generated projects
PROJECT_ROOT = "projects"

def create_project(name, code):
    """
    Creates a new project directory and initializes the main execution file.
    Triggers AetherShell for validation and potential AetherFlow refinement.
    """
    check_file_size(code)

    path = ensure_workspace_path(os.path.join(PROJECT_ROOT, name))
    os.makedirs(path, exist_ok=True)

    main_file = os.path.join(path, "main.py")

    with open(main_file, "w", encoding="utf-8") as f:
        f.write(code)

    # Validate execution within AetherShell
    print(f"[AetherClaw] Initializing AetherShell for {name}...")
    fixed_code = run_in_sandbox(main_file, code)

    # Persist improvements from the AetherShell debugging cycle
    if fixed_code != code:
        print(f"[AetherClaw] AetherShell detected and resolved issues in {name}. Updating source...")
        with open(main_file, "w", encoding="utf-8") as f:
            f.write(fixed_code)

    return main_file