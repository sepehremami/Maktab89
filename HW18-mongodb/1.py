from pymongo import MongoClient
from pprint import pprint

myclient = MongoClient('localhost', 27017)

database = myclient.mflix
movies = database.movies.find({'genres':'History'},{'_id':0, 'title':1})
movie = [movie for movie in movies]
pprint (movie)


    



