from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Message(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(Message, '/post')

if __name__ == '__main__':
    app.run(debug=True)