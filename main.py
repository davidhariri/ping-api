import os
from flask import Flask
from flask_restful import Api
from mongoengine import connect

from routes.pings import Pings

# Connect to MongoDB
connect("ping", host=os.environ.get("MONGODB_URI"))

app = Flask(__name__)
api = Api(app)

api.add_resource(Pings, "/")

if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG", False))