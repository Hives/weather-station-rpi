import json

from unittest import TestCase
from unittest.mock import patch
from send_weather import SendWeatherData

import requests

class TestAnalytics(TestCase):

  @patch('requests.post')
  def test_post_method(self, mock_post):
    class WeatherDataMockMock:
      def get(self):
        return {
          "some key": "some value"
        }
    send = SendWeatherData(WeatherDataMockMock())
    send.pushData()
    
    mock_post.assert_called_with("randomurl.com", data={'data': '{"some key": "some value"}'})
