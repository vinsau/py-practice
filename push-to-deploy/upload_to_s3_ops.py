import sys
import boto3
import os
import logging
from botocore.exceptions import NoCredentialsError, ClientError
from boto3.exceptions import S3UploadFailedError

log = logging.getLogger(__name__)

def upload_to_s3(dir_path, bucket_name):
    try:
        dir_name = os.path.basename(dir_path)
        s3_client = boto3.client('s3')
        s3_client.upload_file(dir_path, bucket_name, dir_name)
        log.info(f"Successfully uploaded '{dir_name}' to '{bucket_name}'.")
        return True
    except NoCredentialsError:
        log.error("Caught Error: invalid aws credentials, try 'aws configure' to setup")
        return False
    except ClientError as e:
        error_code = e.response['Error']['Code']

        if error_code == 'NoSuchBucket':
            log.error(f"Caught Error: the bucket '{bucket_name}' is invalid or doesn't exist")
        elif error_code == 'AccessDenied':
            log.error(f"Caught Error: access denied. Check your permissions.")
        else:
            log.error(f"AWS Client Error: {error_code} - {e}")
        return False
    except S3UploadFailedError as e:
        log.error(f"Upload failed: {e}")
        return False
    except Exception as e:import sys
import boto3
import os
import logging
from botocore.exceptions import NoCredentialsError, ClientError
from boto3.exceptions import S3UploadFailedError

log = logging.getLogger(__name__)

def upload_to_s3(dir_path, bucket_name):
    try:
        dir_name = os.path.basename(dir_path)
        s3_client = boto3.client('s3')
        s3_client.upload_file(dir_path, bucket_name, dir_name)
        log.info(f"Successfully uploaded '{dir_name}' to '{bucket_name}'.")
        return True
    except NoCredentialsError:
        log.error("Caught Error: invalid aws credentials, try 'aws configure' to setup")
        return False
    except ClientError as e:
        error_code = e.response['Error']['Code']

        if error_code == 'NoSuchBucket':
            log.error(f"Caught Error: the bucket '{bucket_name}' is invalid or doesn't exist")
        elif error_code == 'AccessDenied':
            log.error(f"Caught Error: access denied. Check your permissions.")
        else:
            log.error(f"AWS Client Error: {error_code} - {e}")
        return False
    except S3UploadFailedError as e:
        log.error(f"Upload failed: {e}")
        return False
    except Exception as e:
        log.error("Caught error: {e}")
        return False

        log.error(f"Caught error: {e}")
        return False
