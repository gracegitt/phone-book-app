from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, INTEGER, String

Base = declarative_base()

class Contact(Base):
    __tablename__ = "contact"
    
    firstname = Column(String)
    lastname = Column(String)
    phonenumber = Column(INTEGER, primary_key=True, index=True)

    

  
