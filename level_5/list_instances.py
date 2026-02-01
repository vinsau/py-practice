import sys
import boto3
import json
from botocore.exceptions import ClientError, NoCredentialsError

try:
    ec2_client = boto3.client('ec2')
    response = ec2_client.describe_instances()
    data = json.dumps(response, indent=4, default=str)
    print(data)
    # for reservation in response['Reservations']:
    #     for instance in reservation['Instances']:
    #         print(f'Keyname: {instance['KeyName']} ; InstanceID: {instance['InstanceId']} ; InstanceType: {instance['InstanceType']} ; State: {instance['State']['Name']}')
except NoCredentialsError:
    print("Error: `invalid aws credentials, setup with 'aws configure'")
    sys.exit(1)
except ClientError as e:
    print(e)
    sys.exit(1)
