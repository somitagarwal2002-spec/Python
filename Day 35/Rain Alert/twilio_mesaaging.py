import requests
# from twilio.rest import Client
import os

# api_key = os.environ.get("OWM_API_KEY") 
api_key = "my_api_key"
account_sid = "my_account_sid"
# auth_token = os.environ.get("AUTH_TOKEN")
auth_token = "auth_token"

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
    if int(conidtion_code) > 700:
        will_rain = True

# if will_rain:
#     client = Client(account_sid, auth_token)
#     message = client.messages.create(
#         body= "Bring your Umbrella",
#         from_="+17472857471",
#         # to=os.environ.get("MY_NUMBER"),
#         to="my_number"
    # )

    # print(message.status)
