from discord.ext import commands
from discord import Webhook
from discord import AsyncWebhookAdapter
import discord
import aiohttp
import json

class Logger(commands.Cog):
    with open("config.json", "r") as file:
        settings = json.load(file)

    def __init__(self, bot):
        self.bot = bot
        self.guild_hook = self.settings.get('guild_logging_webhook', False)
        self.command_hook = self.settings.get('command_logging_webhook', False)

    @classmethod
    async def send_to_wh(cls, embed, url):
        async with aiohttp.ClientSession() as sess:
            hook = Webhook.from_url(url, adapter=AsyncWebhookAdapter(sess))
            await hook.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        if not self.guild_hook:
            return
        embed = discord.Embed(color=discord.Colour.green())
        embed.set_author(name=f"Joined guild {guild}", icon_url=guild.icon_url)
        embed.set_footer(text=f"Total guild: {len(self.bot.guilds)}")
        await self.send_to_wh(embed, self.guild_hook)

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        if not self.guild_hook:
            return
        embed = discord.Embed(color=discord.Colour.red())
        embed.set_author(name=f"Joined guild {guild}", icon_url=guild.icon_url)
        embed.set_footer(text=f"Total guild: {len(self.bot.guilds)}")
        await self.send_to_wh(embed, self.guild_hook)

    @commands.Cog.listener()
    async def on_command(self, ctx: commands.Context):
        if not self.command_hook:
            return
        embed = discord.Embed(color=discord.Colour.purple())
        embed.set_author(name=f"{ctx.author.id} | {ctx.command}")
        await self.send_to_wh(embed, self.command_hook)

def setup(bot):
    bot.add_cog(Logger(bot))
