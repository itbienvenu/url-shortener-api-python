from pydantic import BaseModel, EmailStr
from uuid import UUID, uuid4
from typing import Optional
from datetime import datetime, timedelta

class Url(BaseModel):
    id: Optional[UUID] = uuid4()
    valid: str
    code: Optional[str] = None
    clicks: int = 0
    created_at: datetime = datetime.now()
    expires_ad: Optional[datetime] = None

class LoginInput(BaseModel):
    email: EmailStr
    password: str

class RegisterInput(BaseModel):
    id: Optional[UUID] = uuid4()
    names: str
    email: EmailStr
    password: str

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    names: str
    email: EmailStr
    password: str
    created_at: datetime = datetime.now()