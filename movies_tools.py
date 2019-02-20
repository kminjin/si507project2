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

# list_of_title=[]
# for each in range(len(data)):
#     list_of_title.append(data[each][0])
# print(list_of_title)

class Movie:
    def __init__(self,one_movie_info):
        self.one_movie_info=one_movie_info

class Numofmovies:
    def __init__(self,entire_movies_list):
        self.emv=entire_movies_list
    def __str__(self):
        accum=0
        for each in self.emv:
            accum+=1
        return str(accum)
    def generatelistmovies(self):
        list_of_title=[]
        for each in range(len(self.emv)):
            list_of_title.append(self.emv[each][0])

        space=" "
        sample_movies= " "
        random.shuffle(list_of_title)
        short_movies_list=list_of_title[0:100]
        options = permutations (short_movies_list, 5)
        all_options= list(options)
        random.shuffle(all_options)
        for each in all_options[:5]:
        #     z=space.join(each)
        #     sample_movies=sample_movies+z+" | " +each[14]+"\n"
        # return sample_movies
            return "{} | {}"+"<br>".format(each[0], each[14])



test = Numofmovies(data)

#print(test)

print(test.generatelistmovies)
