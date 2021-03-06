import aiohttp
import asyncio
import concurrent.futures
import discord
import json
import logging
import pandas as pd
import pymongo
from discord.ext import commands
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive


class Settings:
    bot = None

    @classmethod
    def get_config_default(cls) -> dict:
        return {
            'prefix': '?',
            'premium': False
        }


class SpellsDoc:
    """ User's custom spells url storage and monitoring """

    def __init__(self, db):
        self.db = db
        self.user_spells = self.db["TheInnkeeper-Spells"]

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


class RacesDoc:
    """ Custom Races """

    def __init__(self, db):
        self.db = db
        self.user_races = self.db["TheInnkeeper-Races"]

    def add_user_races(self, user_id: int, url: str) -> [dict, int]:
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

    def update_user_races(self, user_id: int, spells_urls: list) -> [dict, str]:
        resp = self.user_races.find_one_and_update({"_id": user_id}, {'$set': {'urls': spells_urls}})
        logging.log(logging.INFO, "Data updated area with UserId: {},\n"
                                  "      resp: {}\n".format(user_id, resp.raw_result))
        return resp.raw_result

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


class MonsterDoc:
    """ Custom Monsters """

    def __init__(self, db):
        self.db = db
        self.user_monsters = self.db["TheInnkeeper-Monsters"]

    def add_user_monsters(self, user_id: int, url: str) -> [dict, int]:
        current_data = self.user_monsters.find_one({'_id': user_id})
        logging.log(logging.DEBUG, "ADD-MONSTERS: User with Id: {} returned with results: {}".format(
            user_id, current_data))
        if current_data is not None:
            urls = current_data['urls']
            urls.append({'url': url})
            resp = self.user_monsters.update_one({'_id': user_id}, {'$set': {'urls': urls}})
            logging.log(logging.INFO, "Data updated area with UserId: {},\n"
                                      "      resp: {}\n".format(user_id, resp.raw_result))
            return resp.raw_result
        else:
            data = {'_id': user_id, 'urls': [{'url': url}]}
            resp = self.user_monsters.insert_one(data)
            logging.log(logging.INFO, "Data inserted into area with UserId: {},\n"
                                      "      resp: {}\n".format(user_id,
                                                                {'_id': resp.inserted_id,
                                                                 'complete': resp.acknowledged}))
            return resp.inserted_id

    def update_user_monsters(self, user_id: int, spells_urls: list) -> [dict, str]:
        resp = self.user_monsters.find_one_and_update({"_id": user_id}, {'$set': {'urls': spells_urls}})
        logging.log(logging.INFO, "Data updated area with UserId: {},\n"
                                  "      resp: {}\n".format(user_id, resp.raw_result))
        return resp.raw_result

    def get_user_monsters(self, user_id: int) -> [dict, None]:
        current_data = self.user_monsters.find_one({'_id': user_id})
        logging.log(logging.DEBUG, "GET-MONSTERS: User with Id: {} returned with results: {}".format(user_id,
                                                                                                     current_data))
        return current_data

    def reset_all_user_monsters(self, user_id: int):
        current_data = self.user_monsters.find_one_and_delete({'_id': user_id})
        logging.log(
            logging.DEBUG,
            "DELETE-ALL-MONSTERS: User with Id: {} returned with results: {}".format(user_id, current_data))
        return "COMPLETE"


class GuildData:
    """ Custom Guild settings """

    def __init__(self, db):
        self.db = db
        self.guild_configs = self.db["TheInnkeeper-Guilds"]

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


class MongoDatabase(GuildData):
    """
    This is the main Mongo DB class, this pull data from config.json and
    connects to the remote mongoDB (Falls back to local host if config missing)

    + Class Inherits:
        - SpellsDoc Class
        - RacesDoc Class
        - MonsterDoc Class
        - GuildData Class
    """
    with open(r'config.json', 'r') as file:
        config = json.load(file)

    def __init__(self):
        """
        This method requires no parameters, It takes all data from the
        class var `config`, if data is missing from config it falls
        back to the following settings:

        + host: localhost
        + port: 27017
        + user: root
        + password: root
        """
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
        super().__init__(self.db)

    def close_conn(self):
        """ Logs us out of the database """
        self.db.logout()


