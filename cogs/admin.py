from discord.ext import commands


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.is_owner()
    @commands.command()
    async def debug(self, ctx):
        text = "```prolog\n"
        text += "\n".join([f"{key.capitalize()}: {value}" for key, value in ctx.__dict__.items()])
        text += "```"
        return await ctx.send(text)


def setup(bot):
    bot.add_cog(Admin(bot))
