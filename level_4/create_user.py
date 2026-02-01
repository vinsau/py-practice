import sys
import requests
import os

api_key = os.environ.get('API_KEY')
dummy_token = os.environ.get('DUMMY_TOKEN')

new_user_payload = {
    "name": "Gauciv", 
    "job": "DevOps Engineer"
}

auth_headers = {
    "Authorization": f"Bearer {dummy_token}"
}

try:
    response = requests.post(
        'http://localhost:8000/users',
        json = new_user_payload,
        headers = auth_headers
    )
    
    response.raise_for_status()

    if response.status_code == 201:
        data = response.json()
        print(data)
except requests.exceptions.HTTPError as e:
    print(f"Caught Error: {e}")
    sys.exit(1)
