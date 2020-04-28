from discord.ext import commands
import aiohttp
import json
import pandas as pd
import discord


class GetClass:
    with open('./resources/classes.json', 'r') as file:
        spells = json.load(file)
    spells_data_frame = pd.DataFrame(spells, columns=['name', 'url'])

    @classmethod
    async def _get_request(cls, url):
        """ Sends a request for the json """

        url += "/"  # needed for trailing /
        async with aiohttp.ClientSession() as sess:
            async with sess.get(url) as resp:
                if resp.status != 200:
                    print(resp.status)
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
    async def get_class(cls, search: str):
        """ Search and filter out a class_ from the list """
        results: list = cls._search_list(search)
        if len(results) != 0:
            exact = cls._filter_exact(search, results)
            if exact is not None:
                data = exact
            else:
                data = results[0]
            return await cls._get_request(data['url'])
        else:
            return None


class Classes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def classes(self, ctx, class_: str):
        """ Gets a class_ either from database or site """

        class_data = await GetClass.get_class(class_.capitalize())

        embed = discord.Embed(title=class_data['name'], color=self.bot.colour)
        embed.set_author(name=f"{ctx.message.author.name}", icon_url=ctx.message.author.avatar_url)

        embed.set_footer(text="The Innkeeper, Powered by CF8, ran by the community.")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Classes(bot))
