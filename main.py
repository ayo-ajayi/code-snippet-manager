from db.database import Database, Collection
from fastapi import FastAPI
from api.router import Router
from api.repo import Repo
from pydantic_settings import BaseSettings
from api.controller import Controller
import os
from dotenv import load_dotenv

load_dotenv()

db_uri = os.environ["DB_URI"]
db_name = os.environ["DB_NAME"]

if not db_uri:
    print("DB_URI not set")
    exit(1)
if not db_name:
    print("DB_NAME not set")
    exit(1)


class Settings(BaseSettings):
    openapi_url: str = "/openapi.json"


settings = Settings()
app = FastAPI(openapi_url=settings.openapi_url)

app.include_router(
    Router.get_router(Controller(Repo(Collection(Database(db_uri, db_name), "code")))),
    prefix="/code",
    tags=["code"],
)


@app.get("/", tags=["root"])
async def read_root():
    return {"message": "Welcome to code snippet manager app!"}
