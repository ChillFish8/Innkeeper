import asyncio
import aiohttp
import pymongo
import json
import logging


class Settings:
    bot = None

    @classmethod
    def get_config_default(cls) -> dict:
        return {
            'prefix': '?',
            'premium': False
        }


class MongoDatabase:
    with open(r'custom_data\config.json', 'r') as file:
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
    def add_user_spells(self, user_id: int, name: str, url: str) -> [dict, int]:
        current_data = self.user_spells.find_one({'_id': user_id})
        logging.log(logging.DEBUG, "ADD-SPELLS: User with Id: {} returned with results: {}".format(
            user_id, current_data))
        if current_data is not None:
            urls = current_data['urls']
            urls.append({'name': name, 'url': url})
            resp = self.user_spells.update_one({'_id': user_id}, {'$set': {'urls': urls}})
            logging.log(logging.INFO, "Data updated area with UserId: {},\n"
                                      "      resp: {}\n".format(user_id, resp.raw_result))
            return resp.raw_result
        else:
            data = {'_id': user_id, 'urls': [{'name': name, 'url': url}]}
            resp = self.user_spells.insert_one(data)
            logging.log(logging.INFO, "Data inserted into area with UserId: {},\n"
                                      "      resp: {}\n".format(user_id,
                                                                {'_id': resp.inserted_id,
                                                                 'complete': resp.acknowledged}))
            return resp.inserted_id

    def remove_user_spells(self, user_id: int, name: str):
        def check(value):
            return not value['name'] == name

        current_data = self.user_spells.find_one({'_id': user_id})
        logging.log(logging.DEBUG,
                    "REMOVE-SPELL: User with Id: {} returned with results: {}".format(user_id, current_data))
        if current_data is not None:
            urls = current_data['urls']
            urls = list(filter(check, urls))
            resp = self.user_spells.update_one({'_id': user_id}, {'$set': {'urls': urls}})
            logging.log(logging.INFO, "Data updated area with UserId: {},\n"
                                      "      resp: {}\n".format(user_id, resp.raw_result))
            return resp.raw_result
        else:
            return "NO-SPELLS"

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
            urls.append({'name': name, 'url': url})
            resp = self.user_races.update_one({'_id': user_id}, {'$set': {'urls': urls}})
            logging.log(logging.INFO, "Data updated area with UserId: {},\n"
                                      "      resp: {}\n".format(user_id, resp.raw_result))
            return resp.raw_result
        else:
            data = {'_id': user_id, 'urls': [{'name': name, 'url': url}]}
            resp = self.user_races.insert_one(data)
            logging.log(logging.INFO, "Data inserted into area with UserId: {},\n"
                                      "      resp: {}\n".format(user_id,
                                                                {'_id': resp.inserted_id,
                                                                 'complete': resp.acknowledged}))
            return resp.inserted_id

    def remove_user_races(self, user_id: int, name: str):
        def check(value):
            return not value['name'] == name

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


def setup(bot):
    Settings.bot = bot


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    db = MongoDatabase()
