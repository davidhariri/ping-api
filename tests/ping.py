import unittest, datetime
from models.ping import *

class TestPingModel(unittest.TestCase):
    def setUp(self):
        self.ping = Ping(
            lat=0.04,
            lon=24.34,
            alt=234,
            speed=24.2
        )
        self.ping.save()

    def test_jdict(self):
        """Tests that to_jdict method returns right values for BSON types"""
        self.assertTrue(isinstance(self.ping.to_jdict["id"], str))
        self.assertTrue(isinstance(self.ping.to_jdict["time"], str))

    def tearDown(self):
        self.ping.delete()

if __name__ == '__main__':
    unittest.main()