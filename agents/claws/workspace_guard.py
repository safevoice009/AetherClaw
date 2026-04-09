\"\"\"
AetherClaw AetherGuard: Directive 1.0 (Directory Sovereignty)
Enforces strict workspace isolation and resource quotas for autonomous agents.
\"\"\"

import os

# Physical perimeter of the active workspace
WORKSPACE_PHYSICAL_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

# Cognitive output boundary (200 KB)
MAX_SYNTHESIS_SIZE = 200_000


def ensure_workspace_path(path):
    """Enforces absolute path sovereignty, preventing agent boundary escape."""
    abs_path = os.path.abspath(path)

    if not abs_path.startswith(WORKSPACE_PHYSICAL_ROOT):
        log(f"Sovereignty Violation: Attempted access outside defined boundary: {abs_path}")
        raise PermissionError("AetherGuard: Directive 1.0 violation. Access outside AI_WORKSPACE denied.")

    return abs_path


def check_file_size(code):
    """Validates that synthesized artifacts remain within defined resource quotas."""
    size = len(code.encode("utf-8"))

    if size > MAX_SYNTHESIS_SIZE:
        log(f"Quota Exception: Synthetic artifact exceeds Directive 1.0 limit ({size} bytes).")
        raise ValueError(
            f"AetherGuard: Directive 1.0 violation. Synthesis size {size} exceeds {MAX_SYNTHESIS_SIZE} quota."
        )


def log(message):
    """Internal AetherGuard logger."""
    try:
        from datetime import datetime
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[AETHER-CORE] {timestamp} | {message}")
    except:
        print(f"[AETHER-CORE] {message}")