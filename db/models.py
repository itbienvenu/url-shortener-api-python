from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

import uuid

import datetime

Base  = declarative_base()

class Url(Base):
    __tablename__ = "urls"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    valid = Column(String, nullable=False)
    code = Column(String, unique=True, nullable=True)
    clicks = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.datetime.now)
    expires_at = Column(DateTime, nullable=True)

class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    names = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now)