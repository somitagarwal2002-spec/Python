import requests
import datetime as dt

username = "somit"
token = "iwquhfihna23wq1"

pixela_endpoint = "https://pixe.la/v1/users"

user_parameters = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response)
# ab humne apna user bana liya hai aur agr hum iss response wali line ko dobara chalate hai to 
# ye hume error dega ki user already exist

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"

graph_parameters = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": token,
}

# graph_request = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(graph_request.text)

today = dt.datetime(year=2026, month=6, day=4)

adding_pixel_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_parameters["id"]}"

adding_pixel_parameters = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "9.05",
}

adding_pixel_response = requests.post(url=adding_pixel_endpoint, json=adding_pixel_parameters, headers=headers)
# print(adding_pixel_response.text)

update_pixel_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_parameters["id"]}/20260604"

update_pixel_parameter = {
    "quantity": "15",
}

update_pixel_response = requests.put(url=update_pixel_endpoint, json=update_pixel_parameter, headers=headers)
# print(update_pixel_response.text)


delete_pixel_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_parameters["id"]}/20260604"

delete_response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(delete_response.text)
