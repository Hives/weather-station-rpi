from freezegun import freeze_time
import pytest

from datetime import datetime

from weather_data_mock import WeatherDataMock

def test_class_instance():
  weather = WeatherDataMock()
  if isinstance(weather, WeatherDataMock):
    print('It is an instance')

def test_get_method_returns_temperature():
  weather = WeatherDataMock()
  data = weather.get()
  assert 'temperature' in data

def test_temperature_has_a_value():
  weather = WeatherDataMock()
  data = weather.get()
  temp = data["temperature"]
  assert type(temp["value"]) == float

@freeze_time("2019-05-14 14:44:37")
def test_temperature_has_the_date():
  weather = WeatherDataMock()
  data = weather.get()
  temperature = data["temperature"]
  assert temperature["date"] == datetime.now()