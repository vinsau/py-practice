import logging
import sys
import requests
from .config import auth_header

log = logging.getLogger(__name__)

def create_repo(repo_name):
    url = 'https://api.github.com/user/repos'

    payload = {
        "name": repo_name,
        "description": "A new repo created by my Python script",
        "private": True
    }

    try:
        response = requests.post(
            url,
            json = payload,
            headers = auth_header
        )

        response.raise_for_status()

        if response.status_code == 201:
            data = response.json()
            log.info(f"Success! Created new private repo at: {data['html_url']}")
        return data
    except requests.exceptions.HTTPError as e:
        log.exception(f"Caught Error: {e}")
        return None