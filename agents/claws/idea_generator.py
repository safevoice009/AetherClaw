import random

from agents.claws.agent_manager import planner

# fallback ideas if LLM fails

IDEAS = [
    "simple password manager",
    "file organizer tool",
    "markdown note taking app",
    "cli weather checker",
    "url metadata scraper",
    "todo list with sqlite",
    "terminal based calculator",
    "log file analyzer",
]


def generate_static_idea():
    return random.choice(IDEAS)


def generate_llm_idea():

    prompt = """
Generate ONE small Python project idea.
Requirements:
- useful CLI or small tool
- beginner to intermediate complexity
- avoid repeats
Return only the idea.
"""

    try:

        idea = planner(prompt)

        if isinstance(idea, str) and len(idea.strip()) > 5:
            return idea.strip()

    except Exception:
        pass

    return None


def generate_idea():

    idea = generate_llm_idea()

    if idea:
        return idea

    return generate_static_idea()