# Concept: saving a list of dicts to/from a file
import os

def save_movies(movies):
    with open("movie_list.txt", "w") as f:
        for m in movies:
            f.write(m["title"] + "," + m["genre"] + "," + str(m["rating"]) + "\n")

def load_movies():
    if os.path.exists("movie_list.txt"):
        with open("movie_list.txt", "r") as f:
            lines = f.readlines()
        loaded_movies = []
        for line in lines:
            parts = line.strip().split(",")
            loaded_movies.append({"title": parts[0], "genre": parts[1], "rating": float(parts[2])})
        return loaded_movies
    else: 
        return []

movies = [
    {"title": "Pirates", "genre": "Adventure", "rating": 4.5},
    {"title": "Cars", "genre": "Kids", "rating": 2.2},
    {"title": "Devil Yes", "genre": "Horror", "rating": 3.3},
    {"title": "Ogres Delight", "genre": "Horror", "rating": 6.66},
    {"title": "Dennis The Menace", "genre": "Kids", "rating": 4.3}
]
save_movies(movies)
result = load_movies()

for r in result:
    print(f"{r['title']}: ({r['genre']}) Rating: {r['rating']:.1f}")
