from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class ContactRequest(BaseModel):
    firstname: str = Field(
        None, title="First Name", max_length=1000
    )
    lastname: str = Field(
        None, title="Last Name", max_length=1000
    )
    phonenumber: int = Field(None, title="Phonenumber")


class ContactUpdateRequest(BaseModel):
    firstname: str = Field(
        None, title="First Name", max_length=1000
    )
    firstname: str = Field(
        None, title="Last Name", max_length=1000
    )
    phonenumber: int
