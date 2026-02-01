# api_client.py
import requests

def get_user_name(user_id):
    """Fetches a user's name from a (fake) public API."""
    try:
        response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
        response.raise_for_status() # Raise an error for bad responses (4xx, 5xx)
        
        # We got a good response, return the user's name
        return response.json()['name']
        
    except requests.exceptions.HTTPError as e:
        # The API returned a 404 or 500
        return f"API Error: {e}"
    except Exception:
        # Any other error (e.g., no network)
        return "Generic Error"