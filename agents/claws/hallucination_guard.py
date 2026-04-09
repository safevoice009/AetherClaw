"""
AetherClaw Hallucination Guard
Detects and prevents the use of non-existent libraries or hallucinated facts in generated code.
"""

import re

# Blocklist of known hallucination patterns
BLACKLIST = [
    "import imaginarylib",
    "import nonexistlib"
]

def check_code(code):
    for item in BLACKLIST:
        if item in code:
            raise ValueError(f"AetherGuard Alert: Hallucinated library '{item}' detected.")
    return True