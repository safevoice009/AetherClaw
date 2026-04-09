"""
AetherClaw Core Supervisor
The primary CLI interface for executing single autonomous objectives.
"""

import sys
import os
import threading
import itertools
import time
import psutil
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agents.claws.agent_manager import planner, developer, reviewer
from agents.claws.project_builder import create_project

LOG_FILE = "aether_core.log"

def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[AETHER-CORE] {timestamp} | {message}"
    print(line)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")


# -------------------------------------------------
# Spinner (visual progress)
# -------------------------------------------------

spinner_running = False


def spinner():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if not spinner_running:
            break
        sys.stdout.write('\rRunning ' + c)
        sys.stdout.flush()
        time.sleep(0.1)


# -------------------------------------------------
# Utility: Map goal to project directory name
# -------------------------------------------------

def goal_to_folder(goal):
    """Generates a sanitized directory string from a high-level goal."""
    return "_".join(goal.lower().split()[:3])


# -------------------------------------------------
# Resource Management: CPU safety guard
# -------------------------------------------------

def wait_for_cpu():
    """Pauses execution if system load exceeds safe operational thresholds."""
    while psutil.cpu_percent(interval=1) > 85:
        log("System load high... deferring execution.")
        time.sleep(2)


# -------------------------------------------------
# Orchestration: Agent runner with retry logic
# -------------------------------------------------

def run_agent(agent_function, input_data, name, retries=3):
    """Executes an agent skill with progress visualization and fault tolerance."""
    for attempt in range(retries):
        try:
            wait_for_cpu()

            global spinner_running
            spinner_running = True

            t = threading.Thread(target=spinner)
            t.start()

            result = agent_function(input_data)

            spinner_running = False
            t.join()

            log(f"Sub-process [{name}] reached terminal state.")
            return result

        except Exception as e:
            spinner_running = False
            log(f"Process [{name}] encountered an exception (Attempt {attempt + 1}).")
            log(f"Diagnostic: {str(e)}")

            if attempt < retries - 1:
                log("Initiating retry protocol...")
                time.sleep(5)

    raise RuntimeError(f"Framework failure: {name} failed to complete after {retries} attempts.")


# -------------------------------------------------
# Deployment Lifecycle
# -------------------------------------------------

print("\n" + "="*50)
print("   AETHERCLAW CORE | AUTONOMOUS SWARM SUPPRESSOR")
print("="*50 + "\n")

goal = input("Define strategic objective: ")

log("Objective acquired. Initializing AetherFlow...")
log(f"Strategic Target: {goal}")

# Phase 1: Planning
log("Initializing AetherPlanner agent...")
plan = run_agent(planner, goal, "Planner")

log("Strategic blueprint established.")
print("\n--- BLUEPRINT ---\n")
print(plan)

# Phase 2: Synthesis
log("Initializing AetherDeveloper agent...")
code = run_agent(developer, plan, "Developer")

project_name = goal_to_folder(goal)
file_path = create_project(project_name, code)

log(f"Artifact synthesized at: {file_path}")
print(f"\nDEEPLOYMENT PATH: {file_path}")

# Phase 3: Validation
log("Initializing AetherReviewer agent...")
review = run_agent(reviewer, code, "Reviewer")

log("Quality validation terminal reached.")
print("\n--- VALIDATION REPORT ---\n")
print(review)

log("Deployment cycle successfully concluded.")