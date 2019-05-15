import pytest
import requests
from unittest import TestCase
from unittest.mock import patch
# import requests_mock

from send_weather import SendWeatherData

class WeatherDataMockMock:
  def get(self):
    return {
      "some key": "some value"
    }

class TestAnalytics(TestCase):

  @patch('requests.post')
  def test_post_method(self, mock_post):
    sender = SendWeatherData(WeatherDataMockMock())
    sender.pushData()

    url = SendWeatherData.api_url
    
    mock_post.assert_called_with(url, data={'data': '{"some key": "some value"}'})

  def test_class_has_correct_api_url(self):
    sender = SendWeatherData(WeatherDataMockMock())
    assert sender.api_url == "https://fb724921.ngrok.io/api/data"
    