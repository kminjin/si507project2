from movies_tools import *
import csv
from flask import Flask

#Set up application
app=Flask(__name__)

#Routes
@app.route('/')
def index():
    return '<h1>{} movies recorded</h1>'.format(accum)


@app.route('/movies/ratings/')
def movieslist():
    return'{}'.format(sample_movies)


if __name__ == '__main__':
    app.run()
