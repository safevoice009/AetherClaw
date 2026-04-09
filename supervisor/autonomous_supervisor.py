import time
import os
import psutil
from datetime import datetime

from agents.claws.idea_generator import generate_idea
from agents.claws.agent_manager import planner, developer, reviewer
from agents.claws.project_builder import create_project


# ------------------------------------------------
# Logging setup (same file used by supervisor)
# ------------------------------------------------

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LOG_DIR = os.path.join(BASE_DIR, "logs")
LOG_FILE = os.path.join(LOG_DIR, "system.log")

os.makedirs(LOG_DIR, exist_ok=True)


def log(message):

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    line = f"[{timestamp}] {message}"

    print(line)

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")


# ------------------------------------------------
# Resource Orchestration: System Load Monitoring
# ------------------------------------------------

def wait_for_cpu():
    """Pauses autonomous operations if system utilization exceeds safe operational limits."""
    for _ in range(10):
        if psutil.cpu_percent(interval=1) < 85:
            return
        log("System load critical. Deferring autonomous processing...")
        time.sleep(2)


# ------------------------------------------------
# Telemetry: Performance Metrics
# ------------------------------------------------

stats = {
    "projects_built": 0,
    "failed_tasks": 0,
    "start_time": time.time()
}


# ------------------------------------------------
# Utility: Directory Sanitization
# ------------------------------------------------

def goal_to_folder(goal):
    """Generates a system-safe directory identifier from a high-level objective."""
    return "_".join(goal.lower().split()[:3])


# ------------------------------------------------
# Operational Tier: Individual Artifact Synthesis
# ------------------------------------------------

def run_task(goal):
    """Executes the standard AetherFlow loop for a single strategic objective."""
    log(f"Initializing autonomous synthesis flow: {goal}")

    try:
        wait_for_cpu()

        # Phase 1: Planning
        log("Activating AetherPlanner module...")
        start = time.time()
        plan = planner(goal)
        log(f"Strategic blueprint generated in {round(time.time()-start,2)}s.")

        # Phase 2: Synthesis
        log("Activating AetherDeveloper module...")
        start = time.time()
        code = developer(plan)
        log(f"Code synthesis completed in {round(time.time()-start,2)}s.")

        # Phase 3: Deployment
        project_name = goal_to_folder(goal)
        path = create_project(project_name, code)
        log(f"Artifact deployed at tactical address: {path}")

        # Phase 4: Quality Validation
        log("Activating AetherReviewer module...")
        start = time.time()
        review = reviewer(code)
        log(f"Review cycle completed in {round(time.time()-start,2)}s.")

        stats["projects_built"] += 1

    except Exception as e:
        log(f"Framework Exception during synthesis: {e}")
        stats["failed_tasks"] += 1


# ------------------------------------------------
# Analytics: System Resonance Reporting
# ------------------------------------------------

def show_stats():
    """Outputs high-level telemetry regarding the autonomous swarm's performance."""
    runtime = int(time.time() - stats["start_time"])
    print("\n" + "-"*30)
    print("   AETHERCLAW RESONANCE STATUS")
    print("-"*30)
    print(f"Artifacts Synthesized : {stats['projects_built']}")
    print(f"Deployment Exceptions  : {stats['failed_tasks']}")
    print(f"Uptime Duration (sec)  : {runtime}")
    print("-"*30 + "\n")


# ------------------------------------------------
# Mode: Continuous Neural Stream
# ------------------------------------------------

def continuous_mode():
    """Engages the framework in an indefinite loop of autonomous idea generation and synthesis."""
    log("Continuous Neural Stream mode engaged.")
    print("Press CTRL+C to terminate system resonance...\n")

    try:
        while True:
            idea = generate_idea()
            log(f"AetherBrain identified new potential objective: {idea}")
            run_task(idea)
            time.sleep(5)
    except KeyboardInterrupt:
        log("Neural stream deactivated by manual override.")


# ------------------------------------------------
# Strategic Control Desk (Interactive Menu)
# ------------------------------------------------

def main():
    """Primary interactive interface for supervising the AetherClaw ecosystem."""
    while True:
        print("\n" + "="*50)
        print("   AETHERCLAW | STRATEGIC SUPERVISOR (PRO)")
        print("="*50)
        print("1 🎯 Initiate Synthesis from Manual Objective")
        print("2 🧠 Generate & Synthesize AetherBrain Concept")
        print("3 🚀 Execute Batch Deployment Cycle")
        print("4 🔄 Engage Continuous Neural Stream (Autonomous)")
        print("5 📊 View System Telemetry & Resonance")
        print("0 🛑 Emergency System Shutdown")

        choice = input("\nSelect strategic operational tier: ")

        if choice == "1":
            goal = input("\nEnter strategic goal: ")
            run_task(goal)

        elif choice == "2":
            idea = generate_idea()
            print("\nAetherBrain Concept:", idea)
            run_task(idea)

        elif choice == "3":
            try:
                count = int(input("\nEnter batch cycle depth: "))
                for i in range(count):
                    print(f"\n[AetherFlow] Processing cycle {i+1} of {count}...")
                    idea = generate_idea()
                    run_task(idea)
            except ValueError:
                print("Invalid operational depth.")

        elif choice == "4":
            continuous_mode()

        elif choice == "5":
            show_stats()

        elif choice == "0":
            log("Executing graceful system depowered and shutdown...")
            break

        else:
            print("Invalid operational parameters. Select a valid tier.")


# ------------------------------------------------

if __name__ == "__main__":
    main()
 "__main__":
    main()