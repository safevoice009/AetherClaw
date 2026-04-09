import requests
import time
import os
from utils.telegram_notify import notify
from utils.voice import speak

# AetherNexus Configuration
LM_STUDIO_URL = os.getenv("LLM_API_URL", "http://localhost:1234")
DEFAULT_MODEL = os.getenv("LLM_MODEL_NAME", "phi-4-mini-instruct")

# Tier Mapping (Recommended)
# Strategic: Complex reasoning, planning, architectural decisions (e.g., Gemma-4, Llama-3-70B)
# Tactical: Fast synthesis, coding, boilerplate generation (e.g., Phi-4, Llama-3-8B)
INTELLIGENCE_TIERS = {
    "STRATEGIC": os.getenv("LLM_STRATEGIC_MODEL", DEFAULT_MODEL),
    "TACTICAL": os.getenv("LLM_TACTICAL_MODEL", DEFAULT_MODEL)
}


def get_active_models():
    """Queries the local AetherNexus endpoint for loaded intelligence models."""
    try:
        r = requests.get(f"{LM_STUDIO_URL}/v1/models", timeout=5)
        if r.status_code == 200:
            return [m["id"] for m in r.json()["data"]]
    except Exception:
        return []
    return []


def get_model_for_tier(tier="TACTICAL"):
    """
    Retrieves the optimized model ID for the requested intelligence tier.
    Falls back to the default model if the specific tier model is not loaded.
    """
    target = INTELLIGENCE_TIERS.get(tier.upper(), DEFAULT_MODEL)
    active = get_active_models()
    
    if target in active:
        return target
    
    # Dynamic fallback to the first available model if target isn't loaded
    if active:
        return active[0]
        
    return DEFAULT_MODEL


def check_nexus_resonance():
    """Verifies that the AetherNexus core is active and responding."""
    active = get_active_models()
    return active[0] if active else None


def wait_for_resonance():
    """Blocks execution until the AetherNexus intelligence layer is online."""
    print("[AETHER-CORE] Checking Nexus resonance...")
    last_model = None

    while True:
        model = check_nexus_resonance()
        if model:
            if model != last_model:
                msg = f"Nexus Resonance Established: {model} active."
                print(f"[AETHER-CORE] {msg}")
                notify(msg)
                speak("Intelligence layer synchronized.")
                last_model = model
            return model

        print("[AETHER-CORE] Waiting for Nexus resonance (verify LLM backend is running)...")
        time.sleep(5)
