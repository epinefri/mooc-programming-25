def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    # database is a list of dictionaries
    movie_db = {}
    movie_db["name"] = name
    movie_db["director"] = director
    movie_db["year"] = year
    movie_db["runtime"] = runtime

    database.append(movie_db)

if __name__ == "__main__":
    database = []
    add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
    add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
    print(database)