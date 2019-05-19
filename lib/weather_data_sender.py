from weather_data_reader import WeatherDataReader
import json
import requests


class WeatherDataSender:

    api_url = 'https://quiet-everglades-27917.herokuapp.com/api/data'

    def __init__(self, weather_data_reader=WeatherDataReader):
        self.weather_data_reader = weather_data_reader()

    def push_data(self):
        weather_record = self.__get_data()
        print("POST-ing data to %s" % (self.api_url))
        response = requests.post(self.api_url, data={'data': weather_record})
        print(response)

    def __get_data(self):
        return json.dumps(self.weather_data_reader.extract_data())

if __name__ == "__main__":
    WeatherDataSender().push_data()
