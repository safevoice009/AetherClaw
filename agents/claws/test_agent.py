import subprocess
import sys


def run_tests(script_path):

    print("\n[Test Agent] Running tests")

    try:

        result = subprocess.run(
            [sys.executable, script_path],
            capture_output=True,
            text=True,
            timeout=10
        )

        if result.returncode == 0:
            print("[Test Agent] Code executed successfully")

        else:
            print("[Test Agent] Code failed")

        print(result.stdout)

    except Exception as e:
        print("[Test Agent] Error:", e)