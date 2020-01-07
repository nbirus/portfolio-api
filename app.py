from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
api = Api(app)
CORS(app)

class Message(Resource):
    def get(self):
        return {'status': 200}
    def post(self):

        # get data from body
        data = request.get_json(force=True)

        # email message to me
        email_message(data)

        return {'status': 200}

api.add_resource(Message, '/')

def email_message(msg):
  message = 'Name: ' + msg['name'] + '; Email: ' + msg['email']  + '; Message: ' + msg['message'] 
  data = '{"text":"' + message + '"}'
  headers = {'Content-type': 'application/json'}
  response = requests.post(os.getenv('SLACK'), headers=headers, data=data)

if __name__ == '__main__':
    app.run(debug=True)