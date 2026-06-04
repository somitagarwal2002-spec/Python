import requests

api_key = "my_api_key"

parameter = {
    "lat": 26.256531,
    "lon": 82.082475,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameter)
# print(response.status_code)
response.raise_for_status()

weather_data = response.json()
# print(data)

will_rain = False

for hour_data in weather_data["list"]:
    conidtion_code = hour_data["weather"][0]["id"]
    if int(conidtion_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an Umbrella")
else:
    print("No need to bring Umbrella")
