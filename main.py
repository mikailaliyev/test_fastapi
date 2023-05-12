from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
async def root():
    return {"example": "This is an example", "data": 999}

@app.get("/random/{rand_number}")
async def get_random(rand_number):
    return random.randint(9, int(rand_number))
