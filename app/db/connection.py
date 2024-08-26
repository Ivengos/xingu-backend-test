import os
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.models.dummy import Dummy
from dotenv import load_dotenv

from app.models.dummy import Dummy

# load config over .env file
load_dotenv()


async def init_db():
    mongodb_url = os.getenv("MONGODB_URL")
    mongodb_name = os.getenv("MONGODB_NAME")

    client = AsyncIOMotorClient(mongodb_url)
    database = client[mongodb_name]
    await init_beanie(database=database, document_models=[Dummy])
