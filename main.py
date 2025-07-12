from fastapi import FastAPI, HTTPException, Depends
from uuid import UUID, uuid4
from typing import Optional
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware  # ✅ Import CORS
from sqlalchemy.orm import Session
from models import Url, User, LoginInput, RegisterInput
from demo import generate_short_code
from db.database import engine, SessionLocal
from db import models
from datetime import datetime, timedelta
import jwt
from dotenv import load_dotenv
import os


app = FastAPI()

# ✅ Add CORS middleware here

from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
SECRET_KEY = os.getenv("SECRET_KEY", "secret_itbienvenu_key_hahaha")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))

def generate_access_code(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Create DB tables (run once)
models.Base.metadata.create_all(bind=engine)

# Dependency to get DB session per request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/login")
def login(u: LoginInput, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == u.email).first()
    if user and user.password == u.password:
        data = {
            "names":user.names,
            "email":user.email
        }
        access_token = generate_access_code(data=data)
        return {"status": 200, "message": "User logged in", "email":user.email, "names":user.names,  "access_token":access_token}
    raise HTTPException(status_code=404, detail="Invalid email or password")

@app.post("/register")
def register(u: RegisterInput, db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(models.User.email == u.email).first()
    if existing_user:
        return {"status": "failed", "message": "User already registered"}
    
    new_user = models.User(
        id=uuid4(),
        names=u.names,
        email=u.email,
        password=u.password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"status": "success", "message": "User registered well"}


@app.get('/get_all')
def get_all_url(db: Session = Depends(get_db)):
    urls = db.query(models.Url).all()
    return urls


@app.post("/shorten")
def shorten_link(url: Url, db: Session = Depends(get_db)):
    # Generate a unique short code
    while True:
        shorten_url = generate_short_code(length=8)
        existing = db.query(models.Url).filter(models.Url.code == shorten_url).first()
        if not existing:
            break
    new_url = models.Url(
        id=uuid4(),
        valid=url.valid,
        code=shorten_url,
        clicks=0
    )
    db.add(new_url)
    db.commit()
    db.refresh(new_url)

    return {
        "message": "URL shortened well",
        "shorten_url": f"http://127.0.0.1:8000/{shorten_url}",
        "data": new_url
    }


@app.get("/{url_code}")
def redirect_user(url_code: str, db: Session = Depends(get_db)):
    url = db.query(models.Url).filter(models.Url.code == url_code).first()
    if url:
        url.clicks += 1
        db.commit()
        return RedirectResponse(url=url.valid)
    raise HTTPException(status_code=404, detail="Invalid code")
