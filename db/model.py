from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SnippetSchema(BaseModel):
    title: str = Field(...)
    code: str = Field(...)
    language: str = Field(...)
    tags: str = Field(...)
    favorite: bool = Field(default=False)
    createdAt: datetime = Field(default=datetime.now())
    updatedAt: datetime = Field(default=datetime.now())

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Printing helloworld in Haskell",
                "code": "print('Hello World')",
                "language": "Haskell",
                "tags": "Haskell,Hello World",
                "favorite": False,
                "createdAt": datetime.now(),
                "updatedAt": datetime.now(),
            }
        }


class UpdateSnippetModel(BaseModel):
    title: str = Optional[str]
    code: str = Optional[str]
    language: str = Optional[str]
    tags: str = Optional[str]
    favorite: bool = Optional[bool]
    updatedAt: datetime = Optional[datetime]

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Printing helloworld in Haskell",
                "code": "print('Hello World my dear kids')",
                "language": "Haskell",
                "tags": "Haskell,Hello World",
                "favorite": True,
                "updatedAt": datetime.now(),
            }
        }
