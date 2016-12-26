from flask_restful import Resource, reqparse
from models.ping import Ping
from mongoengine import *
import datetime

class Pings(Resource):
	def post(self):
		parser = reqparse.RequestParser()
		req_floats = ["speed", "alt"]

		for f in req_floats:
			parser.add_argument(
				f,
				type=float,
				help="'{}' should be parsable to float".format(f),
				required=True
			)

		parser.add_argument(
			"point",
			type=float,
			help="'point' should be a lat, lon list of floats",
			action="append",
			required=True
		)

		args = parser.parse_args()

		new_ping = Ping(**args)
		new_ping.save()

		return {"id" : str(new_ping.id)}, 201

	def get(self):
		parser = reqparse.RequestParser()
		parser.add_argument(
		    "size",
		    type=int,
		    help="'size' should be an integer greater than 0",
		    location="args"
		)

		args = parser.parse_args()

		size = args["size"] or 10
		size = min(size, 100)

		pings = Ping.objects.order_by("-_id")[:size]

		return list(map(lambda p: p.to_jdict(), pings))