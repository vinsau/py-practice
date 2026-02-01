import logging
import sys
import requests
from .config import auth_header

log = logging.getLogger(__name__)

def list_repos(username):
    url = f'https://api.github.com/users/{username}/repos'

    try:
        response = requests.get(url, headers=auth_header, timeout=5)
        response.raise_for_status()
        data = response.json()

        if not len(data) < 1:
            log.info(f"Listing repos for {username}:")
            for repo in data:
                log.info(f"- {repo['name']}")
        else:
            log.error(f"User '{username}' currently has 0 public repositories")
        return data
    except requests.exceptions.HTTPError as e:
        log.exception(f"Caught Error: {e}")
        return None