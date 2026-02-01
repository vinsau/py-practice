import subprocess
import sys

def execute_bash(cmd):
    result = subprocess.run(
        [cmd],
        capture_output = True,
        text = True,
        check = True
    )
    return result.stdout.strip()

try:
    username = execute_bash('whoami')
    hostname = execute_bash('hostname')

    print(f"Running as {username} on {hostname}")
except Exception as e:
    print(f"Caught Error: {e}")
    sys.exit(1)