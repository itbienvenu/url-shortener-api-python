from pydantic import BaseModel
from uuid import UUID, uuid4
from typing import Optional
class Url(BaseModel):
    id: Optional[UUID] = uuid4()
    valid: str
    code: Optional[str] = None

