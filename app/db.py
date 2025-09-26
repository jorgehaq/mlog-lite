import motor.motor_asyncio
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:27017/mlog")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client.mlog