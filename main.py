from fastapi import FastAPI, HTTPException
from uuid import UUID, uuid4
from typing import Optional, List
from enum import Enum
from models import Url
from demo import generate_short_code


app = FastAPI()

db: List[Url] = []

@app.get('/get_all')
def get_all_url():
    return db
def index():
    return {"message":"Heome page"}

@app.post("/shorten")

def shorten_link(url: Url):
    shorten_url = generate_short_code(length=8)
    new_url = Url(
        id=uuid4(),
        valid=url.valid,
        code=shorten_url
    )
    db.append(new_url)
    return{
        "message":"URL shortened well",
        "shorten_url":f"http://127.0.0.1:8080/{shorten_url}",
        "data": new_url
    }

@app.get("/{url_code}")
def redirect_user(url_code):
    code = [code for code in url_code.split("/")][-1]
    for url in db:
        if url.code == code:
            return {"message":url.valid}
    raise HTTPException(status_code=404, detail="Invalid code")
