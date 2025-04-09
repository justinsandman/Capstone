#
#
#

import requests

# Function to fetch nutrition data from an external API (e.g., Nutritionix, OpenFoodFacts, etc.)
def fetch_nutrition_data(food_item):
    API_URL = "https://api.nutritionix.com/v1_1/search"
    API_KEY = "your_api_key_here"  # API key needs to be discussed
    APP_ID = "your_app_id_here"    # App ID goes here 

    # Make a request to the API
    response = requests.get(
        API_URL,
        params={
            "query": food_item,
            "fields": "item_name,nf_calories,nf_protein,nf_total_carbohydrate,nf_total_fat",
            "appId": APP_ID,
            "appKey": API_KEY,
        }
    )
    
    if response.status_code == 200:
        data = response.json()
        # Assuming the response contains a list of foods, we'll return the first result
        food_data = data.get("hits", [])[0]["fields"]
        return {
            "food_item": food_data.get("item_name"),
            "calories": food_data.get("nf_calories"),
            "protein": food_data.get("nf_protein"),
            "carbs": food_data.get("nf_total_carbohydrate"),
            "fats": food_data.get("nf_total_fat"),
        }
    else:
        return {"error": "Unable to fetch nutrition data"}
