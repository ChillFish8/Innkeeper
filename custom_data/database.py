import asyncio
import aiohttp
import pymongo
import json
import logging
import pandas as pd
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import concurrent.futures


class Settings:
    bot = None

    @classmethod
    def get_config_default(cls) -> dict:
        return {
            'prefix': '?',
            'premium': False
        }


class MongoDatabase:
    with open(r'config.json', 'r') as file:
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

        self.db = self.client["TheInnkeeperProject"]

        # custom content
        self.user_spells = self.db["TheInnkeeper-Spells"]
        self.user_races = self.db["TheInnkeeper-Races"]
        self.user_monsters = self.db["TheInnkeeper-Monsters"]

        # custom guild configs
        self.guild_configs = self.db["TheInnkeeper-Guilds"]

    def close_conn(self):
        self.db.logout()

    """ Custom Guild settings """
    def set_guild_config(self, guild_id: int, config: dict) -> [dict, int]:
        current_data = self.guild_configs.find_one({'_id': guild_id})
        logging.log(
            logging.DEBUG, "SET-GUILD: Guild with Id: {} returned with results: {}".format(guild_id, current_data))

        if current_data is not None:
            QUERY = {'_id': guild_id}
            new_data = {'config': config}
            resp = self.guild_configs.update_one(QUERY, {'$set': new_data})
            logging.log(logging.INFO, "Data updated area with GuildId: {},\n"
                                      "      resp: {}\n".format(guild_id, resp.raw_result))
            return resp.raw_result
        else:
            data = {'_id': guild_id, 'config': config}
            resp = self.guild_configs.insert_one(data)
            logging.log(logging.INFO, "Data inserted into area with GuildId: {},\n"
                                      "      resp: {}\n".format(guild_id, {'_id': resp.inserted_id,
                                                                           'complete': resp.acknowledged}))
            return resp.inserted_id

    def reset_guild_config(self, guild_id: int):
        current_data = self.guild_configs.find_one_and_delete({'_id': guild_id})
        logging.log(
            logging.DEBUG, "DELETE-GUILD: Guild with Id: {} returned with results: {}".format(guild_id, current_data))
        return "COMPLETE"

    def get_guild_config(self, guild_id: int) -> dict:
        current_data = self.guild_configs.find_one({'_id': guild_id})
        logging.log(
            logging.DEBUG, "GET-GUILD:  Guild with Id: {} returned with results: {}".format(guild_id, current_data))
        return current_data['config'] if current_data is not None else Settings.get_config_default()

    """ User's custom spells url storage and monitoring """
    def add_user_spells(self, user_id: int, url: str) -> [dict, int]:
        current_data = self.user_spells.find_one({'_id': user_id})
        logging.log(logging.DEBUG, "ADD-SPELLS: User with Id: {} returned with results: {}".format(
            user_id, current_data))
        if current_data is not None:
            urls = current_data['urls']
            urls.append({'url': url})
            resp = self.user_spells.update_one({'_id': user_id}, {'$set': {'urls': urls}})
            logging.log(logging.INFO, "Data updated area with UserId: {},\n"
                                      "      resp: {}\n".format(user_id, resp.raw_result))
            return resp.raw_result
        else:
            data = {'_id': user_id, 'urls': [{'url': url}]}
            resp = self.user_spells.insert_one(data)
            logging.log(logging.INFO, "Data inserted into area with UserId: {},\n"
                                      "      resp: {}\n".format(user_id,
                                                                {'_id': resp.inserted_id,
                                                                 'complete': resp.acknowledged}))
            return resp.inserted_id

    def update_user_spells(self, user_id: int, spells_urls: list) -> [dict, str]:
        resp = self.user_spells.find_one_and_update({"_id": user_id}, {'$set': {'urls': spells_urls}})
        logging.log(logging.INFO, "Data updated area with UserId: {},\n"
                                  "      resp: {}\n".format(user_id, resp.raw_result))
        return resp.raw_result

    def get_user_spells(self, user_id: int) -> [dict, None]:
        current_data = self.user_spells.find_one({'_id': user_id})
        logging.log(logging.DEBUG, "GET-SPELLS: User with Id: {} returned with results: {}".format(user_id,
                                                                                                   current_data))
        return current_data

    def reset_all_user_spells(self, user_id: int):
        current_data = self.user_spells.find_one_and_delete({'_id': user_id})
        logging.log(
            logging.DEBUG,
            "DELETE-ALL-SPELLS: User with Id: {} returned with results: {}".format(user_id, current_data))
        return "COMPLETE"

    """ Custom Races """
    def add_user_races(self, user_id: int, name: str, url: str) -> [dict, int]:
        current_data = self.user_races.find_one({'_id': user_id})
        logging.log(logging.DEBUG, "ADD-RACES: User with Id: {} returned with results: {}".format(
            user_id, current_data))
        if current_data is not None:
            urls = current_data['urls']
            urls.append({'url': url})
            resp = self.user_races.update_one({'_id': user_id}, {'$set': {'urls': urls}})
            logging.log(logging.INFO, "Data updated area with UserId: {},\n"
                                      "      resp: {}\n".format(user_id, resp.raw_result))
            return resp.raw_result
        else:
            data = {'_id': user_id, 'urls': [{'url': url}]}
            resp = self.user_races.insert_one(data)
            logging.log(logging.INFO, "Data inserted into area with UserId: {},\n"
                                      "      resp: {}\n".format(user_id,
                                                                {'_id': resp.inserted_id,
                                                                 'complete': resp.acknowledged}))
            return resp.inserted_id

    def remove_user_races(self, user_id: int, url: str):
        def check(value):
            return not value['url'] == url

        current_data = self.user_races.find_one({'_id': user_id})
        logging.log(logging.DEBUG,
                    "REMOVE-RACES: User with Id: {} returned with results: {}".format(user_id, current_data))
        if current_data is not None:
            urls = current_data['urls']
            urls = list(filter(check, urls))
            resp = self.user_races.update_one({'_id': user_id}, {'$set': {'urls': urls}})
            logging.log(logging.INFO, "Data updated area with UserId: {},\n"
                                      "      resp: {}\n".format(user_id, resp.raw_result))
            return resp.raw_result
        else:
            return "NO-SPELLS"

    def get_user_races(self, user_id: int) -> [dict, None]:
        current_data = self.user_races.find_one({'_id': user_id})
        logging.log(logging.DEBUG, "GET-RACES: User with Id: {} returned with results: {}".format(user_id,
                                                                                                  current_data))
        return current_data

    def reset_all_user_races(self, user_id: int):
        current_data = self.user_races.find_one_and_delete({'_id': user_id})
        logging.log(
            logging.DEBUG,
            "DELETE-ALL-RACES: User with Id: {} returned with results: {}".format(user_id, current_data))
        return "COMPLETE"

    """ Custom Monsters """
    def add_user_monsters(self, user_id: int, name: str, url: str) -> [dict, int]:
        current_data = self.user_monsters.find_one({'_id': user_id})
        logging.log(logging.DEBUG, "ADD-MONSTER: User with Id: {} returned with results: {}".format(
            user_id, current_data))
        if current_data is not None:
            urls = current_data['urls']
            urls.append({'name': name, 'url': url})
            resp = self.user_monsters.update_one({'_id': user_id}, {'$set': {'urls': urls}})
            logging.log(logging.INFO, "Data updated area with UserId: {},\n"
                                      "      resp: {}\n".format(user_id, resp.raw_result))
            return resp.raw_result
        else:
            data = {'_id': user_id, 'urls': [{'name': name, 'url': url}]}
            resp = self.user_monsters.insert_one(data)
            logging.log(logging.INFO, "Data inserted into area with UserId: {},\n"
                                      "      resp: {}\n".format(user_id,
                                                                {'_id': resp.inserted_id,
                                                                 'complete': resp.acknowledged}))
            return resp.inserted_id

    def remove_user_monsters(self, user_id: int, name: str):
        def check(value):
            return not value['name'] == name

        current_data = self.user_monsters.find_one({'_id': user_id})
        logging.log(logging.DEBUG,
                    "REMOVE-MONSTER: User with Id: {} returned with results: {}".format(user_id, current_data))
        if current_data is not None:
            urls = current_data['urls']
            urls = list(filter(check, urls))
            resp = self.user_monsters.update_one({'_id': user_id}, {'$set': {'urls': urls}})
            logging.log(logging.INFO, "Data updated area with UserId: {},\n"
                                      "      resp: {}\n".format(user_id, resp.raw_result))
            return resp.raw_result
        else:
            return "NO-SPELLS"

    def get_user_monsters(self, user_id: int) -> [dict, None]:
        current_data = self.user_monsters.find_one({'_id': user_id})
        logging.log(logging.DEBUG, "GET-MONSTER: User with Id: {} returned with results: {}".format(user_id,
                                                                                                  current_data))
        return current_data

    def reset_all_user_monsters(self, user_id: int):
        current_data = self.user_monsters.find_one_and_delete({'_id': user_id})
        logging.log(
            logging.DEBUG,
            "DELETE-ALL-MONSTERS: User with Id: {} returned with results: {}".format(user_id, current_data))
        return "COMPLETE"


