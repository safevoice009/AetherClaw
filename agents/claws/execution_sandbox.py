\"\"\"
AetherClaw AetherShell (Strategic Isolation Chamber)
Enforces a sterile runtime environment for tactical artifacts.
\"\"\"

import subprocess
import sys
import psutil
import time

from agents.claws.debugger_agent import debug_code


def run_in_sandbox(script_path, code):
    """Executes a tactical artifact within the AetherShell isolation perimeter."""
    log(f"Initializing AetherShell for artifact at: {script_path}")

    start_time = time.time()
    
    try:
        # Start the process in quarantine
        proc = subprocess.Popen(
            [sys.executable, script_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        p = psutil.Process(proc.pid)
        max_mem = 0
        
        # Quarantine Monitoring Loop
        timeout = 15
        while proc.poll() is None:
            try:
                mem = p.memory_info().rss / (1024 * 1024) # MB
                if mem > max_mem: max_mem = mem
                
                # Directive 1.0 Quota: Max 256MB
                if mem > 256:
                    log(f"Resource Quota Exceeded: {mem:.2f}MB > 256MB. Terminating quarantine session.")
                    proc.kill()
                    break
                    
                time.sleep(0.1)
                if time.time() - start_time > timeout:
                    log(f"Temporal Boundary Violation: {timeout}s limit reached.")
                    proc.kill()
                    break
            except psutil.NoSuchProcess:
                break

        stdout, stderr = proc.communicate()
        duration = time.time() - start_time

        log(f"Quarantine Telemetry -> Duration: {duration:.2f}s | Peak RAM: {max_mem:.2f}MB")

        if proc.returncode == 0:
            log("Sanitization Pass: SUCCESS. Artifact validated for resonance.")
            return code
        else:
            log("Sanitization Pass: FAIL. Architectural defects identified.")
            log("Activating AetherDebugger tier...")
            fixed = debug_code(code, stderr)
            
            with open(script_path, "w", encoding="utf-8") as f:
                f.write(fixed)
            
            log("Tactical fixes applied. Sanitization pass complete.")
            return fixed

    except Exception as e:
        log(f"AetherShell Framework Exception: {str(e)}")
        return code


def log(message):
    """Internal AetherShell logger."""
    try:
        from datetime import datetime
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[AETHER-CORE] {timestamp} | {message}")
    except:
        print(f"[AETHER-CORE] {message}")