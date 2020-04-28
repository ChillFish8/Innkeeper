from discord.ext import commands
import aiohttp
import json
import pandas as pd
import discord


class GetSpells:
    with open('./resources/monsters.json', 'r') as file:
        spells = json.load(file)
    spells_data_frame = pd.DataFrame(spells, columns=['name', 'url'])

    @classmethod
    async def _get_request(cls, url):
        """ Sends a request for the html """

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
    async def get_spell(cls, search: str):
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
            attempt_2: list = cls._search_list(search[0])  # lets get the first term and see
            if len(attempt_2) > 0:
                text = f"**Maybe you were looking for:**\n"
                text += '\n'.join([f"**•** `{item['name']}`" for item in attempt_2[:5]])

                embed = discord.Embed()
                embed.set_author(name="Oops! I cant find anything with that search term.",
                                 icon_url="https://cdn.discordapp.com/emojis/704784002166554776.png?v=1")
                embed.description = text

            else:
                embed = discord.Embed()
                embed.set_author(name="Oops! I cant find any results relating to your search.",
                                 icon_url="https://cdn.discordapp.com/emojis/704784002166554776.png?v=1")

            return embed


class Spells(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def spell(self, ctx, spell: str):
        """ Gets a class_ either from database or site """

        if not spell.isalpha():
            embed = discord.Embed(color=self.bot.colour)
            embed.set_author(name="Oops! I cant search for things that are not words or letters.",
                             icon_url="https://cdn.discordapp.com/emojis/704784002166554776.png?v=1")
            return await ctx.send(embed=embed)

        spell_data = await GetSpells.get_spell(spell.capitalize())

        if not isinstance(spell_data, dict):
            spell_data.color = self.bot.colour
            return await ctx.send(embed=spell_data)

        embed = discord.Embed(title=spell_data['name'], color=self.bot.colour)
        embed.set_author(name=f"{ctx.message.author.name}", icon_url=ctx.message.author.avatar_url)

        stats = f"**Level:** `{spell_data['level']}`\n" \
                f"**Range:** `{spell_data['range']}`\n" \
                f"**Duration:** `{spell_data['duration']}`\n" \
                f"**Components:** `{','.join(spell_data['components'])}`\n" \
                f"**Casting time:** `{spell_data['casting_time']}`\n" \
                f"**Concentration:** `{'yes' if spell_data['concentration'] else 'no'}`\n" \
                f"**Ritual:** `{'yes' if spell_data['ritual'] else 'no'}`\n"
        classes = f"**School:** `{spell_data['school']['name']}`\n" \
                  f"**Classes:**\n"
        for class_ in spell_data['classes']:
            classes += f"`{class_['name']}`\n"
        embed.add_field(name="Stats:", value=stats, inline=True)
        embed.add_field(name="More:", value=classes, inline=True)

        embed.add_field(name="Description", value=spell_data['desc'][0], inline=False)
        for extra in spell_data['desc'][1:]:
            embed.add_field(name="\u200b", value=extra, inline=False)

        if 'higher_level' in spell_data.keys():
            embed.add_field(name="At higher levels:", value="\n".join(spell_data['higher_level']), inline=False)
        embed.set_footer(text="The Innkeeper, Powered by CF8, ran by the community.")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Spells(bot))
