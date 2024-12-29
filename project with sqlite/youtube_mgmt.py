# this project i am gonna make using the sqlite3 
# it will make the project using the database more clean and easy to use

import sqlite3

# variable to store the connection of the film db
conn=sqlite3.connect('IMDB_film.db')

cursor=conn.cursor()

# now i am gonna create the table using sqlite as i am also gonna use sqlite
cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS movies (
                id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL       
               )
''')

def list_movies():
    cursor.execute("SELECT * FROM  ")  # this will select all the movies from the movies table
    movies=cursor.fetchall() # this will fetch all the movies from the table
    for row in movies:
        print(row) # this will print the movie

def add_new_movie(name,time): # this will add the new movie to the table
    cursor.execute("INSERT INTO movies (name,time) VALUES (?,?)",(name,time)) # this will insert the movie name and time duration of the movie
    conn.commit() # this will commit the changes to the database or simply save the changes to the database
    print("New movie added successfully!") # this will print the message that the movie is added successfully

def update_movie(new_name,new_time,video_id): # this will update the movie from the table
    cursor.execute("UPDATE movies SET name=?, time=? WHERE id=?",(new_name,new_time,video_id)) # this will update the movie name and time duration of the movie
    conn.commit()
    print("Movie updated successfully!")

def delete_movie(video_id): # this will delete the movie from the table
    cursor.execute("DELETE FROM movies WHERE id=?",(video_id,))
    conn.commit()
    print("Movie deleted successfully!") 




# simply creating the main method for different condition that will be needed for crud operations
def main():
    # creating the while loop to run this command until i finish my work or finish my entry
    while True:
        print(" \n This is Your IMDB FILM MOVIE LIST using the SQLITE3 DATABASE")
        print("\n  Enter Your Choice !! \n")
        print("\n")
        print("1. List movies ")
        print("2. Add new movie ")
        print("3. Update  movie")
        print("4. Delete movie ")
        print("5. Exit the App")
        print('\n')

        choice=input("Enter your choice: ")

        # using the if else statement to check the choice of the user        
        if choice=='1':
            list_movies()
       
        elif choice=='2':
            named=input("Enter the name of the movie : ")
            times=input("Enter the time duration of the movie : ")
            add_new_movie(name = named,time =times)
       
        elif choice=='3':
            video_id=input("Enter the ID of the movie you want to update : ")
            name=input("Enter the new name of the movie : ")
            time=input("Enter the new time duration of the movie : ")
            update_movie(video_id,name,time)
       
        elif choice=='4':
            video_id=input("Enter the id of the movie you want to delete : ")
            delete_movie(video_id)
       
        elif choice=='5':
            break
      
        else:
            print("Invalid choice entered!!!")

    conn.close()




# this is because it will first see the main method and it will execute, if your program name is main then run the main method
if __name__ == "__main__":
    main()