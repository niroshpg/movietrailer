# ===============================================================================
# Movie Trailer Web Site
# ----------------------
# This project is to track favorite movie trailers with its associate meta
# data.
#
# This is the main module of the movie trailer web site. This will create list
# of instance of movies using Movie class and launch them in a web page using
# launcher module
#
# @author: Nirosh Gunaratne
# @since: 28/08/2017
# @version: 1.0
# ===============================================================================

import launcher
import media

# Create  each instance of favorite movies available
metrix = media.Movie(
    "Matrix",
    "A story about escaping from a virtul matrix created by machines",
    "http://static.rogerebert.com/uploads/movie/movie_poster/the-matrix-1999/large_gynBNzwyaHKtXqlEKKLioNkjKgN.jpg",  # NOQA
    "https://www.youtube.com/watch?v=vKQi3bBA1y8")

avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

toystory = media.Movie(
    "Toy Story",
    "A stroy of a boy and his toys that comes to life",
    "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg",  # NOQA
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")


nemo = media.Movie("Finding Nemo",
    "A clown fish Maline searching his lost son Nemo",
    "https://s-media-cache-ak0.pinimg.com/originals/76/e9/bb/76e9bb65c557b261bb2e71a0dc08bd55.jpg",   # NOQA
    "https://www.youtube.com/watch?v=2zLkasScy7A&t=15s")


dragons = media.Movie(
    "How to train your dragon",
    "Stroy about kindom of dragons",
    "http://static.rogerebert.com/uploads/movie/movie_poster/how-to-train-your-dragon-2010/large_zMAm3WYmvD40FaWFsOmpicQFabz.jpg",   # NOQA
    "https://www.youtube.com/watch?v=oKiYuIsPxYk")

xmen = media.Movie(
    "X-Men",
    "A story about genetic super humans",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjU1ODM1MzYxN15BMl5BanBnXkFtZTgwOTA4NDE2ODE@._V1_UY1200_CR91,0,630,1200_AL_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=Iy5R5_T243w")

# Set movie list to be used in movie page
movies = [
    metrix,
    avatar,
    toystory,
    nemo,
    dragons,
    xmen
    ]

# Pass the created list of movies to launcher module and open them in a web
# browser
launcher.open_movies_page(movies)
