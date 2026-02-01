import sys
import argparse
import boto3
import json
from botocore.exceptions import ClientError, NoCredentialsError

parser = argparse.ArgumentParser(description="A simple program that uploads data to s3 bucket")
parser.add_argument(
    '--bucket',
    '-b',
    metavar = '<bucket_name>',
    type = str,
    required = True,
    help = "Adds the bucket name to process"
)

args = parser.parse_args()

try:
    s3_client = boto3.client('s3')
    response = s3_client.list_objects_v2(Bucket=args.bucket)
    contents = response['Contents']
    if contents:
        i = 1
        for item in contents:
            print(f"{i}. Filename: {item['Key']} ; Size: {item['Size']}")
            i += 1
except NoCredentialsError:
    print("Error: invalid aws credentials, try 'aws configure' to setup")
    sys.exit(1)
except ClientError as e:
    error_code = e.response['Error']['Code']
    if error_code == 'NoSuchBucket':
        print(f"Error {error_code}: invalid s3 bucket name")
    sys.exit(1)