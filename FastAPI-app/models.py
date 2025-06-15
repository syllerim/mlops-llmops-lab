from pydantic import BaseModel
from typing import Optional

class Identity(BaseModel):
    name: str 
    surname: Optional[str] = None
    date_of_birth: str