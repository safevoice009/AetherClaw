\"\"\"
AetherClaw AetherLink (Tactical Connectivity Layer)
Enforces domain sovereignty and ensures secure external data ingestion.
\"\"\"

import requests

# Authorized Domain Perimeter
AUTHORIZED_DOMAINS = [
    "github.com",
    "pypi.org",
    "docs.python.org",
    "pypi.python.org",
    "pythonhosted.org",
    "raw.githubusercontent.com"
]

def fetch(url):
    """Executes a secure data ingestion from an authorized external coordinate."""
    
    if not any(domain in url for domain in AUTHORIZED_DOMAINS):
        log(f"Perimeter Violation: Unauthorized access attempt to {url}")
        raise PermissionError(f"AetherLink Constraint: Domain sovereignty violation for {url}")

    log(f"Ingesting external data from authorized coordinate: {url}")
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except Exception as e:
        log(f"AetherLink Exception: Connectivity failure for {url}. Details: {e}")
        raise

def log(message):
    """Internal AetherLink logger."""
    try:
        from datetime import datetime
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[AETHER-CORE] {timestamp} | {message}")
    except:
        print(f"[AETHER-CORE] {message}")