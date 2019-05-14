import pytest
import unittest

from datetime import datetime

from weather_data_mock import *

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

@pytest.mark.freeze_time
def test_temperature_has_the_date():
  weather = WeatherDataMock()
  data = weather.get()
  temp = data["temperature"]
  assert temp["date"] == datetime.now()