import asyncio
import aiohttp
import pymongo
import json


class MongoDatabase:
    with open('config.json', 'r') as file:
        config = json.load(file)

    def __init__(self):
        addr = self.config.get('host_address', 'localhost')
        port = self.config.get('port', '27017')
        usr = self.config.get('username', 'root')
        pas = self.config.get('password', 'root')
        host = f"mongodb://{usr}:{pas}@{addr}:{port}/"
        self.client = pymongo.MongoClient(host)

        system_info = self.client.server_info()
        version = system_info['version']
        git_ver = system_info['gitVersion']
        print(f"Connected to {addr}:{port} from {self.client.HOST}, Version: {version}, Git Version: {git_ver}")


class CustomSpells:
    def __init__(self, user_id):
        self.user_id = user_id
        self.spell_df = None


if __name__ == "__main__":
    db = MongoDatabase()
