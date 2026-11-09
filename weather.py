from geopy.geocoders import Nominatim
import openmeteo_requests

import pandas as pd
import requests_cache
from retry_requests import retry
from timezonefinder import TimezoneFinder

import ssl, certifi

ctx = ssl.create_default_context(cafile=certifi.where())

app = Nominatim(user_agent="Weather-Clock", ssl_context=ctx)
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)
tz_finder = TimezoneFinder()

def weather(lat, long, temp_unit, tz):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": long,
        "hourly": ["temperature_2m", "precipitation_probability", "precipitation", "wind_speed_10m", "wind_direction_10m", "temperature_80m"],
        "models": "best_match",
        "current": "apparent_temperature",
        "timezone": tz,
        "forecast_days": 3,
        "temperature_unit": temp_unit,
    }
    responces = openmeteo.weather_api(url, params=params)
    response = responces[0]
    cords = str(f"Coordinates: {response.Latitude()}°N {response.Longitude()}°E")
    elev = str(f"Elevation: {response.Elevation()} m asl")
    diff = str(f"Timezone difference to GMT+0: {response.UtcOffsetSeconds()}s")

    current = response.Current()
    current_apparent_temperature = current.Variables(0).Value()

    time=str(f"\nCurrent time: {current.Time()}")
    ct = str(f"Current apparent temperature: {current_apparent_temperature}")

    hourly = response.Hourly()
    hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
    hourly_precipitation_probability = hourly.Variables(1).ValuesAsNumpy()
    hourly_precipitation = hourly.Variables(2).ValuesAsNumpy()
    hourly_wind_speed_10m = hourly.Variables(3).ValuesAsNumpy()
    hourly_wind_direction_10m = hourly.Variables(4).ValuesAsNumpy()

    hourly_data = {
        "date": pd.date_range(
            start = pd.to_datetime(hourly.Time(), unit="s", utc = True),
            end = pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
            freq = pd.Timedelta(seconds = hourly.Interval()),
            inclusive = "left"
        ).tz_convert(response.Timezone().decode())
    }
    hourly_data["temperature_2m"] = hourly_temperature_2m
    hourly_data["precipitation_probability"] = hourly_precipitation_probability
    hourly_data["precipitation"] = hourly_precipitation
    hourly_data["wind_speed_10m"] = hourly_wind_speed_10m
    hourly_data["wind_direction_10m"] = hourly_wind_direction_10m

    hd = pd.DataFrame(data=hourly_data)
    # ("\nHourly data\n", hourly_dataframe)
    return(cords, elev, diff, time, ct, hd)

def hub(address, unit):
    # address = input("Where do you want the weather for. eg Athens, AL: ")
    # unit= input("What tempature uint do you prefer (f or c):")
    if unit == "f" or unit == "F":
        tempunit = "fahrenheit"
    elif unit == "c" or unit == "C":
        tempunit = "celsius"
    location = app.geocode(address)
    lat = location.latitude
    long = location.longitude
    tz = tz_finder.timezone_at(lng=long, lat=lat)
    # print("Timezone: ", timezone)
    cords, diff, elev, time, ct, hd = weather(lat, long, tempunit, tz)
    return(tz, cords, diff, elev, time, ct, hd)
    # print(cords)
    # print(diff)
    # print(elev)
    # print(time)
    # print(ct)
    # print("\nHourly data\n", hd)
    