from datetime import date
from pydantic import BaseModel


class Contact(BaseModel):
    firstname = str
    lastname = str
    phonenumber = int

    class Config:
        orm_mode = True