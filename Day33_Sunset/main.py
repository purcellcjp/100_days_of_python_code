import requests
import json
from datetime import datetime


URL = 'https://api.sunrise-sunset.org/json'
MY_LAT = 38.907192
MY_LONG = -77.036873

parameters = {
    'lat': MY_LAT,
    'lng': MY_LONG,
    'formatted': 0,
}

response = requests.get(url=URL, params=parameters)
response.raise_for_status()

data = response.json()
print(json.dumps(data, indent=4, sort_keys=True))

sunrise = data['results']['sunrise']
sunset = data['results']['sunset']
# print('sunrise', sunrise, 'sunset', sunset, sep='|')

time_now = datetime.now()

# print(sunrise)
# print(sunrise.split('T'))
# print(sunrise.split('T')[1].split(':'))
# print(sunrise.split('T')[1].split(':')[0])
# print(time_now)

sunrise_hr = data['results']['sunrise'].split('T')[1].split(':')[0]
sunset_hr = data['results']['sunset'].split('T')[1].split(':')[0]

print(sunrise_hr)
print(sunset_hr)
