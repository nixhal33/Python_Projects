import json # json file is 

def load_data():
    try:
        with open('newfile.txt', 'r') as file:
            content = file.read().strip()  # Read and strip whitespace
            return json.loads(content) if content else []  # Return empty list if content is empty
    except FileNotFoundError:
        return []  # If file doesn't exist, return an empty list

def datasaver_helper(videos):
    with open('newfile.txt','w') as file:
        json.dump(videos,file) #here json.load means it loads the data and dump means write all the data in that file..... and it takes two parameters

def list_all_ytvids(videos): # simply the helper method
    if not videos:
        print("\n no video details found!! \n")
    
    print("\n Your List of Video are as follows : \n")
    
    for index, video in enumerate(videos,start=1):   #here this start=1 means start enumerate start the indexing with 1.. # this enumerate function job is that if there's any enumerable or any iterable method then it will add the index in those list or  
              print("\n")
              print("*" * 50)
              print(f"{index}. Video name : {video['Video name']} , Video time : {video['Video time']}") 
              print("*" * 50)
              # but in here if i use this statement then it will not print the dictionary but the exact name of the video and it's time...
              # print(f"{index}. {video}")------->  if i use this print statement then it will print the list in form   of dictionary ie: {'Video name': 'Project 1', 'Video time': '20 minutes'}

def add_new_vid(videos):
    print("*"*50)
    vid_name=input("Enter the name of video : ")
    vid_time=input("Enter the time duration of video : ")
    videos.append({'Video name': vid_name , 'Video time' : vid_time})
    print("*"*50)
    print("New video added successfully!")
    print("*"*50)
    
    datasaver_helper(videos)

def update_vid(videos):
    list_all_ytvids(videos)
    print("\n")
    update=int(input("Enter the number of the video you want to update : "))
    if 1<=update<=len(videos):
        updated_name=input("Enter the new video name :")
        updated_time=input("Enter the new video time  :")
        videos[update-1]= {'Video name':updated_name, 'Video time' : updated_time}
        print("New video updated successfully!")
        datasaver_helper(videos) 
    else:
        print("Invalid video Index entered!!!")

def delete_vid(videos):
    list_all_ytvids(videos)
    delete=int(input("Enter the video number you want to delete : ?"))
    if 1<=delete<=len(videos):
        del videos[delete-1]
        datasaver_helper(videos)
        print(f"Video no. '{delete}' deleted successfully!")
    else:
        print("Invalid video index entered!!!")


def main_process(): # after writing below code below this main_process method i right indented using ctrl+] sign

    videos=load_data()

    # for checking the choice is required. It will execute like if the choice came true then only it will execute the choices
    while True:
        print(" \n This is Your Youtube Manager ")
        print("\n  Enter Your Choice !! ")
        print("\n")
        print("1. List your all youtube videos ")
        print("2. Add new youtube video ")
        print("3. Update youtube video")
        print("4. Delete youtube video ")
        print("5. Exit the App")
        print('\n')
        
        choice=input("Enter your choice: ")

        # print(videos)

        # this is similar to switchcase like using in c or c++ or in like java 
        match choice:
            case '1':
                list_all_ytvids(videos)
            case '2':
                add_new_vid(videos)
            case '3':
                update_vid(videos)
            case '4':
                delete_vid(videos)
            case '5':
                break
            case _:
                print("\n")
                print("You have entered Invalid Choice.......!!!!!!!!")
if __name__ == "__main__":
    main_process()