import requests
from unittest import TestCase
from unittest.mock import patch
import sys
sys.path.append('./lib/')


class WeatherDataMockMock:
    def get(self):
        return {
            "some key": "some value"
        }


class WeatherDataSenderMock:
    test_api_url = 'www.raspberrypisender.com'

    def pushData(self):
        requests.post(self.test_api_url, data={
                      'data': '{"test key": "test value"}'})


class TestAnalytics(TestCase):
    def test_class_has_correct_api_url(self):
        sender = WeatherDataSenderMock()
        assert sender.test_api_url == 'www.raspberrypisender.com'

    @patch('requests.post')
    def test_sender_mock(self, mock_post):
        test_sender = WeatherDataSenderMock()
        test_sender.pushData()
        url = WeatherDataSenderMock.test_api_url

        mock_post.assert_called_with(
            url, data={'data': '{"test key": "test value"}'})
