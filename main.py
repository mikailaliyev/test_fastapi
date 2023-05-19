from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import random
import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000)

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def form_post(request: Request):
    result = "Type a number"
    return templates.TemplateResponse('index.html', context={'request': request, 'result': result})


@app.get("/{rand_number}")
async def get_random(rand_number):  
  if rand_number.isnumeric() == False:
    raise HTTPException(status_code=404, detail="You should enter only integers")
  return random.randint(0, int(rand_number))
