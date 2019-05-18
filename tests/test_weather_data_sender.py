import sys
sys.path.append('./lib/')
import requests
from weather_data_sender import WeatherDataSender
from unittest import TestCase
from unittest.mock import patch


class WeatherDataReaderMock:
    def extract_data(self):
        return { "test key": "test value" }

@patch('requests.post')
def test_sender_mock(mock_post_request):

    sender = WeatherDataSender(WeatherDataReaderMock)
    sender.push_data()
    url = WeatherDataSender.api_url

    mock_post_request.assert_called_with(
            url, data = { 'data': '{"test key": "test value"}' })

