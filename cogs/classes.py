from discord.ext import commands
import aiohttp
import json
import pandas as pd
import asyncio

from resources import classes_srd
from modules import paginator


class GetClass:
    with open('./resources/classes.json', 'r') as file:
        classes = json.load(file)
    classes_data_frame = pd.DataFrame(classes, columns=['name', 'id'])
    base_classes = [
        classes_srd.Barbarian,
        classes_srd.Bard,
        classes_srd.Cleric,
        classes_srd.Druid,
        classes_srd.Fighter,
        classes_srd.Monk,
        classes_srd.Paladin,
        classes_srd.Ranger,
        classes_srd.Rogue,
        classes_srd.Sorcerer,
        classes_srd.Warlock,
        classes_srd.wizard,
    ]

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
        results: pd.DataFrame = cls.classes_data_frame[
            cls.classes_data_frame['name'].str.contains(search)]
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
    async def get_class(cls, search: str):
        """ Search and filter out a class_ from the list """
        results: list = cls._search_list(search)
        if len(results) != 0:
            data = cls._filter_exact(search, results)
            if data is None:
                data = results[0]
            if data['id'].isdigit():
                return await cls.base_classes[int(data['id']) - 1](False)
            else:
                pass  # todo add system for custom content
        else:
            text = f"<:wellfuck:704784002166554776> **Oops! I could not find anything matching that search!**\n" \
                   f"Here are the classes i can bring up:\n"
            text += '\n'.join([f"• `{item['name']}`" for item in cls.classes])
            return text


class Classes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def classes(self, ctx, class_: str):
        """ Gets a class_ either from database or site """

        if class_.isalpha():
            class_data = await GetClass.get_class(class_.capitalize())
            if isinstance(class_data, list):
                pager = paginator.Paginator(class_data, ctx.message, self.bot, self.bot.colour)
                asyncio.get_event_loop().create_task(pager.start())
            else:
                await ctx.send(class_data)
        else:
            await ctx.send(
                "<:wellfuck:704784002166554776> **Oops! I cant search for things that are not words or letters.**")

def setup(bot):
    bot.add_cog(Classes(bot))
