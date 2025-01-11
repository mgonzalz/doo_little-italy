import requests
from django.conf import settings

APP_ID = settings.EDAMAM_NUTRITION_APP_ID
APP_KEY = settings.EDAMAM_NUTRITION_APP_KEY
BASE_URL = "https://api.edamam.com/api/nutrition-data"

def fetch_nutrition(ingredient_name):
    """
    Fetches nutrition from the Edamam Recipe API.
    """

    params = {
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "ingr": ingredient_name,
    }

    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None
