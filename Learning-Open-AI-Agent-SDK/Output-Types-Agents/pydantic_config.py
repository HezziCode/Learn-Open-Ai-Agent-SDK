from pydantic import BaseModel

class Output_config(BaseModel):
    n1: int
    n2: int
    result: int