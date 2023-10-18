from fastapi import Body, HTTPException
from fastapi.encoders import jsonable_encoder
from db.model import SnippetSchema
from api.repo import Repo
from .response import ResponseModel, ErrorResponseModel
from fastapi.responses import JSONResponse


class Controller(object):
    def __init__(self, repo: Repo):
        self.repo = repo

    async def add_code(self, code: SnippetSchema = Body(...)):
        code = jsonable_encoder(code)
        new_code = await self.repo.add_code(code)
        if new_code:
            return JSONResponse(
                content=ResponseModel(new_code, "Code added successfully."),
                status_code=201,
            )
        raise HTTPException(
            detail=ErrorResponseModel(
                "An error occurred.", "Code addition unsuccessful"
            ),
            status_code=400,
        )

    async def get_codes(self):
        codes = await self.repo.get_codes()
        if codes:
            return JSONResponse(
                content=ResponseModel(codes, "Codes data retrieved successfully."),
                status_code=200,
            )
        return JSONResponse(
            content=ResponseModel(codes, "Empty list returned."), status_code=200
        )

    async def get_code(self, id):
        code = await self.repo.get_code(id)
        if code:
            return JSONResponse(
                content=ResponseModel(code, "Code data retrieved successfully."),
                status_code=200,
            )
        raise HTTPException(
            status_code=404, detail=ErrorResponseModel("not found", "code not found.")
        )
