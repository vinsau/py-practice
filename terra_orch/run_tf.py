import subprocess
import sys
import argparse

parser = argparse.ArgumentParser(description="A simple program to run terraform")
parser.add_argument(
    '--destroy',
    '-d',
    action = 'store_true',
    help = 'Destroy all terraform resources'
)

args = parser.parse_args()

def run_command(cmd):
    return subprocess.run(
        cmd,
        check = True,
        capture_output = True
    )

try:
    if args.destroy:
        print('Destroying all resources...')
        run_command(['terraform', 'destroy', '-auto-approve'])
        print('Successfully DESTROYED all resources...✅')
    else:
        print("Initializing terraform...")
        run_command(['terraform', 'init'])
        print("Successfully INITIALIZED terraform... ✅")
    
        print("Applying configurations...")
        run_command(['terraform', 'apply', '-auto-approve'])
        print('Successfully APPLIED the configurations... ✅')
except subprocess.CalledProcessError as e:
    print(f"Caught Error: {e}")
    sys.exit(1)

