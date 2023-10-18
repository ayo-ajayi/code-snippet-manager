from fastapi import APIRouter, Body
from db.model import SnippetSchema

from .controller import Controller


class Router:
    @classmethod
    def get_router(cls, controller: Controller):
        router = APIRouter()

        @router.post("/")
        async def add_code(code: SnippetSchema = Body(...)):
            res = await controller.add_code(code)
            return res

        @router.get("/")
        async def get_codes():
            res = await controller.get_codes()
            return res

        @router.get("/{id}")
        async def get_code(id):
            res = await controller.get_code(id)
            return res

        return router
