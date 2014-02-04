import unittest

from weather_client import WeatherClient

class WeatherClientTest(unittest.TestCase):
    def test_response(self):
        client = WeatherClient()
        self.assertEquals(client.get_weather(), "Nice, but a little cloudy.")
