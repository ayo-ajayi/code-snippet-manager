from bson import ObjectId
from api.exception import CodeNotFoundException, CodeUpdateFailedException
from db.database import Collection
from .response import ResponseHelper
from datetime import datetime


class Repo(object):
    def __init__(self, collection: Collection):
        self.collection = collection.collection

    async def get_code(self, id: str) -> dict:
        code = await self.collection.find_one({"_id": ObjectId(id)})
        if code:
            return ResponseHelper(code)
        raise CodeNotFoundException("code not found")

    async def add_code(self, code: dict) -> dict:
        new_code = await self.collection.insert_one(code)
        res = await self.collection.find_one({"_id": new_code.inserted_id})
        if res:
            return ResponseHelper(res)
        raise CodeNotFoundException("code addition failed")

    async def get_codes(self) -> list:
        codes = []
        async for code in self.collection.find():
            codes.append(ResponseHelper(code))
        return codes

    async def update_code(self, id: str, data: dict):
        if len(data) < 1:
            return False
        data["updatedAt"] = datetime.isoformat(datetime.utcnow())
        code = await self.collection.find_one({"_id": ObjectId(id)})
        if code:
            updated_code = await self.collection.update_one(
                {"_id": ObjectId(id)}, {"$set": data}
            )
            if updated_code:
                return True
            raise CodeUpdateFailedException("code update failed")
        raise CodeNotFoundException("code not found")
    
    async def delete_code(self, id: str):
        code = await self.collection.find_one({"_id": ObjectId(id)})
        if code:
            await self.collection.delete_one({"_id": ObjectId(id)})
            return code
        raise CodeNotFoundException("code not found")