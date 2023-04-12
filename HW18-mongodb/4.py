from pymongo import MongoClient

client = MongoClient('localhost', 27017)
database = client.mflix
pipline = [
    {
    '$unwind':"$languages"
    },
    {'$group': 
        { '_id': "$languages",
        'count': { '$sum': 1 }
        }
    }]
movies = database.movies.aggregate(pipline)

for movie in movies:
    print(movie)