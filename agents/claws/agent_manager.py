"""
AetherClaw Agent Manager
Controls the initialization and retrieval of specialized 'Claws'.
"""

from agents.claws.orchestrator import planner, developer, reviewer

def get_agent(role):
    """
    Retrieves an AetherClaw agent by its role.
    Supported roles: 'planner', 'developer', 'reviewer'.
    """
    agents = {
        "planner": planner,
        "developer": developer,
        "reviewer": reviewer
    }
    return agents.get(role)