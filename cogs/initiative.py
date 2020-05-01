from discord.ext import commands
import discord


class Tracker:
    """ This class self contains the tracking of users, initiatives affects etc... """

    def __init__(self, ctx: commands.Context):
        self.init_message = None
        self.dungeon_master = ctx.author
        self.permissioned_users = []
        self.guild = ctx.guild

    def _get_embed(self):
        pass


class Initiative(commands.Cog):
    active_initiatives = {}
    VALID_EMOJIS = ['🔄', '🗑️', '<:TickNo:640187792911237131>']

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def initiative(self, ctx: commands.Context):
        """ Track your initiative """
        if ctx.guild.id in self.active_initiatives:
            return await ctx.send("<:wellfuck:704784002166554776> **You already have an initiative tracker running."
                                  " Please close the existing tracker first.**")

    @classmethod
    def get_initiative_msg_ids(cls):
        """ gets a list of initiative message ids """
        return [initiatives.init_message.id for initiatives in cls.active_initiatives.values()]

    @classmethod
    def get_initiative_user_ids(cls):
        """ :returns a list of creator (DM) ids """
        return [initiatives.creator_id for initiatives in cls.active_initiatives.values()]

    @classmethod
    async def filter_payload(cls, payload):
        """ Filters out the payloads we want to respond to and ones we dont """
        if payload.guild_id not in cls.active_initiatives:
            return False
        elif str(payload.emoji) not in cls.VALID_EMOJIS:
            return False
        elif payload.message_id not in cls.get_initiative_msg_ids():
            return False
        else:
            return True

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        """
        + WHEN A REACTION GETS ADDED
                This returns a set of Ids essentially,
                this is used for messages and reactions that
                will last longer than they get cached.
                We take the Ids then fetch the message object
                and go from there.
        """
        if await self.filter_payload(payload=payload):
            pass

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        """
        + WHEN A REACTION GETS REMOVED
               This returns a set of Ids essentially,
               this is used for messages and reactions that
               will last longer than they get cached.
               We take the Ids then fetch the message object
               and go from there.
        """
        if await self.filter_payload(payload=payload):
            pass


def setup(bot):
    bot.add_cog(Initiative(bot))
