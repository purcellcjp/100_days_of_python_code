import requests
import json
from config import api_key

url = "http://api.openweathermap.org/data/2.5/"
city = 'Washington D.C.'
units = 'imperial'
lon = -77.0364
lat = 38.8951

# query_url = f'{url}weather?appid={api_key}&q={city}&units={units}'
# print('-'*20)
# print(query_url)
# print('-'*20)

# query_url = f'{url}forecast?lat={lat}&lon={lon}&appid={api_key}'


forecast_url = "http://api.openweathermap.org/data/2.5/forecast"
params = {
    'appid': api_key,
    'lat': lat,
    'lon': lon,
    'cnt': 4,
}

response = requests.get(forecast_url, params=params)
response.raise_for_status()

response_json = response.json()

# print(response_json['list'][0]['weather'][0]['id'])
will_rain = False

for item in response_json['list']:
    id = int(item['weather'][0]['id'])
    if id < 700:
        will_rain = True
        break
print('-'*20)
if will_rain:
    print('bring an umbrella')
else:
    print('don\'t bring an umbrella')
print('-'*20)

# print(json.dumps(response_json, indent=4, sort_keys=True))
