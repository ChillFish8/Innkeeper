from discord.ext import commands
import discord


class DiceRoller(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roll(self, ctx, dice_str: str):
        """ Roll a set of dice e.g 4d6kh3"""
        pass

    @commands.command()
    async def randstats(self, ctx):
        """ Roll a set of random stats ( 6 * 4d6kh3 ) """
        pass

    @commands.command()
    async def charroll(self, ctx, dice_str: str):
        """ Roll a set of dice """
        pass


def setup(bot):
    bot.add_cog(DiceRoller(bot))
