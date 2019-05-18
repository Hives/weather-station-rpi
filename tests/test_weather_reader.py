from weather_data_reader import WeatherDataReader
from datetime import datetime
from freezegun import freeze_time
import sys
sys.path.append('./lib/')


@freeze_time("2019-05-14 14:44:37")
def test_weather_reader():

    class FakeBus:
        def SMBus(self, port):
            return

    class FakeBme280:
        class fake_readings:
            def __init__(self):
                self.temperature = 20
                self.pressure = 21
                self.humidity = 22

        def load_calibration_params(self, bus, port):
            return

        def sample(self, bus, address):
            data = self.fake_readings()
            print(data)
            return data

    fake_bme = FakeBme280()
    fake_bus = FakeBus()
    reader = WeatherDataReader(
            bme280_module=fake_bme, smbus2_module=fake_bus)
    output = reader.extract_data()

    assert output == {
        "temperature": 20,
        "pressure": 21,
        "humidity": 22,
        "date": datetime.now().timestamp()
    }
