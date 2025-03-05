import json
import requests

url = 'http://api.open-notify.org/iss-now.json'

response = requests.get(url=url)

response.raise_for_status()

# print('response code:', response.status_code)
# print(json.dumps(response.json(), indent=4, sort_keys=True))

data = response.json()
longitude = data['iss_position']['longitude']
latitude = data['iss_position']['latitude']
iss_position = (longitude, latitude)
print(iss_position)
