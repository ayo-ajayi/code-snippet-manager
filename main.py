from db.database import Database, Collection
from fastapi import FastAPI, HTTPException
from api.router import Router
from api.repo import Repo
from pydantic_settings import BaseSettings
from api.controller import Controller
import os
from dotenv import load_dotenv

load_dotenv()

db_uri = os.environ.get("DB_URI")
db_name = os.environ.get("DB_NAME")

if not db_uri:
    print("DB_URI not set")
    exit(1)
if not db_name:
    print("DB_NAME not set")
    exit(1)

try:
    db = Database(db_uri, db_name)
except ConnectionError as e:
    print(f"Could not connect to database: {str(e)}")
    exit(1)


class Settings(BaseSettings):
    openapi_url: str = "/openapi.json"


settings = Settings()
app = FastAPI(openapi_url=settings.openapi_url)

app.include_router(
    Router.get_router(Controller(Repo(Collection(db, "code")))),
    prefix="/code",
    tags=["code"],
)


@app.get("/", tags=["root"])
async def read_root():
    return {"message": "Welcome to code snippet manager app!"}
