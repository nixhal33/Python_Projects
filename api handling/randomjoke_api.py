import requests,random

def fetching_randomjoke_api():
    url="https://api.freeapi.app/api/v1/public/randomjokes?limit=10&query=science&inc=categories%2Cid%2Ccontent&page=1"
    response=requests.get(url)
    data=response.json()

    if data["success"] and "data" in data:
        
        joke_data=data["data"]["data"]
        random_joke=random.choice(joke_data)
        
        joke_content=random_joke["content"]
        joke_categories=random_joke["categories"]
        joke_id=random_joke["id"]

        return joke_content,joke_categories,joke_id

    else:
        raise Exception("Error in fetching joke data from the API")

def main():
    
    try:
        joke_content,joke_categories,joke_id=fetching_randomjoke_api()
        print(f"\n Joke Content: {joke_content}")
        print(f"\n Joke Categories: {joke_categories}")
        print(f"\n Joke ID: {joke_id}")

    except Exception as e:
        print(str(e))

if __name__=="__main__":
    main()

