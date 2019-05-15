import bme280
import smbus2
from time import sleep

port = 1
address = 0x77
bus = smbus2.SMBus(port)

bme280.load_calibration_params(bus, address)

while True:
    sensor_data = bme280.sample(bus, address)
    print(sensor_data)
    ambient_temperature = sensor_data.temperature
    humidity = sensor_data.humidity
    pressure = sensor_data.pressure
    print(ambient_temperature, humidity, pressure)
    sleep(5)
