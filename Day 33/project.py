import requests
import datetime as dt
import smtplib
import time

my_email = "somitprogramming@gmail.com"
password = "csohdvmtpfnlcscr"

MY_LAT = 26.264500
MY_LONG = 82.072800

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["latitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True



def is_night():
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]

    print(sunrise.split("T")[1].split(":"))
    print(sunset.split("T")[1].split(":"))

    time_now = dt.datetime.now().hour
    
    if time_now >= sunset or time_now <= sunrise:
        return True
    
while True:
    time.sleep(60)       
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=f"Subject:ISS IS OVERHEAD\n\nISS Satellite is overhead of you")

