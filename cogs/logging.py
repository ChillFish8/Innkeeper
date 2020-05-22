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
    async def send_to_wh(cls, embed, url, text=False):
        async with aiohttp.ClientSession() as sess:
            hook = Webhook.from_url(url, adapter=AsyncWebhookAdapter(sess))
            if text:
                await hook.send(content=embed)
            else:
                await hook.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_join(self, guild: discord.Guild):
        if not self.guild_hook:
            return
        desc = "💜"
        if len(guild.members) > 1000:
            desc += "🔥"
        if len(guild.members) > 10000:
            desc += "🌟"
        desc += " " + f"Joined guild {guild}, Total members: {len(guild.members)}"
        await self.send_to_wh(desc, self.guild_hook, text=True)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        if not self.guild_hook:
            return
        desc = "💔"
        if len(guild.members) > 1000:
            desc += "💔"
        if len(guild.members) > 10000:
            desc += "💔"
        desc += " " + f"Lost guild {guild}, Total members: {len(guild.members)}"
        await self.send_to_wh(desc, self.guild_hook, text=True)

    @commands.Cog.listener()
    async def on_command(self, ctx: commands.Context):
        if not self.command_hook:
            return
        desc = f"**User:** `{ctx.author.id}` **|** " \
               f"**Guild:** `{ctx.guild.id if ctx.guild is not None else 'direct message'}` **|** " \
               f"**Command:** `{ctx.command}`"
        await self.send_to_wh(desc, self.command_hook, text=True)

def setup(bot):
    bot.add_cog(Logger(bot))