class GuildConfig:
    def __init__(self, guild_id, database=None):
        self.guild_id = guild_id
        self._db = db if database is None else database
        data = self._db.get_guild_config(guild_id=guild_id)

        self.prefix = data.pop('prefix', '?')  # Emergency safe guard
        self.premium = data.pop('premium', False)  # Emergency safe guard

    def set_prefix(self, new_prefix):
        self.prefix = new_prefix
        self._db.set_guild_config(self.guild_id, config={'prefix': self.prefix, 'premium': self.premium})
        return self.prefix

    def reset_prefix(self):
        self._db.reset_guild_config(self.guild_id)
        return Settings.get_config_default().pop('prefix')


class CustomSpells:
    def __init__(self, user_id, database=None):
        self.user_id = user_id
        self._db = db if database is None else database
        self.data = self._db.get_user_spells(user_id=user_id)
        self.spells_data_frame = None
        self.downloader = asyncio.get_event_loop().create_task(self.load_spells_background())
        self._cache_complete = False
        self._can_page = False
        self._error_code = 200

    async def _process_folder(self, folder_urls: list) -> list:
        def mapper(value):
            return value['webContentLink']

        def wrapper(urls_):
            results = []
            for folder_url in urls_:
                result, status = DriveControl.get_files(folder_url['url'])
                if not status:
                    self._error_code = result
                else:
                    results.append(*list(map(mapper, result)))
            return results

        with concurrent.futures.ThreadPoolExecutor() as pool:
            urls = await asyncio.get_event_loop().run_in_executor(pool, wrapper, folder_urls)
        return urls

    async def load_spells_background(self) -> None:
        temp = []
        if self.data is not None:
            folder_urls_to_process = self.data.pop('urls')
            urls_to_process = await self._process_folder(folder_urls_to_process)

            def append_to(value: dict):
                if 'name' not in value:
                    return {'null': None}
                data = {'name': value['name'], 'data': value}
                return data

            async with aiohttp.ClientSession() as sess:
                for url_data in urls_to_process:
                    async with sess.get(url_data) as resp:
                        if resp.status == 200:
                            spell_data = await resp.text()
                            spell_data = json.loads(spell_data)
                            sec = list(map(append_to, spell_data))
                            temp.append(*sec)
                            self.spells_data_frame = pd.DataFrame(temp, columns=['name', 'data'])
                            self._can_page = True
        self.spells_data_frame = pd.DataFrame(temp, columns=['name', 'data'])
        self._can_page = True
        self._cache_complete = True

    async def wait_for_full(self) -> None:
        while not self._cache_complete:
            await asyncio.sleep(0.25)
        return

    async def wait_for_chunk(self) -> None:
        while not self._can_page:
            await asyncio.sleep(0.25)
        return

    @property
    def cache_complete(self) -> bool:
        return self._cache_complete

    @property
    def can_page(self)  -> bool:
        return self._can_page


