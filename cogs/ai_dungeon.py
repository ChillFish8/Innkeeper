from discord.ext import commands


class DungeonStats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot




def setup(bot):
    bot.add_cog(DungeonStats(bot))
