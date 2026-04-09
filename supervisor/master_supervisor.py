\"\"\"
AetherClaw Master Supervisor
The ultimate orchestration layer for large-scale autonomous project swarms.
\"\"\"

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

def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[AETHER-CORE] {timestamp} | {message}"
    print(line)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")


# ------------------------------------------------
# Scheduling Engine
# ------------------------------------------------

scheduler = TaskScheduler()


# ------------------------------------------------
# Utility: Directory Sanitization
# ------------------------------------------------

def goal_to_folder(goal):
    """Maps a strategic objective to a system-safe directory name."""
    return "_".join(goal.lower().split()[:3])


# ------------------------------------------------
# Core Deployment Loop (Swarm Management)
# ------------------------------------------------

def run_project(goal):
    """Executes a full lifecycle deployment for a specific swarm objective."""
    log(f"Initializing swarm deployment: {goal}")

    notify(f"Deployment Initiation: {goal}")
    speak(f"Initializing tactical deployment for objective {goal}")

    try:
        # Phase 1: Strategic Planning
        wait_for_cpu()
        log("Activating AetherPlanner module...")

        start = time.time()
        plan = planner(goal)
        log(f"Planning phase concluded in {round(time.time()-start,2)}s.")

        # Phase 2: Feasibility & Risk Assessment
        approved = evaluate_project(goal, plan)
        if not approved:
            log("Objective rejected: Potential safety or feasibility violation.")
            notify("Deployment Terminated: Safety rejection.")
            return

        # Phase 3: Synthesis
        cooldown()
        wait_for_cpu()
        log("Activating AetherDeveloper module...")

        start = time.time()
        code = developer(plan)
        log(f"Synthesis phase concluded in {round(time.time()-start,2)}s.")

        # Phase 4: Artifact Crystallization
        project_name = goal_to_folder(goal)
        path = create_project(project_name, code)
        log(f"Tactical artifact crystallized at: {path}")

        # Phase 5: Quality Assurance
        cooldown()
        wait_for_cpu()
        log("Activating AetherReviewer module...")

        start = time.time()
        review = reviewer(code)
        log(f"Validation phase concluded in {round(time.time()-start,2)}s.")

        notify(f"Tactical Success: {path}")
        speak("Strategic objective achieved.")

    except Exception as e:
        log(f"Framework Exception during deployment: {e}")
        raise


# ------------------------------------------------
# Main Orchestration Loop
# ------------------------------------------------

def main():
    """Master entry point for the AetherClaw autonomous swarm."""
    log("AetherMaster initialized. Swarm command active.")

    while True:
        try:
            # Idea generation via AetherBrain
            idea = generate_idea()
            log(f"New theoretical objective identified: {idea}")

            scheduler.add_task(idea)
            task = scheduler.next_task()

            if task:
                log(f"Executing scheduled priority task: {task['goal']}")
                try:
                    run_project(task["goal"])
                except Exception as e:
                    log(f"Priority Task Failure: {e}")
                    scheduler.retry_task(task)

        except Exception as e:
            log(f"Orchestration Sub-system Error: {e}")

        scheduler.wait_cycle()


# ------------------------------------------------

if __name__ == "__main__":
    main()