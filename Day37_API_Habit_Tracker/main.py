import requests
from datetime import datetime

USERNAME = 'purcellcj'
TOKEN = 'asdqwehlkk449jjlks2j23'
GRAPH_ID = 'graph1'

pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_config = {
    'id': 'graph1',
    'name': 'Cycling Graph',
    'unit': 'Km',
    'type': 'float',
    'color': 'sora'
}

headers = {
    'X-USER-TOKEN': TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'

today = datetime(year=2025, month=3, day=20)
# print(today.strftime('%Y%m%d'))

# pixel_data = {
#     'date': today.strftime('%Y%m%d'),
#     'quantity': '30'
# }

# response = requests.post(
#     url=pixel_endpoint, json=pixel_data, headers=headers)
# print(response.text)

# Update Existing Pixel
pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    'quantity': '60'
}

# response = requests.put(
#     url=pixel_update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

# Delete Pixel
pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

response = requests.delete(
    url=pixel_delete_endpoint, headers=headers
)
print(response.text)
