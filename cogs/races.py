from discord.ext import commands
import aiohttp
import json
import pandas as pd
import discord


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
            return data
        else:
            text = f"**Here are the races i can bring up:**\n"
            text += '\n'.join([f"**•** `{item['name']}`" for item in cls.races])
            embed = discord.Embed()
            embed.set_author(name="Oops! I cant find anything with that search term.",
                             icon_url="https://cdn.discordapp.com/emojis/704784002166554776.png?v=1")
            embed.description = text
            return embed


class Classes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def race(self, ctx, race: str):
        """ Gets a class_ either from database or site """

        if not race.isalpha():
            embed = discord.Embed(color=self.bot.colour)
            embed.set_author(name="Oops! I cant search for things that are not words or letters.",
                             icon_url="https://cdn.discordapp.com/emojis/704784002166554776.png?v=1")
            return await ctx.send(embed=embed)

        race_data: (str, dict) = await GetRace.get_race(race.capitalize())
        if not isinstance(race_data, dict):
            race_data.color = self.bot.colour
            return await ctx.send(embed=race_data)
        else:
            embed = discord.Embed(title=f"Race - {race_data['name']}", color=self.bot.colour)
            embed.set_author(name=f"{ctx.message.author.name}", icon_url=ctx.message.author.avatar_url)
            embed.set_footer(text="The Innkeeper, Powered by CF8, ran by the community.")

            desc_1 = f"**Speed:** `{race_data['speed']}ft`\n" \
                     f"**Ability Bonuses:** " \
                     f"`{','.join([item['name'] for item in race_data['ability_bonuses']])}`\n" \
                     f"**Size:** {race_data['size']}\n"
            embed.description = desc_1

            embed.add_field(name='Alignment', value=race_data['alignment'], inline=False)
            embed.add_field(name='Age', value=race_data['age'], inline=False)
            embed.add_field(name='Size description', value=race_data['size_description'], inline=False)
            embed.add_field(name='Language description', value=race_data['language_desc'], inline=False)

            return await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Classes(bot))
