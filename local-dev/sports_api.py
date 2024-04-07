from flask import Flask, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for your Flask app

# Load data from sports.json file
with open('../sports.json', 'r') as file:
    sports_data = json.load(file)

# Load data from sports_info.json file
with open('../sports_info.json', 'r') as file:
    sports_info_data = json.load(file)

# Define the route for the API endpoint to get sports data
@app.route('/api/sports', methods=['GET'])
def get_sports():
    return jsonify(sports_data)

# Define the route for the API endpoint to get sports info data
@app.route('/api/sports_info', methods=['GET'])
def get_sports_info():
    return jsonify(sports_info_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
