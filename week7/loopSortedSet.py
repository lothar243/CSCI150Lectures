# Loop through a set

from actor_to_movie import actor_to_movie

movie_set = set(actor_to_movie.values())

for movie in sorted(movie_set):
    print(movie)
