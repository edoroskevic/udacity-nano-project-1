# Movie Trailer Website

## Description
This project creates a basic boilerplate to share your favourite movies. 

A project developed as part of Udacity Nanodegree in Full-stack Web Development. This projects demonstrates knowledge of fundamental Object Oriented Programming (OOP)
principals, as well as showcases the ability to utilizethis knowledge using Python programming language. 

## Installation

1. Install [Python](https://www.python.org/) 
2. Install [Git](https://desktop.github.com/)

3. Using terminal or command prompt, clone the repository

```
  git clone https://github.com/edoroskevic/udacity-nano-project-1.git <folder_name>
```
4. Using terminal or command prompt whilst in `<folder_name>`, run
```
  python entertainment_center.py
```
5. Open **fresh_tomatoes.html** generated in step four.

## Usage

The project consists of three files **media.py**, **entertainment_center.py** and **fresh_tomatoes.py**, where **fresh_tomatoes.py**
has been supplied by the *Udacity*.

The **media.py** implements a single class - *Movie* containing constructor taking three arguments - _`title`_, _`art`_ and _`trailer`_. 

1. _`title`_ - a string containing the name of the movie
2. _`art`_ - a string containing an _URL_ to the poster of the movie
3. _`trailer`_ - a string containing an _URL_ to the trailer. 

The **entertainment_center.py** uses both **media.py** and **fresh_tomatoes.py**. By default, it consists of three instances of type *Movie*.
These instances are stored in a list - `movies` which is then passed to a function `open_movies_page` taken from **fresh_tomatoes.py**. 
Upon execution, the function `open_movies_page` generates an **.html** file named **fresh_tomatoes.html**. This file can be open by 
browser of your choice. 

The function `open_movies_page` takes a list consisting of objects of type *Movie*. By creating your own objects of type `Movie`,
adding them to the list `movies` and executing the step five as described above - you will observe changes in generated **.html** file.

Good luck, and thank you for your time :)
