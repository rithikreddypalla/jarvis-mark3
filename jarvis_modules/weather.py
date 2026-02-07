import os
import requests

OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY', 'YOUR_OPENWEATHER_API_KEY')

def weather(city="hyderabad"):
    api_key = OPENWEATHER_API_KEY
    base_url = "https://api.openweathermap.org/data/2.5/weather?q="
    complete_url = base_url + city + "&appid=" + api_key
    response = requests.get(complete_url)
    x = response.json()
    if x.get("cod") != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_humidity = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        forecast = f"Temperature in {city} is {round(current_temperature-273)}°C, humidity is {current_humidity}%, weather: {weather_description}"
        return forecast
    else:
        return "Weather information not found."
