import logging
import boto3
import os
import sys
from botocore.exceptions import ClientError, NoCredentialsError

log = logging.getLogger(__name__)

# handle ec2
def find_and_tag_instances(tag_key, tag_value):
    try:
        ec2_client = boto3.client('ec2')
        response = ec2_client.describe_instances()
        untagged_instances = []
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                get_id = instance['InstanceId']
                found_key = False
                for tag in instance['Tags']:
                    if tag_key == tag['Key']:
                        found_key = True
                        break

                if not found_key:
                    untagged_instances.append(get_id)
                    

        if untagged_instances:
            ec2_client.create_tags(Resources=untagged_instances, Tags=[{
                'Key': tag_key,
                'Value': tag_value
            }])
            log.info(f"Successfully tagged {len(untagged_instances)} instance(s) with '{tag_key}={tag_value}':")
            log.info(f"Instances: {untagged_instances}")
        else:
            log.info("Message: no instance(s) needs to be tagged")
    except NoCredentialsError:
        log.error("Caught Error: invalid aws credentials, try 'aws configure' to setup")
        sys.exit(1)
    except ClientError as e:
        # error_code = e.response['Error']['Code']

        # if error_code == 'NoSuchBucket':
        #     print(f"Caught Error: the bucket '{bucket_name}' is invalid or doesn't exist")
        log.error(e)
        sys.exit(1)