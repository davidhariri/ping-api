from flask import Flask
from flask_restful import Api

from routes.pings import Pings

from mongoengine import connect

# Connect to MongoDB
connect("ping")

app = Flask(__name__)
api = Api(app)

api.add_resource(Pings, "/")

if __name__ == "__main__":
    app.run(debug=True)