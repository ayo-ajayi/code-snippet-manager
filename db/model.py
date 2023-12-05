from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field



class SnippetSchema(BaseModel):
    title: str = Field(...)
    code: str = Field(...)
    language: str = Field(...)
    tags: str = Field(...)
    favorite: bool = Field(default=False)
    createdAt: datetime = Field(default=datetime.isoformat(datetime.utcnow()))
    updatedAt: datetime = Field(default=datetime.isoformat(datetime.utcnow()))

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Printing helloworld in Haskell",
                "code": "print('Hello World')",
                "language": "Haskell",
                "tags": "Haskell,Hello World",
                "favorite": False,
                "createdAt": datetime.isoformat(datetime.utcnow()),
                "updatedAt": datetime.isoformat(datetime.utcnow()),
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
                "title": "Printing helloworld in Java",
                "code": "print('Hello World my dear kids')",
                "language": "Java",
                "tags": "Java,Hello World",
                "favorite": True,
                "updatedAt": datetime.isoformat(datetime.utcnow()),
            }
        }
