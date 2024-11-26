from pydantic import BaseModel
from typing import Optional

class ModelBase(BaseModel):
    name: str
    description: Optional[str] = None
    version: str

class ModelCreate(ModelBase):
    pass

class ModelUpdate(BaseModel):
    description: Optional[str] = None

class ModelResponse(ModelBase):
    id: int

    class Config:
        orm_mode = True