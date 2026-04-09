\"\"\"
AetherClaw AetherAudit Skill
Performs non-destructive, tactical audits on local directories for security, PII, and quality.
\"\"\"

import os
import re

# Directives for detection
PII_PATTERNS = [
    r'[\w\.-]+@[\w\.-]+\.\w+',  # Emails
    r'\b\d{3}-\d{2}-\d{4}\b',   # SSNs
    r'password\s*=\s*["\'].*["\']', # Plaintext passwords
    r'api_key\s*=\s*["\'].*["\']',  # API Keys
]

SECURITY_PATTERNS = [
    (r'eval\(', "High Risk: 'eval()' usage detected."),
    (r'exec\(', "High Risk: 'exec()' usage detected."),
    (r'os\.system\(', "Medium Risk: 'os.system()' usage detected. Use subprocess instead."),
]


def audit_directory(directory_path):
    """Executes a full tactical audit of the specified local directory."""
    print(f"[AetherAudit] Initializing tactical scan of: {directory_path}")
    
    findings = []
    
    if not os.path.exists(directory_path):
        return f"Error: Directory {directory_path} not found."

    for root, dirs, files in os.walk(directory_path):
        # Skip unnecessary directories
        if any(skip in root for skip in ['.git', '__pycache__', 'projects', 'logs']):
            continue

        for file in files:
            if file.endswith(('.py', '.js', '.txt', '.env', '.md')):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        
                        # Check for PII
                        for pattern in PII_PATTERNS:
                            if re.search(pattern, content, re.IGNORECASE):
                                findings.append(f"[PII/LEAK] Potential sensitive data in: {file_path}")
                        
                        # Check for Security
                        for pattern, msg in SECURITY_PATTERNS:
                            if re.search(pattern, content):
                                findings.append(f"[SECURITY] {msg} in: {file_path}")
                                
                except Exception as e:
                    findings.append(f"[ERROR] Could not audit {file_path}: {e}")

    if not findings:
        return "Audit Complete: Zero critical vulnerabilities detected. Directory state: STERILE."
    
    report = "\n".join(findings)
    return f"Tactical Audit Results:\n{'-'*30}\n{report}\n{'-'*30}\nAetherGuard recommends immediate remedial synthesis."


if __name__ == "__main__":
    import sys
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    print(audit_directory(path))
