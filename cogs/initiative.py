from discord.ext import commands
import discord


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
    def get_player_msg_ids(cls):
        return [player.deck_message.id for player in cls.active_initiatives.values()]

    @classmethod
    def get_player_user_ids(cls):
        return [player.creator_id for player in cls.active_initiatives.values()]

    @classmethod
    async def filter_payload(cls, payload):
        if payload.guild_id not in cls.active_initiatives:
            return False
        elif str(payload.emoji) not in cls.VALID_EMOJIS:
            return False
        elif payload.user_id not in cls.get_player_user_ids():
            return False
        elif payload.message_id not in cls.get_player_msg_ids():
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
