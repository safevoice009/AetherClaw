"""
AetherClaw System Guard
Manages resource efficiency and ensures system stability during heavy workloads.
"""

import time
import psutil

COOLDOWN_SECONDS = 10
MAX_CPU = 85
MAX_WAIT_LOOPS = 20

def cooldown():
    print("[AetherGuard] Cooling down...")
    time.sleep(COOLDOWN_SECONDS)

def wait_for_cpu():
    loops = 0
    while psutil.cpu_percent(interval=1) > MAX_CPU:
        print("[AetherGuard] High system load detected, waiting...")
        time.sleep(2)
        loops += 1
        if loops >= MAX_WAIT_LOOPS:
            print("[AetherGuard] Continuing despite load.")
            break