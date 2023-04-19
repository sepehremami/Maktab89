from pymongo import MongoClient

client = MongoClient('localhost',27017)
database = client.mflix

pipline = [
    {'$unwind':'$cast'},
    {'$unwind':'$genres'}, 
    {'$group':
        {
        '_id':'$cast',
        'genres': {
                    '$addToSet':'$genres'
                  }
    
   }},
   {
    '$project':{"_id":0,'cast':'$_id', 'genres':1}
   }]
actors_with_generes = database.movies.aggregate(pipline)

for actor in actors_with_generes:
    print(actor)
