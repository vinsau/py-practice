import logging
import boto3
import os
import sys
from pathlib import Path
from botocore.exceptions import ClientError, NoCredentialsError
from boto3.exceptions import S3UploadFailedError
log = logging.getLogger(__name__)

def upload_to_s3(file_path, bucket_name):
    try:
        file = Path(file_path)
        if not file.exists():
            raise FileNotFoundError(f"the file '{file}' is invalid or nowhere to be found")
    except FileNotFoundError as e:
        log.error(f"Caught Error: {e}")
        sys.exit(1)
    
    try:
        s3_client = boto3.client('s3')
        file_name = os.path.basename(file)
        s3_client.upload_file(file, bucket_name, file_name)
        log.info(f"Successfully uploaded '{file_name}' to '{bucket_name}'.")
    except NoCredentialsError:
        log.error("Caught Error: invalid aws credentials, try 'aws configure' to setup")
        sys.exit(1)
    except ClientError as e:
        error_code = e.response['Error']['Code']

        if error_code == 'NoSuchBucket':
            log.error(f"Caught Error: the bucket '{bucket_name}' is invalid or doesn't exist")
        elif error_code == 'AccessDenied':
            log.error(f"Caught Error: access denied. Check your permissions.")
        else:
            log.error(f"AWS Client Error: {error_code} - {e}")
        sys.exit(1)
    except S3UploadFailedError as e:
        log.error(f"Upload failed: {e}")
        sys.exit(1)
    except Exception as e:
        log.error("Caught error: {e}")
        sys.exit(1)