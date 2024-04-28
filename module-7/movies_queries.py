import mysql.connector
from mysql.connector import errorcode

# Configuration details
config = {
    "user": "root",
    "password": "Jayden#811",
    "host": "localhost",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    # Connect to the MySQL database
    db = mysql.connector.connect(**config)
    print("\nDatabase user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    print("\n")
    cursor = db.cursor()

    # select all fields for genre 
    cursor = db.cursor()
    cursor.execute("SELECT studio_id, studio_name FROM studio")
    studios = cursor.fetchall()
    print("Displaying Studio Records")
    for studio in studios:
        print("Studio ID: {}\nStudio Name: {}".format(studio[0], studio[1]))
        print("\n")

    # select all fields for genre 
    cursor = db.cursor()
    cursor.execute("SELECT genre_id, genre_name FROM genre")
    genres = cursor.fetchall()
    print("Displaying Genre Records")
    for genre in genres:
        print("Genre ID: {}\nGenre Name: {}".format(genre[0], genre[1]))
        print("\n")
    # select short films
    cursor = db.cursor()
    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime <= 120")
    films = cursor.fetchall()
    print("Displaying Short Film Records")
    for film in films:
        print("Film Name: {}\nFilm Runtime: {}".format(film[0], film[1]))
        print("\n")
    # film names by director
    cursor = db.cursor()
    cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director, film_name")
    films = cursor.fetchall()
    print("Displaying Director Records In Order")
    for film in films:
        print("Film Name: {}\nFilm Director: {}".format(film[0], film[1]))
        print("\n")
    

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
    else:
        print(err)
finally:
    if db is not None and db.is_connected():
        db.close()
        print("\nConnection to MySQL closed.")

input("\n\nPress any key to exit...")