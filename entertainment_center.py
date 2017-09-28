"""
Project: Movie Trailer Website

Description: A project developed as part of Udacity nanodegree in
             Full-stack Web Development. This projects demonstrates
             knowledge of fundamental Object Oriented Programming (OOP)
             principals, as well as showcases the ability to utilize
             this knowledge using Python programming language.

Developer: Eduard Doroskevic
Contact: e_doroskevic@hotmail.com
Date: 27th of September 2017

File(s):
    entertainment_center.py , media.py, fresh_tomatoes.py
"""


# Loading necessary module components.
from media import Movie
from fresh_tomatoes import open_movies_page


# Instantiating three objects of type Movie.
movie_your_highness = Movie(
    "Your Highness",
    "https://upload.wikimedia.org/wikipedia/en/thumb/3/31/Your_Highness_Poster.jpg/220px-Your_Highness_Poster.jpg",  # NOQA
    "https://youtu.be/FplWxtPzWY8"
    )

movie_hackers = Movie(
    "Hackers",
    "https://uk.movieposter.com/posters/archive/main/79/MPW-39928",
    "https://youtu.be/Rn2cf_wJ4f4"
    )

movie_hacksaw_ridge = Movie(
    "Hacksaw Ridge",
    "https://upload.wikimedia.org/wikipedia/en/8/8a/Hacksaw_Ridge_poster.png",
    "https://youtu.be/s2-1hz1juBI"
    )


# Creating a list to hold created movies above.
movies = [movie_your_highness, movie_hackers, movie_hacksaw_ridge]


# Generating .html fil
open_movies_page(movies)
