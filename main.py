import discord
import json
import os
from discord.ext import commands

from custom_data import database

with open('config.json', 'r') as file:
    config = json.load(file)

DEFAULT_PREFIX = ['?']
TOKEN = config['token']
DEVELOPER_IDS = config['dev_ids']
SHARD_COUNT = config['shard_count']


class Innkeeper(commands.AutoShardedBot):
    """
    The Innkeeper,  a Auto Sharded Bot.

    Dedicated to all the role players out in the world

    """

    def __init__(self, command_prefix, **options):
        super().__init__(command_prefix, **options)
        self.owner_ids = DEVELOPER_IDS
        self.colour = 0x3deaf5
        self.icon = "https://cdn.discordapp.com/attachments/638140888949719080/704697130576511056/OrcPubLogo.png"
        self.database = database.MongoDatabase()

    def startup(self):
        """
        Loads all the commands listed in cogs folder, if there isnt a cogs folder it makes one
        :return:
        """
        if not os.path.exists('cogs'):
            os.mkdir('cogs')

        cogs_list = os.listdir('cogs')
        if '__pycache__' in cogs_list:
            cogs_list.remove('__pycache__')

        for cog in cogs_list:
            try:
                self.load_extension(f"cogs.{cog.replace('.py', '')}")
            except Exception as e:
                print(f"Failed to load cog {cog}, Error: {e}")
                raise e

    async def on_ready(self):
        print("Bot connected")

    #async def on_shard_ready(self, shard_id):  todo set to on_shard_ready when in production
    #    """ This fires at every shard connect """
    #    print(f"Shard - [{shard_id}] Connected!")

    async def get_config(self, context):
        guild_data = database.GuildConfig(context.guild.id if context.guild is not None else 0, database=self.database)
        setattr(context, 'config', guild_data)
        return context

    async def on_message(self, message):
        """ This will be used for custom Prefixes """
        await self.process_commands(message)

    async def on_command_error(self, ctx, exception):
        """ Any errors that happen in the bot will get sent here """
        await ErrorProcessor.process_error(ctx, exception)


class ErrorProcessor:
    @classmethod
    async def process_error(cls, ctx: commands.Context, exception):
        """ This handles the errors and sends them to different area of the handler"""
        if isinstance(exception, commands.CommandNotFound):     # When the right prefix is used but wrong command
            return

        elif isinstance(exception, commands.MissingRequiredArgument):   # When a user doesnt give it something
            return await ctx.send(cls.missing_args())

        elif isinstance(exception, discord.Forbidden):  # If its not allowed to do something
            return await ctx.send(cls.missing_perms(ctx.message.channel))

        elif isinstance(exception, discord.NotFound):   # If it cant find something
            return

        elif isinstance(exception, commands.CheckFailure):  # We used a check deco and it went no
            return await ctx.send(cls.load_check_msg(ctx))

        elif isinstance(exception, commands.NoPrivateMessage):  # the command is guild only
            return await ctx.send(cls.guild_only())

        elif ctx.command.name in ("roll", "setup"):
            return

        else:
            text = exception
            await ctx.send(text)
            raise exception

    @staticmethod
    def missing_args():
        return "<:wellfuck:704784002166554776> **You didnt give me anything to work with.**"

    @staticmethod
    def missing_perms(channel):
        return f"<:wellfuck:704784002166554776> **Oops! Looks like i dont have permission todo that in {channel}.**"

    @staticmethod
    def load_check_msg(ctx):
        check_name = ctx.command.checks[0].__qualname__
        return f"<:wellfuck:704784002166554776> **Oops! **"

    @staticmethod
    def guild_only():
        return f"<:wellfuck:704784002166554776> " \
               f"**Sorry, You can only run this command " \
               f"in a server, not private message.**"


async def get_custom_prefix(bot: Innkeeper, message: discord.Message):
    guild_data = database.GuildConfig(message.guild.id if message.guild is not None else 0, database=bot.database)
    return guild_data.prefix

if __name__ == "__main__":
    the_innkeeper = Innkeeper(
        command_prefix=get_custom_prefix,
        case_insensitive=True,
        fetch_offline_member=False,
        activity=discord.Game(name=f"RPGs | ?help"),
        shard_count=SHARD_COUNT,
        )
    the_innkeeper.before_invoke(the_innkeeper.get_config)
    the_innkeeper.startup()
    the_innkeeper.run(TOKEN)
