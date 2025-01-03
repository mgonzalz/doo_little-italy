import requests
import time
from django.conf import settings

APP_ID = settings.EDAMAM_RECIPE_APP_ID
APP_KEY = settings.EDAMAM_RECIPE_APP_KEY
BASE_URL = "https://api.edamam.com/api/recipes/v2"

def fetch_recipes(query, max_results=100):
    """
    Fetches recipes from the Edamam Recipe API.
    """

    params = {
        "type": "public",
        "q": query,
        "app_id": APP_ID,
        "app_key": APP_KEY
    }

    all_recipes = []
    current_url = BASE_URL

    while len(all_recipes) < max_results:
        print(f"Fetching URL: {current_url}")
        response = requests.get(current_url, params=params if current_url == BASE_URL else None)
        if response.status_code == 200:
            data = response.json()
            hits = data.get("hits", [])
            all_recipes.extend(hits)

            # Check for the next page URL.
            current_url = data.get("_links", {}).get("next", {}).get("href")
            if not current_url:
                break
        else:
            print(f"Error: {response.status_code} - {response.text}")
            response.raise_for_status()

        # Add a delay to respect the 3 requests per minute limit - FREE plan.
        time.sleep(20)

    return all_recipes[:max_results]

