from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Message(Resource):
    def post(self):

        # get data from body
        data = request.get_data()

        # email message to me
        email_message(data)

        return {'status': 200}

api.add_resource(Message, '/')

def email_message(msg):
  print(msg)

if __name__ == '__main__':
    app.run(debug=True)