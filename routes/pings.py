from flask_restful import Resource
from models.ping import Ping
from mongoengine import *

class Pings(Resource):
	def post(self):
		try:
			new_ping = Ping(
				lon=0.4,
				time="2016"
			)
			new_ping.save()

			return new_ping.to_jdict(), 201

		except ValidationError as e:
			return {"error": str(e)}, 400