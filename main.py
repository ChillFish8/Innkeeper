from discord.ext import commands
import discord
import os
import json

with open('config.json', 'r') as file:
    config = json.load(file)

DEFAULT_PREFIX = ['?', '']
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

    async def on_ready(self):
        print("Bot connected")

    #async def on_shard_ready(self, shard_id):  todo set to on_shard_ready when in production
    #    """ This fires at every shard connect """
    #    print(f"Shard - [{shard_id}] Connected!")

    async def on_message(self, message):
        """ This will be used for custom Prefixes """

        await self.process_commands(message)

    async def on_command_error(self, context, exception):
        """ Any errors that happen in the bot will get sent here """
        if isinstance(exception, commands.CommandNotFound):
            pass


if __name__ == "__main__":
    the_innkeeper = Innkeeper(
        command_prefix=commands.when_mentioned_or(*DEFAULT_PREFIX),
        case_insensitive=True,
        fetch_offline_member=False,
        activity=discord.Game(name=f"RPGs | ?help"),
        shard_count=SHARD_COUNT,
    )
    the_innkeeper.startup()
    the_innkeeper.run(TOKEN)
