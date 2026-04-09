\"\"\"
🌌 AetherNexus Bot (v3.0)
Tactical Telegram interface for the AetherClaw swarm.
Allows for remote objective deployment and system monitoring.
\"\"\"

import requests
import os
import time
import sys
from dotenv import load_dotenv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
API_URL = f"https://api.telegram.org/bot{TOKEN}"

def send_msg(text):
    if not TOKEN or not CHAT_ID: return
    requests.post(f"{API_URL}/sendMessage", json={"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"})

def get_updates(offset=None):
    params = {"timeout": 30, "offset": offset}
    try:
        r = requests.get(f"{API_URL}/getUpdates", params=params)
        return r.json().get("result", [])
    except:
        return []

def handle_command(text):
    text = text.strip()
    if text.startswith("/start"):
        return "🌌 *AetherClaw v3.0 Online*\nSend an objective to begin autonomous deployment.\nCommands:\n/deploy [goal]\n/status\n/audit [path]"
    
    if text.startswith("/deploy"):
        goal = text.replace("/deploy", "").strip()
        if not goal: return "⚠️ Please specify a goal."
        
        # Broadcast to AetherFlow
        os.makedirs("logs", exist_ok=True)
        with open("logs/commands.log", "a") as f:
            f.write(f"BUILD:{goal}\n")
        return f"🚀 *Objective Queued:* {goal}"
    
    if text.startswith("/status"):
        if os.path.exists("logs/agent_status.log"):
            with open("logs/agent_status.log", "r") as f:
                lines = f.readlines()
            status = lines[-1] if lines else "Idle"
            return f"🛰️ *Swarm Status:* {status}"
        return "🛰️ *Swarm Status:* Inactive"

    if text.startswith("/audit"):
        path = text.replace("/audit", "").strip() or "."
        return f"🔍 *Audit Initiation:* Scanning `{path}`... (Check Dashboard for report)"

    return None

def start_bot():
    if not TOKEN:
        print("❌ TELEGRAM_BOT_TOKEN missing in .env")
        return

    print("🌌 AetherNexus Bot listening for tactical commands...")
    send_msg("🛰️ *AetherClaw Nexus Online.* Awaiting objectives.")
    
    offset = None
    while True:
        updates = get_updates(offset)
        for update in updates:
            offset = update["update_id"] + 1
            if "message" in update and "text" in update["message"]:
                chat_id = str(update["message"]["chat"]["id"])
                if chat_id != CHAT_ID:
                    continue
                    
                msg_text = update["message"]["text"]
                response = handle_command(msg_text)
                if response:
                    send_msg(response)
        
        time.sleep(1)

if __name__ == "__main__":
    start_bot()
