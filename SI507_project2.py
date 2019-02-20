from movie_tools import*
import csv
from flask import Flask

#Set up application
app=Flask(__name__)

@app.route('/')
def home():
    return '<h1>{} movies recorded</h1>'.format(self.numofmovies)


# Should display a list of movies from the CSV data -- any! (At least 5 movies, but could be any number and any subsection you want -- the first five, a random set of five or ten… anything you like, completely up to you.)
@app.route('/movies/ratings/')
def weclome_bank(bankname):
    movie=Movie(onerow)
    return '<h1>Welcome to {}!<h1>'.format(bank.name)


if __name__ == '__main__':
    app.run()
