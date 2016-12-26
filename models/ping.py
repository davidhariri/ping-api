import datetime, os
from mongoengine import *

# Connect to MongoDB
connect("ping", host=os.environ.get("MONGODB_URI"))

class Ping(Document):
	point = PointField(required=True)
	time = DateTimeField(required=True, default=datetime.datetime.now)
	alt = FloatField(required=True)
	speed = FloatField(required=True)

	def to_jdict(self):
		return {
			"id" : str(self.id),
			"time" : str(self.time),
			"point" : self.point,
			"alt" : self.alt,
			"speed" : self.speed
		}