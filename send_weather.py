from weather_data_mock import *
import json
import requests

class SendWeatherData:

  def __init__(self, weather_data_mock = WeatherDataMock()):
    self.weather = weather_data_mock

  def pushData(self):
    data_string = json.dumps(self.weather.get())
    return requests.post('randomurl.com', data={'data': data_string})