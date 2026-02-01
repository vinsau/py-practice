from flask import Flask, request, jsonify
import subprocess
import logging
import sys

def run_command(cmd):
    try:
        result = subprocess.run(
            cmd,
            capture_output = True,
            check = True,
            text = True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        log.exception(f"Error: something went wrong during the execution. {e}")
        return None

app = Flask(__name__)

@app.route('/system/uptime')
def get_uptime():
    uptime = run_command(['uptime'])
    log.info("Operation successful. Returning 'uptime' output")
    return jsonify({'uptime': uptime}), 200

@app.route('/system/disk')
def get_disk_status():
    disk = run_command(['df', '-h'])
    log.info("Operation successful. Returning 'disk' output")
    return jsonify({'disk-health': disk}), 200

if __name__ == '__main__':
    app.run(debug=True)