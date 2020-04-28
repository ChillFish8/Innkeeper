from discord.ext import commands
import aiohttp
import json
import pandas as pd


class GetRace:
    with open('./resources/races.json', 'r') as file:
        races = json.load(file)
    spells_data_frame = pd.DataFrame(races, columns=['name', 'url'])

    @classmethod
    async def _get_request(cls, url):
        """ Sends a request for the json """

        url += "/"  # needed for trailing /
        async with aiohttp.ClientSession() as sess:
            async with sess.get(url) as resp:
                if resp.status != 200:
                    return False
                else:
                    return await resp.json()

    @classmethod
    def _search_list(cls, search: str):
        """ The heavy lifter, pandas searches the frame for matches """
        results: pd.DataFrame = cls.spells_data_frame[
            cls.spells_data_frame['name'].str.contains(search)]
        data: dict = results.to_dict(orient='index')
        return list(data.values())

    @staticmethod
    def _filter_exact(spell_exact, results):
        """ Filter the result if it has an exact match """
        for spell in results:
            if spell['name'] == spell_exact:
                return spell
        return None

    @classmethod
    async def get_race(cls, search: str):
        """ Search and filter out a class_ from the list """
        results: list = cls._search_list(search)
        if len(results) != 0:
            data = cls._filter_exact(search, results)
            if data is None:
                data = results[0]

        else:
            text = f"<:wellfuck:704784002166554776> **Oops! I could not find anything matching that search!**\n" \
                   f"Here are the classes i can bring up:\n"
            text += '\n'.join([f"• `{item['name']}`" for item in cls.races])
            return text


class Classes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def classes(self, ctx, race: str):
        """ Gets a class_ either from database or site """

        if race.isalpha():
            race_data = await GetRace.get_race(race.capitalize())


        else:
            await ctx.send(
                "<:wellfuck:704784002166554776> **Oops! I cant search for things that are not words or letters.**")

def setup(bot):
    bot.add_cog(Classes(bot))
