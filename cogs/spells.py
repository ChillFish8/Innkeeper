from discord.ext import commands


class Spells(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def spell(self, ctx, spell: str):
        """ Gets a spell either from database or site """

        await ctx.send(f"K man gay also his spell is: {spell}")

def setup(bot):
    bot.add_cog(Spells(bot))
