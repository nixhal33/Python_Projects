# importing requests library to make the api request and random library to fetch the random joke from the api

import requests,random

def fetching_randomuser_freeapi():
    url="https://api.freeapi.app/api/v1/public/randomusers?page=1&limit=10"
    response=requests.get(url)
    data=response.json()
    

    if data["success"] and "data" in data:
        
        user_data=data["data"]["data"]
        random_userdata=random.choice(user_data)    # fetching the user data from the api
        
        user_name=random_userdata["login"]["username"]     
        user_country=random_userdata["location"]["country"]
        user_email=random_userdata["email"]
        user_coordinate=random_userdata["location"]["coordinates"]
        
        return user_name,user_country,user_email,user_coordinate
    else:
        raise Exception("Error in fetching user data from the API")

# whenever accepting or using the external web request from external source then always use the try and except block to handle the error and exception cuz you are working with the database maybe the data request will timeout or database will not respond

def main():
    try:
        user_name,user_country,user_email,user_coordinate=fetching_randomuser_freeapi()
        print(f"\n User Name: {user_name}")
        print(f"\n User Country: {user_country}")
        print(f"\n User Email: {user_email}")
        print(f"\n User Coordinate: {user_coordinate} \n")

    except Exception as e:
        print(str(e))
 

if __name__=="__main__":
    main()


def comments():

    """ 
    Here's a short and easy explanation of what happens in each part of the code:
    Imports

    a. import requests, random

        requests: Used to make HTTP requests (like fetching data from an API).
        random: Used to select random items from a list.

    b. Function: fetching_randomuser_freeapi()

        Define API URL
        url="https://api.freeapi.app/api/v1/public/randomusers?page=1&limit=10"

        Specifies the API endpoint to fetch random user data.

    c. Make API Request

        response=requests.get(url)
        data=response.json()

        Sends a GET request to the API and converts the response into JSON format.

    d. Check for Success

        if data["success"] and "data" in data:

        Confirms the API response is successful and contains the required data.

    e. Extract User Data

        user_data=data["data"]["data"]
        random_userdata=random.choice(user_data)

        Retrieves the list of users from the API response.
        Picks a random user from the list.

    f. Extract Random User Details

        user_name=random_userdata["login"]["username"]
        user_country=random_userdata["location"]["country"]
        user_email=random_userdata["email"]
        user_coordinate=random_userdata["location"]["coordinates"]

        Pulls specific details like username, country, email, and coordinates of the selected random user.

    g. Return User Details

        return user_name, user_country, user_email, user_coordinate

        Sends the fetched details back to the main function.

    h. Handle Errors

        else:
            raise Exception("Error in fetching user data from the API")

            Raises an error if the API response is unsuccessful.

    i. Function: main()

        Fetch User Data in Try Block

        user_name,user_country,user_email,user_coordinate=fetching_randomuser_freeapi()

        Calls fetching_randomuser_freeapi() to get random user details.

    j. Print User Details

        print(f"\n User Name: {user_name}")
        print(f"\n User Country: {user_country}")
        print(f"\n User Email: {user_email}")
        print(f"\n User Coordinate: {user_coordinate} \n")

        Displays the fetched user details (username, country, email, coordinates).

    k. Handle Errors in Except Block

        except Exception as e:
            print(str(e))

            Prints an error message if something goes wrong (e.g., API issues).

    l. Main Execution

        if __name__=="__main__":
            main()

            Ensures the main() function runs only when the script is executed directly.

    In summary:

        Makes a request to a random user API.
        Fetches a random user from the response.
        Extracts user details and displays them.
        Handles errors gracefull

    """
