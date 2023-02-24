from fastapi import FastAPI, APIRouter

app = FastAPI()
api_router = APIRouter()

books = [
    {
        "book_name" : "It Ends with Us", 
        'description' : "It Ends with Us is a romance novel by Colleen Hoover, published by Atria Books on August 2, 2016. Based on the relationship between her mother and father, Hoover described it as\"the hardest book I've ever written\"."
    },
    {
        "book_name" : "Verity", 
        'description' : "New York Times BestsellerUSA Today BestsellerThe Globe and Mail BestsellerPublishers Weekly BestsellerWhose truth is the lie? Stay up all night reading the sensational psychological thriller that has readers obsessed, from the #1 New York Times bestselling author of It Ends With Us. "
    },
    {
        "book_name" : "Atomic Habits", 
        'description' : "James Clear, an expert on habit formation, reveals practical strategies that will teach you how to form good habits, break bad ones, and master the tiny behaviors that lead to remarkable results. "
    }
]


@api_router.get("/", status_code=200)
def root():
    return {'message: hello'}


@api_router.get('/search/', status_code=201)
async def search(term: str = "example"):
    temp = []
    for dictionary in books:
        for key, value in dictionary.items():
            if term.lower() in key.lower() or term.lower() in value.lower():
                temp.append(dictionary)
                break
    return temp




app.include_router(api_router)

if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")