from bson import ObjectId
from db.database import Collection
from .response import ResponseHelper


class Repo(object):
    def __init__(self, collection: Collection):
        self.collection = collection.collection

    async def get_code(self, id: str) -> dict:
        code = await self.collection.find_one({"_id": ObjectId(id)})
        if code:
            return ResponseHelper(code)
        return None

    async def add_code(self, code: dict) -> dict:
        new_code = await self.collection.insert_one(code)
        res = await self.collection.find_one({"_id": new_code.inserted_id})
        return ResponseHelper(res)

    async def get_codes(self) -> list:
        codes = []
        async for code in self.collection.find():
            codes.append(ResponseHelper(code))
        return codes
