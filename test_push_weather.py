import pytest
import unittest

from send_weather import *

def test_class():
  send = SendWeatherData()
  if isinstance(send, SendWeatherData):
    print("obj is an instance")

def test_pushdata():
  class WeatherDataMockMock:
    def get(self):
      return "anything"

  mock = WeatherDataMockMock()
  send = SendWeatherData(mock)
  data = send.pushData()
  assert data is "anything"