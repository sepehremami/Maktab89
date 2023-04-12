from pymongo import MongoClient


client = MongoClient('localhost', 27017)
database = client.mflix
pelham_movie = database.movies.find_one({'title':'The Taking of Pelham 1 2 3'})
pipline = [
    {'$match':
     {
    'movie_id' : pelham_movie['_id']
    }},
    {
    '$group':
            {
            '_id':'$name'
            }},
    {
    '$project':{'_id':1}
    }]
people_who_commented = database.comments.aggregate(pipline)

for person in people_who_commented:
    print(person)
