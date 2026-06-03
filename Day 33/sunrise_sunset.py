import requests
import datetime as dt

MY_LAT = 26.264500
MY_LONG = 82.072800

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
# ye hume error isliye de rha hai kyuki ye api humse 2 parameters bhi as input chahti hai that
# are longitude (lng) and latitude (lat) so usi ke liye humne upr parameters mein use likh rhe hai

data = response.json()

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunrise)
print(sunset)

time_now = dt.datetime.now()
print(time_now)
