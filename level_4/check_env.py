from dotenv import load_dotenv
import os

load_dotenv()

secret_env_var = 'MY_SECRET_MESSAGE'
secret_message = os.environ.get(secret_env_var)

if secret_message != None:
    print(f"Success! The message is: {secret_message}")
else:
    print(f"Error: {secret_env_var} is not set.")