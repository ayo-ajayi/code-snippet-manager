import motor.motor_asyncio


class Database(object):
    def __init__(self, db_uri: str, db_name: str):
        self.db_uri = db_uri
        self.db_name = db_name
        try:
            self.client = motor.motor_asyncio.AsyncIOMotorClient(self.db_uri)[
                self.db_name
            ]
        except Exception as e:
            raise ConnectionError(f"Could not connect to database: {str(e)}")
        print(f"Connected to database: {self.client.name}")


class Collection(object):
    def __init__(self, database_instance: Database, collection_name: str):
        self.db = database_instance
        self.collection_name = collection_name
        self.collection = self.db.client[self.collection_name]
