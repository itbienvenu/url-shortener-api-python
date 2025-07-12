from fastapi import FastAPI, HTTPException
from uuid import UUID, uuid4
from typing import Optional, List
from enum import Enum
from models import Url, User, LoginInput,RegisterInput
from demo import generate_short_code
from fastapi.responses import RedirectResponse


app = FastAPI()

db: List[Url] = []
users: List[User] = [
    User(id=uuid4(), 
         names="Mwimule Bienvenu", 
         email="bienvenu@gmail.com", 
         password="Bienvenu123@",
         
        )
]
@app.post("/login")
def login(u: LoginInput):
    for user in users:
        if user.email == u.email and user.password == u.password:
            return {"status":200, "message":"User logged in"}
    raise HTTPException(status_code=404, detail="Invalid email or password")    

@app.post("/register")
def register(u: RegisterInput):
    for user in users:
        if user.email == u.email:
            return {"status":"failed", "message":"User alredy registred"}
        users.append(u)
        return {"status":"success", "message":"User Registered well"}


@app.get('/get_all')
def get_all_url():
    return db
def index():
    return {"message":"Heome page"}

@app.post("/shorten")

def shorten_link(url: Url):
    while True:
        shorten_url = generate_short_code(length=8)
        if not any(u.code == shorten_url for u in db):
            break
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

# @app.get("/{code}")
@app.get("/{url_code}")
def redirect_user(url_code: str):
    for url in db:
        if url.code == url_code:
            url.clicks +=1
            return RedirectResponse(url=url.valid)  # or RedirectResponse
    raise HTTPException(status_code=404, detail="Invalid code")

