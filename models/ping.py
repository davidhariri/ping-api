import datetime, os
from mongoengine import *

# Connect to MongoDB
connect("ping", host=os.environ.get("MONGODB_URI"))

class Ping(Document):
	lat = FloatField(required=True)
	lon = FloatField(required=True)
	time = DateTimeField(required=True, default=datetime.datetime.now)
	alt = FloatField(required=True)
	speed = FloatField(required=True)

	def to_jdict(self):
		return {
			"id" : str(self.id),
			"time" : str(self.time),
			"lat" : self.lat,
			"lon" : self.lon,
			"alt" : self.alt,
			"speed" : self.speed
		}