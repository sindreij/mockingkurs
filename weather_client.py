import json

import requests

class WeatherClient(object):
    def get_weather(self):
        response = requests.get('http://www.mocky.io/v2/52f10541bf227bca03d8a14b')
        content = response.content
        data = json.loads(content)
        return data['weather']


if __name__ == '__main__':
    client = WeatherClient()
    print "The weather is:", client.get_weather()
