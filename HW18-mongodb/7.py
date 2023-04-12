from pymongo import MongoClient

client = MongoClient('localhost', 27017)

database = client.mflix
pipline = [
    {'$unwind':'$cast'},
    {'$group':
        {
        '_id':'$cast',
        'count':{'$sum':1}
        }}, 
        {
        '$sort':{'count':-1}
        }]
actors_with_movie_count = database.movies.aggregate(pipline)
for actor in actors_with_movie_count:
    print(actor)
