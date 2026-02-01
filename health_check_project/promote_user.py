import sys
import os
import json

json_path = 'users.json'

try:
    with open(json_path, 'r') as f:
        data = json.load(f)

        data[1]['role'] = 'admin'
    
    new_json_path = 'updated_users.json'
    
    with open(new_json_path, 'w') as f:
        json.dump(data, f, indent=4)
except FileNotFoundError as e:
    print(f"Caught Error: {e}")
    sys.exit(1)