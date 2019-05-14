from weather_data_mock import *

class SendWeatherData:

  def __init__(self):
    self.weather = WeatherDataMock()

  def pushData(self):
    return self.weather.get()