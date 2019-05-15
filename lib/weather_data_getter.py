import bme280 # Import library of methods for sensor
import smbus2 # Import library to read RPi system bus

from datetime import datetime

class WeatherDataReader:
  port = 1 # system bus port 1 where RPi is connected
  address = 0x77 # BME280 address, default on production, could be different
  bus = smbus2.SMBus(port) # var for connection to port

  def get(self):
    bme280.load_calibration_params(self.bus,self.address) # load current calibration settings on bme280 before sampling
    sensor_data = bme280.sample(self.bus, self.address) # bme280 library method to take a sample and store into variable as dictionary

    # access that dictionary for the sample data
    ambient_temperature = sensor_data.temperature
    pressure = sensor_data.pressure
    humidity = sensor_data.humidity

    output = {
      "temperature": ambient_temperature,
      "pressure": pressure,
      "humidity": humidity,
      "date": datetime.now().timestamp()
    }
    return output




# print(ambient_temperature, humidity, pressure) # print the data vars!
