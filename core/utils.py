"""
Utility functions for the application.

This module contains helper functions for external integrations,
such as retrieving nutritional data via APIs (e.g., Nutritionix).

Authors: Justin Sandstedt, Matthew Swandal, Gabriel Morgan
"""


import requests



def fetch_nutrition_data(food_item):
    """
    Fetch nutrition facts for a given food item using an external nutrition API.

    Parameters:
        food_item (str): The name of the food item to search.

    Returns:
        dict: A dictionary containing nutritional information:
              - food_item: str
              - calories: float
              - protein: float
              - carbs: float
              - fats: float
              If the request fails, returns:
              - error: str
    """
    # Base URL for Nutrition API 
    API_URL = "https://api.nutritionix.com/v1_1/search"

    # ... 
    API_KEY = "your_api_key_here"  # API key needs to be discussed
    APP_ID = "your_app_id_here"    # App ID goes here 

    
# Prepare request parameters
    params = {
        "query": food_item,
        "fields": "item_name,nf_calories,nf_protein,nf_total_carbohydrate,nf_total_fat",
        "appId": APP_ID,
        "appKey": API_KEY,
    }

    # Send GET request
    response = requests.get(API_URL, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        if data.get("hits"):
            food_data = data["hits"][0]["fields"]
            return {
                "food_item": food_data.get("item_name"),
                "calories": food_data.get("nf_calories"),
                "protein": food_data.get("nf_protein"),
                "carbs": food_data.get("nf_total_carbohydrate"),
                "fats": food_data.get("nf_total_fat"),
            }
        else:
            return {"error": "No results found for the given food item."}
    else:
        return {"error": f"Failed to fetch data: HTTP {response.status_code}"}