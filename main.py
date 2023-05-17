from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import random

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def form_post(request: Request):
    result = "Type a number"
    return templates.TemplateResponse('index.html', context={'request': request, 'result': result})


@app.get("/{rand_number}")
async def get_random(rand_number):    
    if isinstance(int(rand_number), int) == False:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        return random.randint(0, int(rand_number))
