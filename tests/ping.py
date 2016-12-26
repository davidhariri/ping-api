import unittest, datetime
from models.ping import *

class TestPingModel(unittest.TestCase):
    def setUp(self):
        self.ping = Ping(
            point=[51.5033640, -0.1276250],
            alt=234,
            speed=24.2
        )
        self.ping.save()

    def test_jdict(self):
        """Tests that to_jdict method returns right values for BSON types"""
        # Find the newly made ping
        new_ping = Ping.objects.order_by("-_id")[0]
        jdict = new_ping.to_jdict()
        
        self.assertTrue(isinstance(jdict["id"], str))
        self.assertTrue(isinstance(jdict["time"], str))
        self.assertTrue(isinstance(jdict["point"], dict))

    def tearDown(self):
        self.ping.delete()

if __name__ == '__main__':
    unittest.main()