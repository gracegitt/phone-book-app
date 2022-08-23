import uvicorn
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.db.database import engine
#from  import crud, model
from app import schema
from app.models import models
from app.db.database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


origins = ["http://localhost:8000"]



if __name__ == "__main__":
    uvicorn.run("app.api:app", host="0.0.0.0", port=8000, reload=True)