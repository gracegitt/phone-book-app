from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

contacts = [
    {
        "firstname": "John",
        "lastname": "Njenga",
        "phonenumber": "99944"
    }
]


    
@app.get("/contacts", tags=["contacts"])
async def get_contact() -> dict:
    return { "data": contacts }

@app.post("/contacts", tags=["contacts"])
async def add_contact(contact: dict) -> dict:
    contacts.append(contact)
    return {
        "data": { "Contact added." }
    }

@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to your contact list."}