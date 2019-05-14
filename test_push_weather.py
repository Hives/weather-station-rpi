import pytest
import requests
import requests_mock

from send_weather import *

def test_class():
  send = SendWeatherData()
  if isinstance(send, SendWeatherData):
    print("obj is an instance")
    