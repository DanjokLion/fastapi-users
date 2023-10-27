from datetime import datetime
from typing import List, Union

from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    is_adult: bool

class Feedback(BaseModel):
    name: str
    message: str