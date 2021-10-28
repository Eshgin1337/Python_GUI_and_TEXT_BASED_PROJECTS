import requests
from datetime import datetime
import time
import smtplib

MY_LAT = 40.409264
MY_LONG = 49.867092

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


def is_close():
    return (iss_latitude - 5 < MY_LAT < iss_latitude + 5) and (iss_longitude - 5 < MY_LONG < iss_longitude + 5)


def currently_dark():
    return time_now.hour > sunset or sunrise > time_now.hour


while True:
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time.sleep(200)
    time_now = datetime.now()
    if is_close() and currently_dark():
        my_gmail = "eshgin.hasanov.1337@gmail.com"
        my_pass = "Eshgin2002@"
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(my_gmail, my_pass)
        connection.sendmail(from_addr=my_gmail,
                            to_addrs=my_gmail,
                            msg="Subject: Look up!\n\nLook at the sky, the ISS is over you in the sky!"
                            )

    time.sleep(60)

