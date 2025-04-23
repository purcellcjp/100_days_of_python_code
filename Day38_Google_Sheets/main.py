import requests
from datetime import datetime
from config import APP_ID, API_KEY, BEAR_TOKEN

GENDER = 'male'
AGE = '57'
WEIGHT = '91'
HEIGHT = '182'

exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
sheety_endpoint = 'https://api.sheety.co/dadc7a7b95e345d4e624f50157b40d26/myWorkouts/workouts'


# exercise_input = input('Enter your completed exercises: ')
exercise_input = 'rowed 5km in 30 min and jump roped for 20 min'

today = datetime.now()


# Nutritionix API
headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

user_params = {
    'query': exercise_input,
    'gender': GENDER,
    'age': AGE,
    'weight_kg': WEIGHT,
    'height_cm': HEIGHT
}

response = requests.post(
    url=exercise_endpoint,
    json=user_params,
    headers=headers
)
result = response.json()
# print(result)
date = today.strftime('%x')
time = today.strftime('%X')

# Sheety Token Authorization
bearer_auth_header = {"Authorization": f"Bearer {BEAR_TOKEN}"}

for workout in result['exercises']:

    exercise = workout['name'].title()
    duration = workout['duration_min']
    calories = workout['nf_calories']

    print(date, time, exercise, duration, calories, sep='|')

    sheety_params = {
        'workout': {
            'date': date,
            'time': time,
            'exercise': exercise,
            'duration': duration,
            'calories': calories
        }
    }

    sheety_response = requests.post(
        url=sheety_endpoint,
        json=sheety_params,
        headers=bearer_auth_header
    )
    print(sheety_response.text)
