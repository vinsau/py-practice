from flask import Flask, request, jsonify
import logging
import sys
import redis
import os

redis_host = os.environ.get("REDIS_HOST", 'localhost')
redis_client = redis.Redis(host=redis_host, port=6379)

logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
log = logging.getLogger(__name__)

tasks = []

app = Flask(__name__)

@app.route('/todos')
def get_todos():
    log.info("Operation successful. Returning list of tasks")
    return jsonify(tasks)

@app.route('/todos', methods=['POST'])
def post_data():
    data = request.json
    tasks.append(data)
    log.info(f"Task added: {data}")
    return jsonify({'status': 'Task Added'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)