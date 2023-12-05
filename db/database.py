import motor.motor_asyncio


class Database:
    def __init__(self, db_uri: str, db_name: str):
        try:
            client = motor.motor_asyncio.AsyncIOMotorClient(db_uri)
            self.client = client[db_name]
            print(f"Connected to database: {self.client.name}")
        except Exception as e:
            raise ConnectionError(f"Could not connect to database: {e}")

class Collection:
    def __init__(self, database_instance: Database, collection_name: str):
        self.db = database_instance
        self.collection_name = collection_name
        self.collection = self.db.client[collection_name]
