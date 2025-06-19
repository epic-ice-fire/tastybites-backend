from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import date

class Customer(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str
    surname: str
    middle_name: Optional[str]
    date_of_birth: date
    home_address: str
    date_of_registration: date
    _334942894723: bool
