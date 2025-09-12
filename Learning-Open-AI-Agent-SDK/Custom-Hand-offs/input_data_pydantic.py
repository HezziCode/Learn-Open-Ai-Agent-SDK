from pydantic import BaseModel

class InputDataSchema(BaseModel):
    reason : str