import os
import sys
import argparse
import requests
import logging
from dotenv import load_dotenv
from .list_repos_ops import list_repos
from .create_repo_ops import create_repo

LOG_DIR = os.path.join(os.path.dirname(__file__), 'logs')
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, 'app.log')
# logging
logging.basicConfig(
    level = logging.DEBUG,
    format = "%(asctime)s - %(levelname)s - %(message)s",
    handlers = [
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler(sys.stdout)
    ]
)

log = logging.getLogger(__name__)

# declare argparser
parser = argparse.ArgumentParser(description="A simple program that manages github")
group = parser.add_mutually_exclusive_group(required=True)

# load environment variables
load_dotenv()

# header for api request

# helper for argument creation
def create_arg(long_flag, short_flag, help_msg, metavar_value):
    group.add_argument(
        long_flag,
        short_flag,
        type = str,
        metavar = metavar_value,
        help = help_msg,
    )
        
create_arg('--list-repos', '-l', 'Lists all available repositories', '<username>')
create_arg('--create-repo', '-c', 'Creates a private repository with the given name', '<repo-name>')

args = parser.parse_args()

def main():
    log.info("Starting application...")
    if args.list_repos:
        list_repos(args.list_repos)
    elif args.create_repo:
        create_repo(args.create_repo)
    log.info("Stopping application...")

if __name__ == '__main__':
    main()
