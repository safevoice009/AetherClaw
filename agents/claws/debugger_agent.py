"""
AetherClaw Debugger Agent
Part of the AetherFlow loop, providing rapid auto-correction for execution errors.
"""

from agents.claws.orchestrator import developer

def debug_code(code, error):
    prompt = f"""
The following Python code produced an error in the AetherShell.

CODE:
{code}

ERROR:
{error}

Fix the code and return ONLY the corrected Python code.
"""
    return developer(prompt)