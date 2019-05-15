from freezegun import freeze_time
import pytest

from datetime import datetime

from weather_data_mock import WeatherDataMock

def test_class_instance():
  weather = WeatherDataMock()
  if isinstance(weather, WeatherDataMock):
    print('It is an instance')

def test_get_method_returns_dict_including_temperature():
  weather = WeatherDataMock()
  data = weather.get()
  assert type(data['temperature']) == float

def test_get_method_returns_dict_including_pressure():
  weather = WeatherDataMock()
  data = weather.get()
  assert type(data['pressure']) == float

def test_get_method_returns_dict_including_humidity():
  weather = WeatherDataMock()
  data = weather.get()
  assert type(data['humidity']) == float

@freeze_time("2019-05-14 14:44:37")
def test_temperature_has_the_date():
  weather = WeatherDataMock()
  data = weather.get()
  assert data["date"] == datetime.now()