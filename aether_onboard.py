\"\"\"
🌌 AetherOnboard: Interactive Configuration Wizard
Helps users set up their AetherClaw environment via the command line.
\"\"\"

import os
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_input(prompt, default=None):
    if default:
        user_input = input(f"{prompt} [{default}]: ").strip()
        return user_input if user_input else default
    else:
        return input(f"{prompt}: ").strip()

def run_onboarding():
    clear_screen()
    print("🌌 [AetherClaw v3.0] Universal Onboarding Wizard")
    print("="*50)
    print("This utility will configure your tactical environment.")
    print("-" * 50)

    # 1. API Configuration
    print("\n[PART 1: LLM CONNECTIVITY]")
    api_url = get_input("Enter LLM API URL (e.g. LM Studio, Ollama)", "http://localhost:1234")
    strategic_model = get_input("Strategic Model Name (Architecture)", "phi-4-mini-instruct")
    tactical_model = get_input("Tactical Model Name (Coding/Review)", "phi-4-mini-instruct")

    # 2. Search Integration
    print("\n[PART 2: RESEARCH CAPABILITIES (Optional)]")
    serper_key = get_input("Enter Serper.dev API Key (leave blank to skip)", "")

    # 3. Telegram Integration
    print("\n[PART 3: NEXUS CONNECTIVITY (Telegram Bot)]")
    tg_token = get_input("Enter Telegram Bot Token (leave blank to skip)", "")
    tg_id = get_input("Enter Telegram Chat ID (leave blank to skip)", "")

    # Save to .env
    env_content = f"""# AetherClaw Nexus Configuration
LLM_API_URL={api_url}
LLM_MODEL_NAME={strategic_model}
LLM_STRATEGIC_MODEL={strategic_model}
LLM_TACTICAL_MODEL={tactical_model}

# Tactical Skills
SERPER_API_KEY={serper_key}

# Telegram Bridge
TELEGRAM_BOT_TOKEN={tg_token}
TELEGRAM_CHAT_ID={tg_id}
"""

    with open(".env", "w") as f:
        f.write(env_content)

    print("\n" + "="*50)
    print("✅ CONFIGURATION CRYSTALLIZED.")
    print("Your environment is now optimized for AetherFlow deployment.")
    print("="*50)
    print("\nTry running: python supervisor/aether_lite.py 'Create a weather app with Python'")

if __name__ == "__main__":
    run_onboarding()
