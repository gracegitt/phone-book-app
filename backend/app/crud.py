from sqlalchemy.orm import Session

from app import models, schema

def get_contact(db: Session):
    return db.query(models.Contact).filter(models.Contact)()