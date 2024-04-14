#Pre-reqs:
#pip install requests
#Make OpenWeather Map Account
#Ensure API is activated
#Copy API Key here
#Note: Free plan cannot predict weather, just shows live weather

import datetime as dt
import requests #for API requests

print("SKYCAST WEATHER APP")
print()

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "{add api_key here}"  #add api key
CITY = input("Enter City: ")

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

response = requests.get(url).json()

def kelvin_to_celsius(kelvin):
    celsius = kelvin-273.15
    return celsius

#print(response)

print(CITY, " Forecast:")
print()

temp_kelvin = response['main']['temp']   #temperature was in 2 dictionaries main and temp
temp_celsius = round(kelvin_to_celsius(temp_kelvin), 1)

print('Temperature: ', temp_celsius, "Degrees Celsius")

feel_like_kelvin = response['main']['feels_like']
feel_like_celsius = round(kelvin_to_celsius(feel_like_kelvin), 1)

print('Feels like: ', feel_like_celsius, "Degrees Celsius")

description = response['weather'][0]['main']

print('Description: ', description)

humidity = response['main']['humidity']

print('Humidity: ', humidity, "%")

wind_speed = response['wind']['speed']

print("Wind Speed: ", wind_speed, "m/s")

temp_max_kelvin = response['main']['temp_max']
temp_max_celsius = round(kelvin_to_celsius(temp_max_kelvin), 1)

print("Maximum Temperature: ", temp_max_celsius)

temp_min_kelvin = response['main']['temp_min']
temp_min_celsius = round(kelvin_to_celsius(temp_min_kelvin), 1)

print("Minimum Temperature: ", temp_min_celsius)

sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])  #adding timezone as timezone shown in wrt to our timezone

print("Sunrise Time: ", sunrise_time)

sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])  #adding timezone as timezone shown in wrt to our timezone

print("Sunset Time: ", sunset_time)

print()
