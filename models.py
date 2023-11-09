from datetime import datetime
from typing import List, Union

from pydantic import *

class User(BaseModel):
    name: str
    age: int
    is_adult: bool

class Feedback(BaseModel):
    name: str
    message: str

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: PositiveInt | None = None
    is_subscribed: bool | None = False