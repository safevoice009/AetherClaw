from utils.llm_session import ask_llm

def review_code(code):
    """
    World-class Code Reviewer Agent.
    Audits for security vulnerabilities, performance bottlenecks, and PEP8 compliance.
    """
    print("[AetherClaw] CodeReviewer is auditing the generated solution...")
    
    prompt = f"""
You are the AetherClaw Security & Performance Auditor.

Review the following Python code.
1. Identify security risks (e.g., shell=True, insecure imports).
2. Suggest performance optimizations.
3. Ensure the code is clean, documented, and professional.

Code:
{code}

If the code is already perfect, return the original code.
Otherwise, return the improved version ONLY.
"""
    
    return ask_llm(prompt, temperature=0.1)

if __name__ == "__main__":
    sample_code = "import os\nos.system('ls')"
    print(review_code(sample_code))
