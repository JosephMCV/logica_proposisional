from os import path, system as sys
from fastapi import FastAPI, Request, Body
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.models.information import Information
from app.controllers.index_controller import index_controller

app = FastAPI()

templates = Jinja2Templates(directory="app/views/templates")
app.mount("/static", StaticFiles(directory=path.join("app","views","public","static")), name="static")

def validate_integer(value):
    if type(value) != int:
        return ("El valor no es entero")

@app.get("/")
async def index(request: Request):
    sys('cls')
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/form-data")
async def form_data(information: Information = Body(...)):
    print(f"La info recibida es:\n\n{information}")
    return index_controller(information)

@app.on_event("startup")
async def start_up():
    sys('cls')