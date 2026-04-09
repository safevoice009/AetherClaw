from utils.llm_session import ask_llm


# -------------------------------------------------
# Central Agent Orchestration 
# -------------------------------------------------

def run_agent(agent_name, prompt):
    """Executes a specialized AetherClaw agent within the swarm."""
    log(f"Initializing Aether{agent_name.capitalize()} module...")

    # Modular agent prompt conditioning
    if agent_name == "planner":

        prompt = f"""
You are the AetherPlanner, a Principal Software Architect.
Your objective is to decompose high-level strategic goals into a granular, executable technical blueprint.

STRATEGIC GOAL:
{prompt}

REQUISITES:
1. Deconstruct the goal into distinct technological milestones.
2. Ensure technical feasibility and architectural robustness.
3. Return as a formal numbered implementation list.
"""

    elif agent_name == "developer":

        prompt = f"""
You are the AetherDeveloper, a Senior Full-Stack Engineer.
Your objective is to synthesize high-quality, efficient Python code based on the provided architectural blueprint.

ARCHITECTURAL BLUEPRINT:
{prompt}

CONSTRAINTS:
- Use idiomatic Python (PEP 8).
- Prioritize modularity and performance.
- Include comprehensive docstrings and internal commentary.
- MINIMIZE EXTERNAL DEPENDENCIES.
"""

    elif agent_name == "reviewer":

        prompt = f"""
You are the AetherReviewer, a Chief Technical Auditor.
Your objective is to perform a rigorous validation pass on the synthesized code, ensuring zero vulnerabilities, optimal complexity, and absolute functional correctness.

SOURCE CODE FOR AUDIT:
{prompt}

VALIDATION PARAMETERS:
- Logic Integrity
- Security Hardening
- Algorithmic Efficiency

OUTPUT:
Return the final, crystallized version of the code, incorporating all necessary hardening.
"""

    # call unified AetherCore communication layer
    response = ask_llm(prompt)

    return response


def aether_flow(goal):
    """The AetherFlow Evolutionary Synthesis Loop."""
    log(f"Engaging AetherFlow evolution for strategic objective: {goal}")
    
    # 1. Planning Layer
    plan = run_agent("planner", goal)
    log("AetherPlanner has established the strategic blueprint.")
    
    # 2. Synthesis Layer
    code = run_agent("developer", plan)
    log("AetherDeveloper has completed the initial synthesis pass.")
    
    # 3. Critical Validation Layer (Tactical Reflexion)
    log("Engaging AetherReviewer for tactical validation pass...")
    final_code = run_agent("reviewer", code)
    log("Evolutionary cycle complete. Artifact state: CRYSTALLIZED.")
    
    return final_code


def log(message):
    """Internal orchestration logger."""
    try:
        from datetime import datetime
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[AETHER-CORE] {timestamp} | {message}")
    except:
        print(f"[AETHER-CORE] {message}")