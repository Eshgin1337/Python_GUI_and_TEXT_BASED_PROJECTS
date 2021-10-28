import requests
import os
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

my_data = {
    "lat": 44.723660,
    "lon": 37.769508,
    "appid": "YOUR_APP_ID",
    "exclude": "current,minutely,daily"
}
data = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=my_data)
data.raise_for_status()
weather_data = data.json()
hourly_data = weather_data["hourly"]
for i in range(12):
    if hourly_data[i]["weather"][0]["id"] < 700:
        print("Bring an umbrella")
        break
