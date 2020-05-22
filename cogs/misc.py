from discord.ext import commands
import discord

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def invite(self, ctx):
        embed = discord.Embed(color=self.bot.colour).set_author(
            name="Lets roll together! (Click me)",
            url="https://discord.com/api/oauth2/authorize?client_id=572022206243012608&permissions=573959232&scope=bot",
            icon_url="https://cdn.discordapp.com/emojis/704784002355036190.png?v=1")
        return await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Misc(bot))
