from weather_data_getter import WeatherDataReader
from datetime import datetime
from freezegun import freeze_time
# import pytest
# import unittest
import sys
sys.path.append('./lib/')


@freeze_time("2019-05-14 14:44:37")
def test_weather_getter():

    class FakeBus:
        def SMBus(self, port):
            return

    class FakeBme280:

        class fakeReadings:
            def __init__(self):
                self.temperature = 20
                self.pressure = 20
                self.humidity = 20

        def load_calibration_params(self, bus, port):
            return

        def sample(self, bus, address):
            data = self.fakeReadings()
            print(data)
            return data

    fakebme = FakeBme280()
    fakebus = FakeBus()
    stub_reader = WeatherDataReader(
        bme280_module=fakebme, smbus2_module=fakebus)
    stub_reader.readSensor()
    output = stub_reader.get()
    assert output == {
        "temperature": 20,
        "pressure": 20,
        "humidity": 20,
        "date": datetime.now().timestamp()
    }
