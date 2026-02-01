from flask import Flask, request, jsonify
import logging
import sys

# 1. Set up logging (from Level 6)
# We want to see the server's activity
logging.basicConfig(level=logging.INFO, stream=sys.stdout)
log = logging.getLogger(__name__)

# 2. Initialize the Flask application
app = Flask(__name__)

# 3. Define a "route" for GET requests
# This is what a browser does
@app.route('/')
def get_hello():
    """This function runs when someone visits the main page."""
    log.info("GET /: 'hello' route was hit")
    return "Hello! This is a web server."

# 4. Define a "route" for POST requests (like your project)
# This is what an API or webhook does
@app.route('/webhook-receiver', methods=['POST'])
def post_data():
    """This function runs when a POST request is sent here."""
    
    # 'request.json' automatically parses the incoming JSON
    # data from the webhook (e.g., from GitHub)
    data = request.json
    
    log.info(f"POST /webhook-receiver: Received data: {data}")
    
    # ... This is where you would do your work ...
    # (e.g., git pull, run pytest, upload to S3)
    
    # Send a response back to the sender
    return jsonify({"status": "success", "message": "Data received"}), 200

# 5. Run the server
if __name__ == '__main__':
    log.info("Starting Flask server on port 5000...")
    # 'debug=True' reloads the server when you save the file
    app.run(host='0.0.0.0', port=5000, debug=True)