class GuildConfig:
    """
        Object representing a guild's custom settings, this system can
        be modified to expand settings as an when they are needed (relies on Settings Class).

        This also handles all DB interactions and self contains it.

        :returns GuildConfig object:
    """

    def __init__(self, guild_id, database=None):
        """
        :param guild_id:
        :param database: -> Optional

        If database is None it falls back to a global var,
        THIS ONLY EXISTS WHEN RUNNING THE FILE AS MAIN!

        On creation the class calls the database getting the guild settings
        if prefix is None it reverts back to `?`, this should never happen
        under normal circumstances.
        Premium by default is False and will default to False in case of
        failure.
        """
        self.guild_id = guild_id
        self._db = db if database is None else database
        data = self._db.get_guild_config(guild_id=guild_id)

        self.prefix = data.pop('prefix', '?')  # Emergency safe guard
        self.premium = data.pop('premium', False)  # Emergency safe guard

    def set_prefix(self, new_prefix) -> str:
        """
        This function sets it's own attr to the new prefix then
        calls the db setting the new prefix from it's attr to avoid desync

        :returns prefix:
        """
        self.prefix = new_prefix
        self._db.set_guild_config(self.guild_id, config={'prefix': self.prefix, 'premium': self.premium})
        return self.prefix

    def reset_prefix(self) -> str:
        """
        resets guild config on db.
        :returns default_prefix:
        """
        self._db.reset_guild_config(self.guild_id)
        return Settings.get_config_default().pop('prefix')


class CustomSpells:
    """
    Object representing the user's custom spells (Part of custom Content)
    this manages interactions with the database and processing the data.

    - When this object is created it creates a background task to cache all the content
    in a folder provided by the user (GDrive).

    - can_page Returns True when it has cached the first file.
    - cache_complete Returns True when every file has been cached.

    :returns CustomRaces Object
    """

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
    def can_page(self) -> bool:
        return self._can_page

    async def get_list(self, ctx: commands.Context, bot) -> list:
        all_races = self.spells_data_frame.to_dict('r')
        pages, remaining = divmod(len(all_races), 10)
        amount_of_pages = pages + (1 if remaining else 0)
        embed_list_output, i, spells_done = [], 0, 0

        for i in range(0, pages, 10):
            embed = discord.Embed(color=bot.colour)
            embed.set_author(
                name=f"{ctx.author.name}'s Custom Spell Page {i + 1}/{amount_of_pages}",
                icon_url=ctx.author.avatar_url)
            for si in range(i, i + 10):
                embed.add_field(name="\u200b", value=f"\u200b**{si + 1}) - {all_races[si]['name']}**", inline=False)
                spells_done += 1
            embed.set_footer(text="Custom content commands part of The Innkeeper, Powered by CF8")
            embed_list_output.append(embed)

        if remaining:
            embed = discord.Embed(color=bot.colour)
            embed.set_author(
                name=f"{ctx.author.name}'s Custom Spell Page {i + 1}/{amount_of_pages}",
                icon_url=ctx.author.avatar_url)
            for si in range(remaining + spells_done):
                embed.add_field(
                    name="\u200b",
                    value=f"\u200b**{si + 1}) - {all_races[si]['name']}**",
                    inline=False)
            embed.set_footer(text="Custom content commands part of The Innkeeper, Powered by CF8")
            embed_list_output.append(embed)
        return embed_list_output

    def _search_list(self, search: str):
        """ The heavy lifter, pandas searches the frame for matches """
        results: pd.DataFrame = self.spells_data_frame[
            self.spells_data_frame['name'].str.contains(search)]
        data: dict = results.to_dict(orient='index')
        return list(data.values())

    @staticmethod
    def _filter_exact(spell_exact, results):
        """ Filter the result if it has an exact match """
        for spell in results:
            if spell['name'] == spell_exact:
                return spell
        return None

    @staticmethod
    def _get_result_embed(ctx, bot, content):
        pass

    async def search(self, ctx, bot, query_string):
        results: list = self._search_list(query_string)
        if len(results) != 0:
            exact = self._filter_exact(query_string, results)
            if exact is not None:
                data = exact
            else:
                data = results[0]
            return self._get_result_embed(ctx, bot, data['data'])
        else:
            attempt_2: list = self._search_list(query_string[0])  # lets get the first term and see
            if len(attempt_2) > 0:
                text = f"**Maybe you were looking for:**\n"
                text += '\n'.join([f"**•** `{item['name']}`" for item in attempt_2[:5]])

                embed = discord.Embed(color=bot.colour)
                embed.set_author(name="Oops! I cant find anything with that search term.",
                                 icon_url="https://cdn.discordapp.com/emojis/704784002166554776.png?v=1")
                embed.description = text

            else:
                embed = discord.Embed(color=bot.colour)
                embed.set_author(name="Oops! I cant find any results relating to your search.",
                                 icon_url="https://cdn.discordapp.com/emojis/704784002166554776.png?v=1")
            return embed


