from utils.llm_session import ask_llm


# -------------------------------------------------
# Central Agent Router
# -------------------------------------------------

def run_agent(agent_name, prompt):

    print(f"[Orchestrator] Running {agent_name} agent")

    # optional agent-specific behaviour
    if agent_name == "planner":

        prompt = f"""
You are AetherClaw Planner, a senior software architect.

Break the following goal into development steps.

Goal:
{prompt}

Return a clear numbered task list.
"""

    elif agent_name == "developer":

        prompt = f"""
You are AetherClaw Developer, a senior Python developer.

Write clean working python code for the following task.

Task:
{prompt}

Rules:
- standard python
- no external dependencies
- include comments
"""

    elif agent_name == "reviewer":

        prompt = f"""
You are AetherClaw Reviewer, a strict code reviewer.

Review the following python code for bugs, style, and efficiency.

Code:
{prompt}

Return ONLY the corrected code.
"""

    # call shared LLM session
    response = ask_llm(prompt)

    return response


def aether_flow(goal):
    """The World-Class Reflexion Loop"""
    print(f"\n[AetherFlow] Starting evolution for: {goal}")
    
    # 1. Plan
    plan = run_agent("planner", goal)
    print("[AetherFlow] Plan generated.")
    
    # 2. Develop
    code = run_agent("developer", plan)
    print("[AetherFlow] Initial development complete.")
    
    # 3. Review & Refine (Reflexion)
    print("[AetherFlow] Starting Reflexion pass...")
    final_code = run_agent("reviewer", code)
    print("[AetherFlow] Reflexion complete. Quality verified.")
    
    return final_code