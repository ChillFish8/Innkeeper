from discord.ext import commands
import discord
from custom_data.database import GuildConfig, MongoDatabase


class GuildSettings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.guild_only()
    @commands.has_guild_permissions(administrator=True)
    @commands.command(aliases=['setprefix'])
    async def set_prefix(self, ctx, *, prefix: str):
        config: GuildConfig = ctx.config
        config.set_prefix(prefix)
        await ctx.send(f"<:gelati_cute:704784002355036190> **My prefix is now** `{config.prefix}`")

    @commands.guild_only()
    @commands.has_guild_permissions(administrator=True)
    @commands.command(aliases=['resetprefix'])
    async def reset_prefix(self, ctx):
        config: GuildConfig = ctx.config
        new = config.reset_prefix()
        await ctx.send(f"<:gelati_cute:704784002355036190> **My prefix is now back to** `{new}` **(default)**")

    @commands.command(aliases=['getprefix'])
    async def get_prefix(self, ctx):
        config: GuildConfig = ctx.config
        await ctx.send(f"<:gelati_cute:704784002355036190> **My prefix is** `{config.prefix}`")

    async def cog_command_error(self, ctx, error):
        """ We catch out own error locally to keep it simple """
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(
                "<:wellfuck:704784002166554776> **Sorry! Your dont seem to have the permission** `ADMINISTRATOR`"
                " **Please make sure you have this permission before using this command.")

def setup(bot):
    bot.add_cog(GuildSettings(bot))
