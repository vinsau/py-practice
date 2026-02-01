import sys
import os

home_dir = os.environ.get("HOME")
ssh_path = os.path.join(home_dir, '.ssh', 'id_rsa')

if os.path.exists(ssh_path):
    print(f"SSH key found at: {ssh_path}")
else:
    print(f"SSH key not found at: {ssh_path}")

