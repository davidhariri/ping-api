import datetime, os
from mongoengine import *

connect("ping", host=os.environ.get("MONGODB_URI"))

class Ping(Document):
	point = PointField(required=True)
	time = DateTimeField(required=True, default=datetime.datetime.now)
	alt = FloatField(required=True)
	speed = FloatField(required=True)
	comment = StringField(max_length=500, default="")

	def to_jdict(self):
		return {
			"id" : str(self.id),
			"time" : str(self.time),
			"point" : {
				"lat" : self.point["coordinates"][0],
				"lon" : self.point["coordinates"][1]
			},
			"comment" : self.comment,
			"alt" : self.alt,
			"speed" : self.speed
		}