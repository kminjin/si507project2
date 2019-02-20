import pandas as pd
import numpy as np
import csv
import random
from itertools import product, permutations

with open ("movies_clean.csv", "r", encoding="utf8") as csvfile:
    reader=csv.reader(csvfile)
    data=[]
    for data_info in reader:
        data.append(data_info)
    csvfile.close()

# class Numofmovies:
#     def __init__(self,entire_movies_list):
#         self.entirelist=entire_movies_list
#     def __str__(self):
accum=0
for each in data:
    accum+=1
print(accum)


class Movie:
    def __init__(self,data):
        # self.one_movie_info=one_movie_info
        self.title=data[0]
        self.rating=data[14]
    def __str__(self):
        return "{} | {} ".format(self.title,self.rating)


testlist=[]
for each in data[1:7]:
    testlist.append(str(Movie(each)))

# space="<br"
# sample_movies= " "
# for each in testlist:
#     z=space.join(each)
#     sample_movies=sample_movies+z+"\n"
#
# print(sample_movies)


sample_movies=" "
for each in testlist:
    sample_movies=sample_movies+str(each)+"<br>"
print(sample_movies)



# linebreak="<br>"
# sample_movies= " "
# for each in testlist:
#     z=linebreak.join(each)
#     sample_movies=sample_movies+z

# print(sample_movies)
#
# print(type(sample_movies))
