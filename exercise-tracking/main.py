import requests
from datetime import datetime

APP_ID = "12762db7"
API_KEY = "ac24072811c515420415148245a1b05b"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

my_exercises = input("Tell me what exercises have you done: ")

parameters = {
    "query": my_exercises
}


response = requests.post(url=exercise_endpoint, headers=headers, json=parameters)
data = response.json()

sheety_endpoint = "https://api.sheety.co/e8a46f8e2b48b11835374ed8d98ef5bb/workoutTracking/workouts"

today_date = datetime.now().strftime("%d%m%Y")
now_time = datetime.now().strftime("%X")

for exercise in data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheet_response = requests.post(url=sheety_endpoint, json=sheet_inputs, auth=("eshgin", "eshgin2002@$%"))
print(sheet_response.json())


