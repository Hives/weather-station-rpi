from weather_data_getter import WeatherDataReader
import json
import requests


class WeatherDataSender:

    api_url = 'https://36a788a2.ngrok.io/api/data'

    def __init__(self, weather_data_reader=WeatherDataReader()):
        self.weather = weather_data_reader

    def pushData(self):
        data_string = json.dumps(self.weather.get())
        print("POST-ing data to %s" % (self.api_url))
        response = requests.post(self.api_url, data={'data': data_string})
        print(response)
