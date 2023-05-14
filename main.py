from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import random

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
def form_post(request: Request):
    result = "Type a number"
    return templates.TemplateResponse('index.html', context={'request': request, 'result': result})


@app.get("/{rand_number}")
async def get_random(rand_number):
    return random.randint(9, int(rand_number))
