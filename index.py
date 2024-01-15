import requests
import json


city = input('Enter a City Name:')

#Api details
base_url = "https://api.openweathermap.org/data/2.5/weather"
api_key = "42d7d481fac11231e34eff4d0c55d4e5"

# parameters are inputs for the api
A = {
    "q":city, 
    "appid":api_key,
    "units":"metric"
}
# how do i finally make a api call or requests 
response = requests.get(base_url,A)
data=response.json()
print(json.dumps(data,indent=3))
D = data["weather"][0]["description"]
T = data["main"]["temp"]
print(f"The current temperature of the {city} is {T} and it's {D}")
