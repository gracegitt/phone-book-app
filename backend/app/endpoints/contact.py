from fastapi import APIRouter
from models.request import ContactRequest
from models.response import Response
from models.models import Contact
from db.database import Database
from sqlalchemy import and_, desc

from fastapi import APIRouter

# APIRouter creates path operations for product module

@router.get("/")
async def contacts():
    return {"firstname": "John", "lastname": "Njenga","phonenumber": "0125679"}


database = Database()
engine = database.get_db_connection()
