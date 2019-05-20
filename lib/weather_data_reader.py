import bme280  # Import library of methods for sensor
import smbus2  # Import library to read RPi system bus
from datetime import datetime


class WeatherDataReader:
    def __init__(self, bme280_module=bme280, smbus2_module=smbus2):
        smbus2 = smbus2_module
        port = 1
        self.sensor = bme280_module
        self.address = 0x77
        self.bus = smbus2.SMBus(port)

        self.sensor.load_calibration_params(self.bus, self.address)

    def extract_data(self):
        sensor_data = self.__read_sensor()

        weather_data = {
            "temperature": sensor_data.temperature,
            "pressure": sensor_data.pressure,
            "humidity": sensor_data.humidity,
            "date": datetime.now().timestamp()
        }

        return weather_data

    def __read_sensor(self):
        return self.sensor.sample(self.bus, self.address)
