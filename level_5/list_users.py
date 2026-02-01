from botocore.exceptions import ClientError, NoCredentialsError
import boto3
import sys

try:
    iam_client = boto3.client('iam')
    response = iam_client.list_users()

    for user in response['Users']:
        print(f'- {user['UserName']}')
except NoCredentialsError:
    print(f"Caught Error: invalid aws credentials, try 'aws configure'")
    sys.exit(1)
except ClientError as e:
    print(e) 
    # I found out that 'e' already prints a nicely informative error message so I'll just use it instead of a creating custom one
    sys.exit(1)

