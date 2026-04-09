\"\"\"
🌌 AetherLite Headless Supervisor (v3.0)
Ultra-low overhead orchestration for Mobile, Termux, and Remote Terminal deployment.
\"\"\"

import sys
import os
import time
from datetime import datetime
from tqdm import tqdm

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agents.claws.agent_manager import planner, developer, reviewer
from agents.claws.project_builder import create_project
from utils.hardware_detect import get_environment_info

def lite_log(message, type="INFO"):
    timestamp = datetime.now().strftime("%H:%M:%S")
    color = "\033[94m" # Blue
    if type == "SUCCESS": color = "\033[92m" # Green
    elif type == "WARN": color = "\033[93m" # Yellow
    elif type == "ERROR": color = "\033[91m" # Red
    
    reset = "\033[0m"
    print(f"{color}[{timestamp}] {type:7} | {message}{reset}")

def run_objective(objective):
    info = get_environment_info()
    lite_log(f"Initializing AetherLite on {info['os']} ({'Termux' if info['is_termux'] else 'Headless'})")
    
    phases = [
        ("Planning", planner),
        ("Synthesis", developer),
        ("Validation", reviewer)
    ]
    
    results = {}
    
    with tqdm(total=len(phases), desc="[AetherFlow]", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}]") as pbar:
        for phase_name, agent_func in phases:
            lite_log(f"Activating {phase_name} Unit...")
            start_time = time.time()
            
            try:
                if phase_name == "Planning":
                    results["plan"] = agent_func(objective)
                elif phase_name == "Synthesis":
                    results["code"] = agent_func(results["plan"])
                elif phase_name == "Validation":
                    results["review"] = agent_func(results["code"])
                
                duration = round(time.time() - start_time, 2)
                lite_log(f"{phase_name} completed in {duration}s", "SUCCESS")
                pbar.update(1)
            except Exception as e:
                lite_log(f"Critical failure in {phase_name}: {e}", "ERROR")
                return

    # Crystallization
    lite_log("Crystallizing tactical artifacts...")
    folder_name = "_".join(objective.lower().split()[:3])
    path = create_project(folder_name, results.get("code", ""))
    
    lite_log(f"Objective Achieved: {path}", "SUCCESS")
    print("\n" + "="*50)
    print(f"Deployment Point: {path}")
    print("="*50 + "\n")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="AetherLite: Headless Autonomous Deployment")
    parser.add_argument("objective", type=str, help="The strategic goal for the agent swarm.")
    args = parser.parse_args()
    
    if not args.objective:
        print("Please provide a strategic objective.")
        sys.exit(1)
        
    try:
        run_objective(args.objective)
    except KeyboardInterrupt:
        lite_log("Emergency Abort initiated by user.", "WARN")
