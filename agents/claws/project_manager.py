from agents.claws.agent_manager import planner

def evaluate_project(goal, plan):

    prompt = f"""
You are a project manager agent.

Goal:
{goal}

Plan:
{plan}

Decide:
1. Is the project feasible as a small Python tool?
2. Should the system proceed with development?

Return one word:
APPROVE or REJECT
"""

    decision = planner(prompt)

    return "APPROVE" in decision.upper()