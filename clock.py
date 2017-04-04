from flask import Flask
from flask import request
app = Flask(__name__)

locations = [1,1,3]

@app.route('/')
def hello_world():
    return 'you have reached anya\'s clock'

@app.route('/get')
def get_location():
    return str(locations[0]) + str(locations[1]) + str(locations[2])

@app.route('/post', methods=['POST'])
def post():
	data = request.get_json()
	if data["user"] <= 2 and data["user"] >= 0:
		locations[data["user"]] = data["location"]
	return str(locations)