import logging
import sys
import os
import subprocess
import shutil
from upload_to_s3_ops import upload_to_s3
from flask import Flask, request, jsonify
from pathlib import Path

target_dir = Path('../yaml_to_json_converter').resolve()
dir_venv_bin = target_dir / '.venv' / 'bin'
dir_python = dir_venv_bin / 'python'

def run_command(cmd):
    try:
        result = subprocess.run(
            cmd,
            cwd = target_dir,
            check = True,
        )
        return result
    except subprocess.CalledProcessError as e:
        log.exception(f"Error: something went wrong during the execution. {e}")
        return None

logging.basicConfig(
    level=logging.INFO,
    format = ("%(asctime)s - %(levelname)s - %(message)s"),
    handlers = [
        logging.FileHandler('app.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

log = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/hello')
def say_hello():
    return jsonify({ 'status' : 'success', 'message' : "hello there!"})

@app.route('/webhook', methods=['POST'])
def manage_github():
    data = request.json
    log.info(f"Author: {data['head_commit']['author']['name']}")
    log.info(f"Message: {data['head_commit']['message']}")

    pull = run_command(['git', 'pull'])
    if pull is None:
        log.error("git pull failed, aborting deployment")
        return jsonify({
            'status': 'failed',
            'message': 'git pull failed'
        }), 500
    log.info("Successfully pulled some changes")

    testing = run_command([dir_python, '-m', 'pytest'])
    if testing is None:
        log.error("pytest failed, aborting deployment")
        return jsonify({
            'status': 'failed',
            'message': 'pytest testing failed'
        }), 500

    log.info("Tests passed! Deploying to s3")

    try:
        deploy_dir = f"{target_dir}_backup"
        if os.path.exists(deploy_dir):
            shutil.rmtree(deploy_dir)
        shutil.copytree(target_dir, deploy_dir)
        archive_path = shutil.make_archive(
            base_name=deploy_dir,
            format='zip',
            root_dir=deploy_dir
        )
    except shutil.Error as e:
        log.exception(f"Caught error: {e}")
        return jsonify({
            'status': 'failed',
            'message': str(e)
        }), 500
    except Exception as e:
        log.exception(f"Caught Error: {e}")

        return jsonify({
            'status': 'failed',
            'message': str(e)
        }), 500
    
    upload_status = upload_to_s3(archive_path, 'aws-cloud-club-website')
    if not upload_status:
        log.error("S3 upload failed, aborting deployment")
        return jsonify({
            'status': 'failed',
            'message': "S3 upload failed"
        }), 500

    log.info("Successfully deployed to S3!")

    try:
        log.info(f"Cleaning up {deploy_dir} and {archive_path}")
        shutil.rmtree(deploy_dir)
        os.remove(archive_path)
    except Exception as e:
        log.exception(f"Cleanup failed: {e}")

    return jsonify({ 'status': 'success' })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)