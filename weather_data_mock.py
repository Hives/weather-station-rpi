from random import random
from datetime import datetime

class WeatherDataMock:
  def get(self):
    output = {
      "temperature": round(random() * 30, 2),
      "pressure": 1000 + round(random() * 200, 2),
      "humidity": round(random() * 10, 2),
      "date": datetime.now().timestamp()
    }
    return output
