import subprocess
import sys
import psutil
import time

from agents.claws.debugger_agent import debug_code

def run_in_sandbox(script_path, code):
    print("\n[AetherShell] Inspecting code environment...")

    start_time = time.time()
    
    try:
        # Start the process
        proc = subprocess.Popen(
            [sys.executable, script_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        p = psutil.Process(proc.pid)
        max_mem = 0
        
        # Monitor Loop
        timeout = 15
        while proc.poll() is None:
            try:
                mem = p.memory_info().rss / (1024 * 1024) # MB
                if mem > max_mem: max_mem = mem
                
                # Security Constraint: Max 256MB
                if mem > 256:
                    print("[AetherShell] CAUTION: Memory limit exceeded (256MB). Terminating.")
                    proc.kill()
                    break
                    
                time.sleep(0.1)
                if time.time() - start_time > timeout:
                    print("[AetherShell] WARNING: Timeout reached.")
                    proc.kill()
                    break
            except psutil.NoSuchProcess:
                break

        stdout, stderr = proc.communicate()
        duration = time.time() - start_time

        print(f"[AetherShell] Stats -> Duration: {duration:.2f}s | Max Memory: {max_mem:.2f}MB")

        if proc.returncode == 0:
            print("[AetherShell] Safety Check: PASS")
            return code
        else:
            print("[AetherShell] Safety Check: FAIL (Error detected)")
            fixed = debug_code(code, stderr)
            with open(script_path, "w", encoding="utf-8") as f:
                f.write(fixed)
            print("[AetherShell] Debugger claw applied fixes.")
            return fixed

    except Exception as e:
        print(f"[AetherShell] Runtime Exception: {str(e)}")
        return code