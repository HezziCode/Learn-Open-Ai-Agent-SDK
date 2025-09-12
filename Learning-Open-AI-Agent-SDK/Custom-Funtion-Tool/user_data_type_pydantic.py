# Pydantic Method
from pydantic import BaseModel


class UserDataType(BaseModel):
    name: str
    age: int
    role:str