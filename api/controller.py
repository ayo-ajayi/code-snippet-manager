from json import JSONDecodeError
from fastapi import Body, HTTPException
from fastapi.encoders import jsonable_encoder
from api.exception import CodeNotFoundException, CodeUpdateFailedException
from db.model import SnippetSchema
from api.repo import Repo
from .response import ResponseModel, ErrorResponseModel
from fastapi.responses import JSONResponse


class Controller(object):
    def __init__(self, repo: Repo):
        self.repo = repo

    async def add_code(self, code: SnippetSchema = Body(...)):
        try:
            code = jsonable_encoder(code)
        except JSONDecodeError as json_decode_error:
                raise HTTPException(
                    detail=ErrorResponseModel(
                        "Invalid JSON",
                        f"There was an error decoding the JSON request: {str(json_decode_error)}",
                    ),
                    status_code=400,
                )
        try:
            new_code = await self.repo.add_code(code)
            if new_code:
                return JSONResponse(
                    content=ResponseModel(new_code, "Code added successfully."),
                    status_code=201,
                )
        except CodeNotFoundException as e:
            raise HTTPException(
                    detail=ErrorResponseModel(
                        "Code addition unsuccessful", f"{str(e)}"
                    ),
                    status_code=400,
                )
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=ErrorResponseModel(
                    "An error occurred",
                    f"There was an error adding the code: {str(e)}",
                ),
            )


    async def get_codes(self):
        try:
            codes = await self.repo.get_codes()
            if codes:
                return JSONResponse(
                    content=ResponseModel(codes, "Codes data retrieved successfully."),
                    status_code=200,
                )
            return JSONResponse(
                content=ResponseModel(codes, "Empty list returned."), status_code=200
            )
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=ErrorResponseModel(
                    "An error occurred",
                    f"There was an error retrieving the codes: {str(e)}",
                ),
            )
        
    async def get_code(self, id):
        try:
            code = await self.repo.get_code(id)
            if code:
                return JSONResponse(
                    content=ResponseModel(code, "Code data retrieved successfully."),
                    status_code=200,
                )
        except CodeNotFoundException as e:
            raise HTTPException(
            status_code=404, detail=ErrorResponseModel("not found", "code not found.")
        )

        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=ErrorResponseModel(
                    "An error occurred",
                    f"There was an error retrieving the code: {str(e)}",
                ),
            )

    async def update_code(self, id: str, data: dict):
        try:
            data = {k: v for k, v in data.items() if v is not None}
            code = await self.repo.update_code(id, data)
            if code:
                return JSONResponse(
                    content=ResponseModel(code, "Code updated successfully."),
                    status_code=200,
                )
        
        except CodeNotFoundException as e:
            raise HTTPException(
                status_code=404,
                detail=ErrorResponseModel(
                    "Code not found", "The specified code ID does not exist."
                ),
            )
        except CodeUpdateFailedException as e:
            raise HTTPException(
                status_code=400,
                detail=ErrorResponseModel(
                    "Code update failed", "There was an error updating the code."
                ),
            )
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=ErrorResponseModel(
                    "An error occurred",
                    f"There was an error updating the code: {str(e)}",
                ),
            )

    async def delete_code(self, id: str):
        try:
            code = await self.repo.delete_code(id)
            if code:
                return JSONResponse(
                    content=ResponseModel(code, "Code deleted successfully."),
                    status_code=200,
                )
        except CodeNotFoundException as e:
            raise HTTPException(
                status_code=404,
                detail=ErrorResponseModel(
                    "Code not found", "The specified code ID does not exist."
                ),
            )
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=ErrorResponseModel(
                    "An error occurred",
                    f"There was an error deleting the code: {str(e)}",
                ),
            )
