from fastapi import FastAPI, APIRouter
from typing import List



app = FastAPI()
api_router = APIRouter()



@api_router.get("/", status_code=200)
def root():
    return {'message: hello'}


@api_router.post('/even/', status_code=201)
async def sum_of_evens(list_of_numbers: List[int]):
    const = 0
    for number in list_of_numbers:
        if number % 2 == 0:
            const += number
    return const


app.include_router(api_router)

if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")