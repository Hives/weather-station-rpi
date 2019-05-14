from weather_data_mock import *

class SendWeatherData:

  def __init__(self, weather_data_mock = WeatherDataMock()):
    self.weather = weather_data_mock

  def pushData(self):
    return self.weather.get()
    # make an http puts request to the server