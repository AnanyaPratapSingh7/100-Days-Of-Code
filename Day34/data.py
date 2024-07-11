import requests

API_ENDPOINT = 'https://opentdb.com/api.php'
parameters = {
    "amount": 10,
    "category":18,
    "type":"boolean",
}
response = requests.get(API_ENDPOINT,params=parameters)
response.raise_for_status()


question_data = response.json()["results"]
