from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/get_website_headers', methods=['POST'])
def get_website_headers():
    # Receive JSON data from the client
    request_data = request.json
    
    # Extract the website URL from the received data
    website_url = request_data.get('website_url', '')

    # Perform any logic here based on the website_url
    # For simplicity, just returning the headers for demonstration
    headers = {'Content-Type': 'text/html'}  # Replace with actual logic

    # Respond with the headers in JSON format
    return jsonify(headers)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
