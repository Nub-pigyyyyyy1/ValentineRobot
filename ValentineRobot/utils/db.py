# below code is taken from USERGE-X repo
# idk who wrote it 


__all__ = ['get_collection']

import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from motor.core import AgnosticClient, AgnosticDatabase, AgnosticCollection
from ValentineRobot import MONGO_DB_URI as DB_URL

print("Connecting to Database ...")

_MGCLIENT: AgnosticClient = AsyncIOMotorClient(DB_URL)
_RUN = asyncio.get_event_loop().run_until_complete

if "Valentine" in _RUN(_MGCLIENT.list_database_names()):
    print("Valentine Database Found :) => Now Logging to it...")
else:
    print("Valentine Database Not Found :( => Creating New Database...")

_DATABASE: AgnosticDatabase = _MGCLIENT["Valentine"]


def get_collection(name: str) -> AgnosticCollection:
    """ Create or Get Collection from your database """
    return _DATABASE[name]


def _close_db() -> None:
    _MGCLIENT.close()
