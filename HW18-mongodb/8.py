from pymongo import MongoClient

client = MongoClient('localhost', 27017)

database = client.mflix
pipline = [
    {
    '$unwind':"$languages"
    },
    {
    '$group':
        {
        '_id': "$languages",
        'average': { '$avg': '$imdb.rating' }
        }
    }, 
    {
    '$sort': {'average':-1}
    }]
movie_by_language_and_imdb_rating = database.movies.aggregate(pipline)
for movie_lang in movie_by_language_and_imdb_rating:
    print(movie_lang)