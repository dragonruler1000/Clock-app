from geopy.geocoders import Nominatim, GoogleV3
import openmeteo_requests

import pandas as pd
import requests_cache
from retry_requests import retry
from timezonefinder import TimezoneFinder

app = Nominatim(user_agent="Weather-Clock")
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)
tz_finder = TimezoneFinder()

def weather(lat, long, temp_unit, tz):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": long,
        "hourly": "temperature_2m",
        "timezone": tz,
        "temperature_unit": temp_unit,
    }
    responces = openmeteo.weather_api(url, params=params)
    response = responces[0]
    print(f"Coordinates: {response.Latitude()}°N {response.Longitude()}°E")
    print(f"Elevation: {response.Elevation()} m asl")
    print(f"Timezone difference to GMT+0: {response.UtcOffsetSeconds()}s")

    hourly = response.Hourly()
    hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()

    hourly_data = {
        "date": pd.date_range(
            start = pd.to_datetime(hourly.Time(), unit="s", utc = True),
            end = pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
            freq = pd.Timedelta(seconds = hourly.Interval()),
            inclusive = "left"
        )
    }
    hourly_data["temperature_2m"] = hourly_temperature_2m

    hourly_dataframe = pd.DataFrame(data=hourly_data)
    print("\nHourly data\n", hourly_dataframe)

def hub():
    print("This option is being worked on and may not have all features working yet")
    address = input("Where do you want the weather for. eg Athens, AL: ")
    tempunit= input("What tempature uint do you prefer (fahrenheit or celsius):")
    location = app.geocode(address)
    print((location.latitude, location.longitude))
    lat = location.latitude
    long = location.longitude
    timezone = tz_finder.timezone_at(lng=long, lat=lat)
    print("Timezone: ", timezone)
    weather(lat, long, tempunit)
    