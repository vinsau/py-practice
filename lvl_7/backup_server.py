import boto3
import logging
import sys
import datetime
import os
from flask import Flask, request, jsonify
from botocore.exceptions import ClientError, NoCredentialsError

logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
log = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/create-backup', methods=['POST'])
def create_backup():
    now = datetime.datetime.now()
    time_now = now.strftime("%Y-%m-%d %H:%M:%S")
    data = request.json
    file = os.path.basename(data['filename'])

    with open(file, 'w') as f:
        f.write(time_now)

    try:
        s3_client = boto3.client('s3')
        bucket = data['bucket']
        s3_client.upload_file(file, bucket, file)
        return jsonify({'status': "backup complete", 'key': file}), 201
    except ClientError as e:
        error_code = e.response['Error']['Code']

        if error_code == 'NoSuchBucket':
            log.error(f"Caught Error: the bucket '{bucket_name}' is invalid or doesn't exist")
        elif error_code == 'AccessDenied':
            log.error(f"Caught Error: access denied. Check your permissions.")
        else:
            log.error(f"AWS Client Error: {error_code} - {e}")
        return None
    except S3UploadFailedError as e:
        log.error(f"Upload failed: {e}")
        return None
    except Exception as e:
        log.error("Caught error: {e}")
        return None 

if __name__ == '__main__':
    app.run(debug=True)
