from dotenv import load_dotenv
from functools import lru_cache
import os
import pathlib
from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from .airtable import push_to_airtable
BASE_DIR = pathlib.Path(__file__).parent #src folder

app = FastAPI()
templates = Jinja2Templates(directory= BASE_DIR/ "templates")

@lru_cache()
def cached_dotenv():
    load_dotenv()

cached_dotenv()

@app.get("/")
def home_view(request: Request):
    return templates.TemplateResponse("home.html", {
        "request":request
    })

@app.post("/")
def home_signup_view(request: Request, email:str = Form(...)):
    """
    CSRF to be added!!!
    """

    #to send email to airtable
    did_send = push_to_airtable(email=email)
    return templates.TemplateResponse("home.html", {
        "request":request,
        "submitted_email": email,
        "did_send": did_send
    })