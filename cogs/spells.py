from discord.ext import commands
import bs4
import aiohttp
import re
import pandas as pd

dict_of_spells = [['test', 'https://k-is-geyh.com/'],
                  ['lol', 'https://k-is-geyh.com/'],
                  ['k', 'https://k-is-geyh.com/'],
                  ['gayyy', 'https://k-is-geyh.com/']]


class GetSpells:
    spells_data_frame = pd.DataFrame(dict_of_spells, columns=['name', 'url'])

    @classmethod
    async def _get_request(cls, url):
        async with aiohttp.ClientSession() as sess:
            async with sess.get(url) as resp:
                if resp != 200:
                    return False
                else:
                    return await resp.text()

    @classmethod
    async def _search_list(cls, keywords: list):
        pass

    @classmethod
    async def get_spell(cls, keywords: list):
        pass


class Spells(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def spell(self, ctx, args: list):
        """ Gets a spell either from database or site """

        await ctx.send(f"K man gay also his spell is: {args}")

def setup(bot):
    bot.add_cog(Spells(bot))
