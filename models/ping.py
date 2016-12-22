from mongoengine import *
import datetime

class Ping(Document):
	lat = FloatField(required=True)
	lon = FloatField(required=True)
	time = DateTimeField(required=True, default=datetime.datetime.now)
	alt = FloatField()
	speed = FloatField()

	def to_jdict(self):
		return {
			"id" : str(self.id),
			"lat" : self.lat,
			"lon" : self.lon,
			"time" : str(self.time),
			"speed" : self.speed
		}