from geopy.geocoders import Nominatim
import geocoder 
import requests
geolocator = Nominatim(user_agent="geoapiExercises")
def weather():
    g = geocoder.ip('me')
    if g.city is not None:
        city=g.city
        api_key = "66c28b29bcbee3e14525e8f4774b091e"
        base_url = "https://api.openweathermap.org/data/2.5/weather?q="
        city_name = city
        complete_url = base_url + city_name + "&appid=" + api_key
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
        forcast="temperature in " + city_name +" is " + str(round(current_temperature-273)) + " degrees celcius and humidity is " + str(current_humidity) + " percent and today's weather is " + str(weather_description)
        return forcast
    else:
        return "Not able to get the weather information for your location"