class CustomRaces:
    """
    Object representing the user's custom races (Part of custom Content)
    this manages interactions with the database and processing the data.

    - When this object is created it creates a background task to cache all the content
    in a folder provided by the user (GDrive).

    - can_page Returns True when it has cached the first file.
    - cache_complete Returns True when every file has been cached.

    :returns CustomRaces Object
    """

    def __init__(self, user_id, database=None):
        self.user_id = user_id
        self._db = db if database is None else database
        self.data = self._db.get_user_races(user_id=user_id)
        self.races_data_frame = None
        self.downloader = asyncio.get_event_loop().create_task(self.load_races_background())
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

    async def load_races_background(self) -> None:
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
                            races_data = await resp.text()
                            races_data = json.loads(races_data)
                            sec = list(map(append_to, races_data))
                            temp.append(*sec)
                            self.races_data_frame = pd.DataFrame(temp, columns=['name', 'data'])
                            self._can_page = True
        self.races_data_frame = pd.DataFrame(temp, columns=['name', 'data'])
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
    def can_page(self) -> bool:
        return self._can_page

    async def get_list(self, ctx: commands.Context, bot) -> list:
        all_races = self.races_data_frame.to_dict('r')
        pages, remaining = divmod(len(all_races), 10)
        amount_of_pages = pages + (1 if remaining else 0)
        embed_list_output, i, spells_done = [], 0, 0

        for i in range(0, pages, 10):
            embed = discord.Embed(color=bot.colour)
            embed.set_author(
                name=f"{ctx.author.name}'s Custom Races Page {i + 1}/{amount_of_pages}",
                icon_url=ctx.author.avatar_url)
            for si in range(i, i + 10):
                embed.add_field(name="\u200b", value=f"\u200b**{si + 1}) - {all_races[si]['name']}**", inline=False)
                spells_done += 1
            embed.set_footer(text="Custom content commands part of The Innkeeper, Powered by CF8")
            embed_list_output.append(embed)

        if remaining:
            embed = discord.Embed(color=bot.colour)
            embed.set_author(
                name=f"{ctx.author.name}'s Custom Races Page {i + 1}/{amount_of_pages}",
                icon_url=ctx.author.avatar_url)
            for si in range(remaining + spells_done):
                embed.add_field(
                    name="\u200b",
                    value=f"\u200b**{si + 1}) - {all_races[si]['name']}**",
                    inline=False)
            embed.set_footer(text="Custom content commands part of The Innkeeper, Powered by CF8")
            embed_list_output.append(embed)
        return embed_list_output

    def _search_list(self, search: str):
        """ The heavy lifter, pandas searches the frame for matches """
        results: pd.DataFrame = self.races_data_frame[
            self.races_data_frame['name'].str.contains(search)]
        data: dict = results.to_dict(orient='index')
        return list(data.values())

    @staticmethod
    def _filter_exact(spell_exact, results):
        """ Filter the result if it has an exact match """
        for spell in results:
            if spell['name'] == spell_exact:
                return spell
        return None

    @staticmethod
    def _get_result_embed(ctx, bot, content):
        pass

    async def search(self, ctx, bot, query_string):
        results: list = self._search_list(query_string)
        if len(results) != 0:
            exact = self._filter_exact(query_string, results)
            if exact is not None:
                data = exact
            else:
                data = results[0]
            return self._get_result_embed(ctx, bot, data['data'])
        else:
            attempt_2: list = self._search_list(query_string[0])  # lets get the first term and see
            if len(attempt_2) > 0:
                text = f"**Maybe you were looking for:**\n"
                text += '\n'.join([f"**•** `{item['name']}`" for item in attempt_2[:5]])

                embed = discord.Embed(color=bot.colour)
                embed.set_author(name="Oops! I cant find anything with that search term.",
                                 icon_url="https://cdn.discordapp.com/emojis/704784002166554776.png?v=1")
                embed.description = text

            else:
                embed = discord.Embed(color=bot.colour)
                embed.set_author(name="Oops! I cant find any results relating to your search.",
                                 icon_url="https://cdn.discordapp.com/emojis/704784002166554776.png?v=1")
            return embed


"""class DriveControl:
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()

    @classmethod
    def get_id_by_url(cls, url: str) -> [str, int]:
        if url.startswith('https://drive.google.com/drive/folders/') or \
                url.startswith("https://drive.google.com/open?id="):
            return url.strip('?usp=sharing') \
                .strip('https://drive.google.com/drive/folders/') \
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
            return file_list, True"""


def setup(bot):
    Settings.bot = bot


async def main():
    spell = CustomRaces(1234)
    await asyncio.wait_for(spell.wait_for_chunk(), timeout=5)
    print(spell.races_data_frame)
    await asyncio.wait_for(spell.wait_for_full(), timeout=5)
    print(spell.races_data_frame)


if __name__ == "__main__":
    # logging.basicConfig(level=logging.DEBUG)
    db = MongoDatabase()
    asyncio.run(main())
