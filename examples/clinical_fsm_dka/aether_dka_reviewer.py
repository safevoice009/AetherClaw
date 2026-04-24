"""
🩺 AetherReviewer: Clinical Safety Node - DKA Protocol
Version: 1.0.0-MEDICAL-APEX
Logic: Deterministic Finite State Machine (FSM)

This node enforces strict adherence to medical guidelines. 
Specifically, it prevents the administration of Insulin in DKA if Potassium is < 3.3 mEq/L.
"""

import re
import os

class AetherClinicalSafetyException(Exception):
    """Custom exception for fatal clinical logic violations."""
    def __init__(self, message, protocol_step):
        super().__init__(message)
        self.protocol_step = protocol_step

class AetherDKAReviewer:
    def __init__(self):
        self.role = "AetherReviewer (Clinical Edition)"
        self.protocol_name = "DKA Treatment Protocol (ADA/ISPAD)"

    def log(self, message, status="INFO"):
        print(f"[{self.role}] [{status}] {message}")

    def parse_clinical_data(self, note_path):
        """Extracts critical labs from the ER note."""
        with open(note_path, 'r') as f:
            content = f.read()
        
        # Regex to find Potassium level
        k_match = re.search(r"Potassium \(K\+\):\s*([\d\.]+)", content)
        if k_match:
            return float(k_match.group(1))
        return None

    def validate_treatment_plan(self, draft_plan, potassium_level):
        """
        Deterministic Logic Gate:
        IF potassium < 3.3 AND plan includes 'Insulin' -> REJECT.
        """
        self.log(f"Auditing draft plan against {self.protocol_name}...")
        self.log(f"Detected Serum Potassium: {potassium_level} mEq/L")

        insulin_requested = "Insulin" in draft_plan or "insulin" in draft_plan
        
        if potassium_level is not None and potassium_level < 3.3:
            if insulin_requested:
                self.log("FATAL PROTOCOL VIOLATION DETECTED", "CRITICAL")
                error_msg = (
                    f"Fatal Error: Treatment plan includes Insulin while Potassium is {potassium_level} mEq/L. "
                    "Insulin administration in hypokalemic DKA patients triggers a shift of K+ into cells, "
                    "potentially causing fatal cardiac arrest. IV Potassium MUST be replaced first."
                )
                raise AetherClinicalSafetyException(error_msg, protocol_step="Electrolyte Stabilization")
        
        self.log("Clinical safety check passed. Artifact crystallized.", "SUCCESS")
        return "CRYSTALLIZED: " + draft_plan

if __name__ == "__main__":
    # Simulate the AetherClaw Loop
    reviewer = AetherDKAReviewer()
    # Support both absolute and relative paths for flexibility in deployment
    current_dir = os.path.dirname(os.path.abspath(__file__))
    note_path = os.path.join(current_dir, "data", "messy_er_note.txt")
    
    # 1. AetherDeveloper's hallucinated/flawed plan
    flawed_plan = "Start IV Fluids and start IV Insulin drip."
    
    print("--- 🌌 AetherClaw Clinical Safety Demo ---")
    print(f"Loading Clinical Note: {note_path}\n")
    
    # 2. Reviewer intercepts
    try:
        k_level = reviewer.parse_clinical_data(note_path)
        final_artifact = reviewer.validate_treatment_plan(flawed_plan, k_level)
        print(f"\n✅ Deployment Ready: {final_artifact}")
        
    except AetherClinicalSafetyException as e:
        print(f"\n❌ [FSM BLOCKER] {e}")
        print(f"🔄 Action: Loop back to AetherPlanner. Requirement: Add IV K+ replacement to protocol.")
