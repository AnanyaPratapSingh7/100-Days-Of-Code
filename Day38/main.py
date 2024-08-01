from datetime import  datetime
import requests

APP_ID = "5c89f0a7"
API_KEY = "6a04460f67428c601d277ac988711ce4"

NLP_EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

user_input = input("What exercises did you do today: ")

params = {
    "query": user_input,
}

response = requests.post(url=NLP_EXERCISE_ENDPOINT, headers=header, json=params)

json_data = response.json()

SHEETY_ENDPOINT = "https://api.sheety.co/cacad77947c7032b2990de01e55dd176/myWorkouts/workouts"

for item in json_data['exercises']:
    print(json_data['exercises'])
    result_data = {
        "workout": {
            "date": datetime.now().date().strftime("%d/%m/%Y"),
            "time": datetime.now().time().strftime("%H:%M:%S"),
            "exercise": item["name"],
            "duration": item['duration_min'],
            "calories": item["nf_calories"]
        }
    }
    response2 = requests.post(url=SHEETY_ENDPOINT, json=result_data)
