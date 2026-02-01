import sys
import argparse
import requests

parser = argparse.ArgumentParser(description="A simple api checker program")
parser.add_argument('username', help="The user's github username")

args = parser.parse_args()

response = requests.get(f"https://api.github.com/users/{args.username}", timeout=5)
try:
    response.raise_for_status()
    data = response.json()
    

    print(f"Name: {data['name']}")
    print(f"Bio: {data['bio']}")
except Exception as e:  
    print(f"Caught error: {e}")
    sys.exit(1)
