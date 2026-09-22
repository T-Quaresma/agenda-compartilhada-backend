from pydantic import BaseModel
from typing import Optional

class Group_Creation(BaseModel):
    name: str
    image: Optional[str] = None

class Group_Search(BaseModel):
    group_id: Optional[int] = None

class Group_Delete(BaseModel):
    group_id: int

class Group_Update(BaseModel):
    group_id: int
    name: Optional[str] = None
    image: Optional[str] = None