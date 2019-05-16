import bme280  # Import library of methods for sensor
import smbus2  # Import library to read RPi system bus
from datetime import datetime


class WeatherDataReader:
    def __init__(self, bme280_module=bme280, smbus2_module=smbus2):
        self.bme280 = bme280_module
        self.smbus2 = smbus2_module
        port = 1
        self.address = 0x77
        self.bus = self.smbus2.SMBus(port)
        self.bme280.load_calibration_params(self.bus, self.address)

    def readSensor(self):
        self.sensor_data = self.bme280.sample(self.bus, self.address)

    def get(self):
        # access dictionary for the sample data
        ambient_temperature = self.sensor_data.temperature
        pressure = self.sensor_data.pressure
        humidity = self.sensor_data.humidity

        output = {
            "temperature": ambient_temperature,
            "pressure": pressure,
            "humidity": humidity,
            "date": datetime.now().timestamp()
        }
        return output