class DriveControl:
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()

    @classmethod
    def get_id_by_url(cls, url: str) -> [str, int]:
        if url.startswith('https://drive.google.com/drive/folders/') or\
                url.startswith("https://drive.google.com/open?id="):
            return url.strip('?usp=sharing')\
                .strip('https://drive.google.com/drive/folders/')\
                .strip("https://drive.google.com/open?id=")
        elif url.startswith('http://'):
            return 1
        elif "drive.google.com/drive/folders" not in url:
            return 2
        else:
            return 3

    @classmethod
    def get_files(cls, url: str) -> [str, list]:
        id_ = cls.get_id_by_url(url)
        if id_ == 1:
            return "You have not parsed a secure link.", False
        elif id_ == 1:
            return "You have not parsed a google drive folder link.", False
        elif id_ == 1:
            return "You have parsed a incorrect url format.", False
        else:
            drive = GoogleDrive(cls.gauth)
            file_list = drive.ListFile({'q': f"'{id_}' in parents and trashed=false"}).GetList()
            return file_list, True


def setup(bot):
    Settings.bot = bot


async def main():
    spell = CustomSpells(1234)
    await asyncio.wait_for(spell.wait_for_chunk(), timeout=5)
    print(spell.spells_data_frame)
    await asyncio.wait_for(spell.wait_for_full(), timeout=5)
    print(spell.spells_data_frame)

if __name__ == "__main__":
    db = MongoDatabase()
    asyncio.run(main())
