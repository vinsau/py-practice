import sys
import subprocess
import argparse

# parse file argument
parser = argparse.ArgumentParser(description="Takes a file and get its size")
parser.add_argument('filename', help="Name of the file")
args = parser.parse_args()

# execute command
def execute_bash(cmd):
    try:
        result = subprocess.run(
            cmd,
            capture_output = True,
            text = True,
            check = True
        )
    except subprocess.CalledProcessError as e:
        print(f"Caught Error: {e}")
        sys.exit(1)
    return result

cmd = ['ls', '-l', args.filename]
bash_out = execute_bash(cmd)

if bash_out.returncode == 0:
    cmd_out = bash_out.stdout.split(' ')
    print(cmd_out[4])
