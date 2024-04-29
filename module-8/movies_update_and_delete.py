import mysql.connector

def show_films(cursor, title):
    cursor.execute("""
        SELECT film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name'
        FROM film
        INNER JOIN genre ON film.genre_id = genre.genre_id
        INNER JOIN studio ON film.studio_id = studio.studio_id;
    """)

    films = cursor.fetchall()

    print("\n -- {} --".format(title))
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))

# Database configuration with the correct database name
config = {
    'user': 'root',
    'password': 'Jayden#811',
    'host': '127.0.0.1',
    'database': 'movies',
    'raise_on_warnings': True
}

try:
    # Establish a database connection
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    # Call the show_films function
    show_films(cursor, "DISPLAYING FILMS")

except mysql.connector.Error as err:
    print("An error occurred: {}".format(err))

finally:
    if 'cnx' in locals() or 'cnx' in globals():
        cnx.close()
    input("Press Enter to exit...")