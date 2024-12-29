# This project uses SQLite3 for managing a simple movie database
import sqlite3

# Variable to store the connection of the film database
conn = sqlite3.connect('IMDB_movies.db')
cursor = conn.cursor()

# Creating the table if it doesn't exist
cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL       
    )
''')

def list_movies():
    cursor.execute("SELECT * FROM movies")
    movies = cursor.fetchall()
    if not movies:
        print("No movies detected!!")
    else:
        for row in movies:
            print(row)

def add_new_movie(name, time):
    cursor.execute("INSERT INTO movies (name, time) VALUES (?, ?)", (name, time))
    conn.commit()
    print("New movie added successfully!")

def update_movie(new_name, new_time, video_id):
    cursor.execute("UPDATE movies SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    conn.commit()
    print("Movie updated successfully!")

def delete_movie(video_id):
    cursor.execute("DELETE FROM movies WHERE id = ?", (video_id,))
    conn.commit()
    print("Movie deleted successfully!")

def main():
    while True:
        print("\nThis is Your IMDB FILM MOVIE LIST using the SQLITE3 DATABASE")
        print("\nEnter Your Choice !!\n")
        print("1. List movies")
        print("2. Add new movie")
        print("3. Update movie")
        print("4. Delete movie")
        print("5. Exit the App\n")

        choice = input("Enter your choice: ")

        if choice == '1':
            list_movies()
        elif choice == '2':
            name = input("Enter the name of the movie: ")
            time = input("Enter the time duration of the movie: ")
            add_new_movie(name, time)
        elif choice == '3':
            video_id = input("Enter the ID of the movie you want to update: ")
            name = input("Enter the new name of the movie: ")
            time = input("Enter the new time duration of the movie: ")
            update_movie(name, time, video_id)
        elif choice == '4':
            video_id = input("Enter the ID of the movie you want to delete: ")
            delete_movie(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice entered!!!")

    conn.close()

if __name__ == "__main__":
    main()
