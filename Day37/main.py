import requests
from datetime import datetime

USERNAME = "daemonisgod"
TOKEN = "fhieuigfuishf"

#Create a new user

USER_API = "https://pixe.la/v1/users"

request ={
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

requests.post(url=USER_API, json=request)
#----------------------------------------------------------

#Creating a graph
graph_api_endpoint = f'https://pixe.la/v1/users/{USERNAME}/graphs'


graph_id = "daemon234"

request2 = {
    "id": graph_id,
    "name": "Codeing",
    "unit": "commit",
    "type": "int",
    "color": "sora",
}
headers = {
    "X-USER-TOKEN": TOKEN, 
}

requests.post(url=graph_api_endpoint, json=request2, headers=headers)
#------------------------------------------------------------------

#---------------Adding a pixel---------------------
PIXEL_API = f"https://pixe.la/v1/users/{USERNAME}/graphs/{graph_id}"

today = datetime.now()

post_pixel = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "7",
}

response3 = requests.post(url=PIXEL_API, json=post_pixel, headers=headers)

print(response3.text)