from discord.ext import commands
import aiohttp
import json
import pandas as pd
import discord


class GetMonster:
    with open('./resources/monsters.json', 'r') as file:
        monsters = json.load(file)
    monsters_data_frame = pd.DataFrame(monsters, columns=['name', 'url'])

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
        results: pd.DataFrame = cls.monsters_data_frame[
            cls.monsters_data_frame['name'].str.contains(search)]
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
    async def get_monster(cls, search: str):
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


class Monsters(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def monster(self, ctx, monster: str):
        """ Gets a class_ either from database or site """

        if not monster.isalpha():
            embed = discord.Embed(color=self.bot.colour)
            embed.set_author(name="Oops! I cant search for things that are not words or letters.",
                             icon_url="https://cdn.discordapp.com/emojis/704784002166554776.png?v=1")
            return await ctx.send(embed=embed)

        monster_data = await GetMonster.get_monster(monster.capitalize())

        if not isinstance(monster_data, dict):
            monster_data.color = self.bot.colour
            return await ctx.send(embed=monster_data)

        embed = discord.Embed(title=monster_data['name'], color=self.bot.colour)
        embed.set_author(name=f"{ctx.message.author.name}", icon_url=ctx.message.author.avatar_url)

        # Quick stats
        text = f"**Size:** `{monster_data['size']}`\n" \
               f"**Alignment:** `{monster_data['alignment']}`\n" \
               f"**Armor class:** `{monster_data['armor_class']}`\n" \
               f"**Hit points:** `{monster_data['hit_points']}`\n"
        text += "**Speed:**" + ','.join([f"{key} {value}" for key, value in monster_data['speed'].items()])
        embed.add_field(name="Quick Stats", value=text, inline=True)

        # Ability Scores
        text = f"**STR:** `{monster_data['strength']}`\n" \
               f"**DEX:** `{monster_data['dexterity']}`\n" \
               f"**CON:** `{monster_data['constitution']}`\n" \
               f"**INT:** `{monster_data['intelligence']}`\n" \
               f"**WIS:** `{monster_data['wisdom']}`\n"\
               f"**CHA:** `{monster_data['charisma']}`\n"
        embed.add_field(name="Ability Score", value=text, inline=True)

        # Profs
        text = '\n'.join([f"**{dic['name']}** `+{dic['value']}`" for dic in monster_data['proficiencies']])
        embed.add_field(name="Proficiencies", value=text, inline=True)

        # Senses and Langs
        text = f"**Senses:**" + ",".join([f"`{key_} {value}`" for key_, value in monster_data['senses'].items()])
        text += f"\n**Languages:** `{monster_data['languages']}`\n" \
                f"**Challenge rating:** `{monster_data['challenge_rating']}`\n"
        embed.add_field(name="Details", value=text, inline=False)

        # Abilities
        for ability in monster_data['special_abilities'][:3]:
            embed.add_field(name=f"{ability['name']}", value=f"{ability['desc']}", inline=False)

        embed.set_footer(text="The Innkeeper, Powered by CF8, ran by the community.")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Monsters(bot))
