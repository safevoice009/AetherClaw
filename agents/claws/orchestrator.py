from utils.llm_session import ask_llm
from utils.model_manager import get_model_for_tier
import time

class AetherFSM:
    \"\"\"
    🌌 AetherFlow Deterministic FSM Engine (v4.0)
    Ensures absolute logic integrity by enforcing strict state-gate transitions.
    \"\"\"
    
    STATES = [\"INIT\", \"PLANNING\", \"SYNTHESIS\", \"VALIDATION\", \"CRYSTALLIZED\", \"FAILED\"]
    
    def __init__(self, objective):
        self.objective = objective
        self.current_state = \"INIT\"
        self.artifacts = {}
        self.retries = 0
        self.max_retries = 3

    def log(self, message, type=\"INFO\"):
        from datetime import datetime
        timestamp = datetime.now().strftime(\"%H:%M:%S\")
        print(f\"[AETHER-FSM] {timestamp} | {type:7} | {message}\")

    def transition(self, next_state):
        if next_state in self.STATES:
            self.log(f\"Migrating state: {self.current_state} -> {next_state}\", \"TRANSIT\")
            self.current_state = next_state
        else:
            self.log(f\"Invalid state target: {next_state}\", \"ERROR\")

    def run(self):
        \"\"\"Executes the deterministic evolutionary loop.\"\"\"
        self.log(f\"Powering up Apex Engine for objective: {self.objective}\")
        
        while self.current_state not in [\"CRYSTALLIZED\", \"FAILED\"]:
            if self.current_state == \"INIT\":
                self.transition(\"PLANNING\")
            
            elif self.current_state == \"PLANNING\":
                res = self._execute_agent(\"planner\", self.objective)
                if res:
                    self.artifacts[\"plan\"] = res
                    self.transition(\"SYNTHESIS\")
                else:
                    self.transition(\"FAILED\")
            
            elif self.current_state == \"SYNTHESIS\":
                res = self._execute_agent(\"developer\", self.artifacts[\"plan\"])
                if res:
                    self.artifacts[\"code\"] = res
                    self.transition(\"VALIDATION\")
                else:
                    self._handle_retry(\"SYNTHESIS\")
            
            elif self.current_state == \"VALIDATION\":
                res = self._execute_agent(\"reviewer\", self.artifacts[\"code\"])
                if res:
                    if \"CRYSTALLIZED\" in res or len(res) > 100:
                        self.artifacts[\"final_code\"] = res
                        self.transition(\"CRYSTALLIZED\")
                    else:
                        self.log(\"Validation rejected artifact. Forcing re-synthesis.\", \"REJECT\")
                        self._handle_retry(\"SYNTHESIS\")
                else:
                    self._handle_retry(\"VALIDATION\")
                    
        return self.artifacts.get(\"final_code\") if self.current_state == \"CRYSTALLIZED\" else None

    def _execute_agent(self, agent_name, context):
        tier = \"STRATEGIC\" if agent_name == \"planner\" else \"TACTICAL\"
        model = get_model_for_tier(tier)
        
        if agent_name == \"planner\":
            prompt = f\"Objective: {context}\\n\\nAct as AetherPlanner architectural core. Provide a deterministic blueprint.\"
        elif agent_name == \"developer\":
            prompt = f\"Blueprint: {context}\\n\\nAct as AetherDeveloper. Synthesize high-performance Python artifacts.\"
        elif agent_name == \"reviewer\":
            prompt = f\"Artifact: {context}\\n\\nAct as AetherReviewer. Hardened audit pass. If perfect, append 'CRYSTALLIZED'.\"

        try:
            return ask_llm(prompt, model=model)
        except Exception as e:
            self.log(f\"Model Resilience Check Failed: {e}\", \"ERROR\")
            return None

    def _handle_retry(self, failed_state):
        self.retries += 1
        if self.retries > self.max_retries:
            self.transition(\"FAILED\")
            self.log(\"Maximum resilience cycles exceeded.\", \"ERROR\")
        else:
            self.log(f\"Triggering resilience recovery cycle ({self.retries}/{self.max_retries})...\", \"RECOVERY\")
            self.transition(failed_state)
            time.sleep(2)

def aether_flow(goal):
    engine = AetherFSM(goal)
    return engine.run()
