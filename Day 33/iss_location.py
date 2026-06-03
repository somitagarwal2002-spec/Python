import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response) #<Response [200]> matlab humari request ka answer milega iss api se

if response.status_code == 404:
    raise Exception("That resource does not exist")
elif response.status_code == 401:
    raise Exception("You are not authorized to access this data")
# hrr error status_code k liye aise if-elif block likhna possible nhi hai isiliye requests module
# mein already iske solution ke liye ek function already present hai

response.raise_for_status()
# this is used for checking all the status codes and simply tells you the particular response code
# problem 

data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(iss_position)
