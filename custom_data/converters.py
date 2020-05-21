import asyncio
import aiohttp
import pymongo


class MongoDatabase:
    def __init__(self, host):
        self.client = pymongo.MongoClient(host)


class CustomSpells:
    def __init__(self, user_id):
        self.user_id = user_id
        self.spell_df = None
