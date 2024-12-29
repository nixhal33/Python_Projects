import requests,random

def fetching_randomfood():
    url="https://api.freeapi.app/api/v1/public/meals/meal/random"
    response=requests.get(url)
    meal=response.json()

    if meal["success"] and "data" in meal:
        meal_data=meal["data"]
        food=