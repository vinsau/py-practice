from dotenv import load_dotenv
import os

load_dotenv()

github_token = os.environ.get('GITHUB_PAT') 

auth_header = {
        "Authorization": f"Bearer {github_token}"
}