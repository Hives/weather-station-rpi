# Raspberry Pi weather station app

## Installation

```script
pip3 install -r requirements.txt
```

## Testing

Run tests and check coverage:

```script
pytest --cov=lib
```
-----

### if __name__ == '__main__' whats this???
You should get in the habit of using this almost always.

```python
// weather_data_sender.py bottom of code

if __name__ == "__main__":
    WeatherDataSender().push_data()
```

Anything that comes after `if __name__ == '__main__':` will be run when you explicitly run your file.

```script
python3 weather_data_sender.py
```

However, if you import myfile.py elsewhere:

```python
import myfile
```
Nothing under `if __name__ == '__main__':` will be called.



