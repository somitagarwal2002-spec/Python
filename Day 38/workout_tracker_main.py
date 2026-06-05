import requests
import datetime as dt

APP_ID = "app_274eed3b4a8e46e3b9536e95"
API_KEY = "nix_live_4J34X9CpuuL5ObdplaQ0Q7p4z5spkb5q"
BASE_URL = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
sheety_api_url_endpoint = "https://api.sheety.co/Somit Agarwal/My Workouts/workouts"
retrieve_row_api = "https://api.sheety.co/c405f8eb0e191acb4e4ce71d8a3a78b7/myWorkouts/workouts"
add_row_api = "https://api.sheety.co/c405f8eb0e191acb4e4ce71d8a3a78b7/myWorkouts/workouts"
GENDER = "male"
WEIGHT_KG = 75
HEIGHT_CM = 168
AGE = 23

today = dt.datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%H:%M:%S")
# print(date)
# print(time)

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": "swam for 1 hour",
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE

}

response = requests.post(url=BASE_URL, headers=header, json=parameters)
print(response.status_code)
print(response.text)
response.raise_for_status()

result = response.json()
print(result["exercises"][0])

sheety_headers = {
    "Authorization": "Bearer secret-token",
    "Content-Type": "application/json"
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "Date": date,
            "Time": time,
            "Exercise": exercise["name"].title(),
            "Duration": exercise["duration_min"],
            "Calories": exercise["nf_calories"],
        }
    }

    sheet_response = requests.post(url=add_row_api, json=sheet_inputs, headers=sheety_headers)
    print(sheet_response.status_code)
    print(sheet_response.text)
    print(sheet_response)

