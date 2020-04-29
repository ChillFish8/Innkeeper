from discord.ext import commands
import discord
import uuid


class DeckPlayer:
    FFMPEG_EXE = r"ffmpeg/bin/ffmpeg.exe"

    def __init__(self, ctx):
        self.guild = ctx.message.guild
        self.deck_message = None
        self.creator_id = ctx.message.author.id
        self._id = uuid.uuid4()
        self._voice_state = None
        self._voice_channel = None
        self._active = False
        self._initial_start = True
        self._track_1 = None
        self._track_2 = None
        self._track_3 = None
        self._track_4 = None
        self._track_5 = None

    def __repr__(self):
        """ Used for debugging """
        return f"Player - {self._id} - {self.guild.id}"

    def _get_markdown(self):
        """ Loads and generates the description markdown """
        pass

    async def _connect(self):
        pass

    async def run_player(self):
        """ Starts the deck listening for commands etc... """
        if self._initial_start:
            await self._connect()


class Audio(commands.Cog):
    """
    The Audio commands class, Using ffmpeg.

    Commands:

    Setup:
        + Starts the Mixer deck and loads and configures everything for your game

        **Events used:**
            - on_raw_reaction_add()
            - on_raw_reaction_remove()
            - on_message()

    Add Track:
        + Adds a track to the selected deck

        **Events used:**
            - on_message()

        **Links to:**
            - Setup (Command) / object

    Stop:
        + Shuts down the event listeners and deck safely, once everything has been cleaned up the bot will leave the call.

        **Events used:**
            - None (Command only)

        **Links to:**
            - Setup (Command) / object
    """
    def __init__(self, bot):
        self.bot = bot  # Discord AutoShardedBot
        self.active_players = {}   # Dictionary relating to guild Ids

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        """
        + WHEN A REACTION GETS ADDED
                This returns a set of Ids essentially,
                this is used for messages and reactions that
                will last longer than they get cached.
                We take the Ids then fetch the message object
                and go from there.
        """
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
        pass

    @commands.Cog.listener()
    async def on_voice_state_update(self,
                                    member: discord.Member,
                                    before: discord.VoiceState,
                                    after: discord.VoiceState):
        """
        + WHEN A REACTION GETS REMOVED
               This returns a set of Ids essentially,
               this is used for messages and reactions that
               will last longer than they get cached.
               We take the Ids then fetch the message object
               and go from there.
        """
        pass

    @commands.command()
    async def setup(self, ctx: commands.Context):
        """
        + This spawns a embed which acts as the 'deck'
            This will get used for managing which tracks
            are in what section and binded to the relevant reaction.
        """

    @commands.command()
    async def setup(self, ctx: commands.Context):
        """
        + This spawns a embed which acts as the 'deck'
            This will get used for managing which tracks
            are in what section and binded to the relevant reaction.
        """


def setup(bot):
    bot.add_cog(Audio(bot))
