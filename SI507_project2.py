from movies_tools import *
import csv
from flask import Flask

#Set up application
app=Flask(__name__)

@app.route('/')
def index():
    return '<h1>{} movies recorded</h1>'.format(accum)


# # Should display a list of movies from the CSV data -- any! (At least 5 movies, but could be any number and any subsection you want -- the first five, a random set of five or ten… anything you like, completely up to you.)
with open ("movies_clean.csv", "r", encoding="utf8") as csvfile:
    reader=csv.reader(csvfile)
    data=[]
    for data_info in reader:
        data.append(data_info)
    csvfile.close()


@app.route('/movies/ratings/')
def movieslist():
    return'{}'.format(sample_movies)


if __name__ == '__main__':
    app.run()
