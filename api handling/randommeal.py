import requests


def fetching_randommeal():
    url="https://api.freeapi.app/api/v1/public/meals/meal/random"
    response=requests.get(url)
    meal_data=response.json()

    if meal_data["success"] and "data" in meal_data:
        
        meal_rand= meal_data["data"]
        
        meal_name=meal_rand["strName"]
        meal_category=meal_rand["strCategory"]
        meal_instructions=meal_rand["strInstructions"]

        ingredients=[]
        for i in range(1,21):
            ingredient=meal_rand[f"strIngredient{i}"]
            if ingredient:
                ingredients.append(ingredient)
            else:
                break

        return meal_name,meal_category,meal_instructions,ingredients
    else:
        raise Exception("Error in fetching meal data from the API")
    
def main():
    try:
        
        meal_name,meal_category,meal_instructions,ingredients=fetching_randommeal()
       
        print(f"\n Meal Name: {meal_name}")
        print(f"\n Meal Category: {meal_category}")
        for ingredient in ingredients:
            print(f"\n Ingredient: {ingredient}")
        print(f"\n Meal Instructions: {meal_instructions} \n")

    except Exception as e:
        print(str(e))

if __name__=="__main__":
    main()