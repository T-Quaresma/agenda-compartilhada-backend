from pydantic import BaseModel
from typing import Optional

class Group_Creation(BaseModel):
    name: str
    user_id: int
    image: Optional[str] = None

class Group_Search(BaseModel):
    user_id: Optional[int] = None
    group_id: Optional[int] = None

class Group_Delete(BaseModel):
    group_id: int

class Group_Update(BaseModel):
    group_id: int
    name: Optional[str] = None
    image: Optional[str] = None