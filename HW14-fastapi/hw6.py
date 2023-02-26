from fastapi import FastAPI, APIRouter
from typing import List, Dict
from pydantic import BaseModel


class Item(BaseModel):
    item_name : str
    price : int


app = FastAPI()
api_router = APIRouter()

item = [
    {
        "item_name" : "Milk", 
        "price" : 30
    },
    {
        "item_name" : "sweet", 
        "price" : 50
    },
    {
        "item_name" : "Cookie", 
        "price" : 90
    }
]


@api_router.get("/", status_code=200)
def root():
    return {'message: hello'}


@api_router.post('/search/', status_code=201)
async def sum(item: List[Item]):
    const = 0 
    for object in item:
        const += object.price
    return const


app.include_router(api_router)

if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")