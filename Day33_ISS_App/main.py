import requests
from datetime import datetime, timezone
import smtplib
import time

# Alexandria, VA
MY_LAT = 38.804836  # Your latitude
MY_LONG = -77.046921  # Your longitude
my_email = 'purcellqnapnas@gmail.com'
my_password = 'ttrj hcwm plts zrpq'


def is_iss_station_close(variance):

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    # print('-'*30)
    # print(iss_latitude, iss_longitude)
    # print('-'*30)

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - variance <= iss_latitude <= MY_LAT + variance and MY_LONG - variance <= iss_longitude <= MY_LONG + variance:
        return True
    else:
        return False


def is_dark():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(
        "https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now(timezone.utc)

    if sunset + 1 <= time_now.hour <= sunrise - 1:
        return True
    else:
        return False


def execute_station_email():
    if is_iss_station_close(5) and is_dark():
        # send email
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=my_email,
                                msg='Subject:ISS\n\nThe ISS is in view!!!')
        return True
    else:
        return False


# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
n = 0
while True:
    n += 1
    retval = execute_station_email()
    print(retval, n)
    time.sleep(60)
