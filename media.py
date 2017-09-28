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


class Movie():
    """
    A class describing properties and methods of a Movie instance.
    """

    def __init__(self, title, art, trailer):
        """
            Initialize an instance of a Movie class

            Arg(s):
                title - a string representing the title of the movie
                art - a string representing the URL to the poster of the movie
                trailer - a string representing URL to the trailer of the movie

            Example(s):
                title - 'The Godfather'
                art - 'https://vignette3.wikia.nocookie.net/mafia/images/b/b8/The-godfather.jpg/revision/latest?cb=20080922232324'  # NOQA
                trailer - 'https://youtu.be/sY1S34973zA'
        """
        self.title = title
        self.poster_image_url = art
        self.trailer_youtube_url = trailer
