import asyncio
import os

import motor.motor_asyncio


class Database:
    def __int__(self):
        mongo_url = os.getenv("MONGO_URL", "mongodb://localhost:27017")
        self._client = motor.motor_asyncio.AsyncIOMotorClient(mongo_url)
        self._collection = self._client.files_db.verdicts

    async def insert_data(self, data):
        await self._collection.insert_one(dict(data))

    async def find_data(self, key):
        return await self._collection.find_one({"hash": key})
