from discord.ext import commands
import discord
import uuid
import asyncio
from datetime import timedelta
import lavalink
import re

url_rx = re.compile(r'https?://(?:www\.)?.+')


class Track:
    def __init__(self, id_, name, guild_id):
        self.id = id_
        self.name = name
        self.guild_id = guild_id
        self.playing = False
        self.track: lavalink.AudioTrack = None
        self.paused = False

    def __str__(self):
        return self.name

    def __repr__(self):
        if self.track is not None:
            return f"**{self.id} - [{self.name}]({self.track.uri})**"
        else:
            return f"**{self.id} - {self.name}**"

    def __bool__(self):
        return self.playing


class DeckPlayer:
    """
    **The Class that handles tracks and audio**

    - Stores upto 5 tracks
    - Connects to VC
    - Manages generating and updating the deck embed

    """

    def __init__(self, ctx: commands.Context, bot, valid_emojis):
        self.VALID_EMOJIS = valid_emojis
        self.bot = bot
        self.guild = ctx.message.guild
        self.deck_message = None
        self.author = ctx.message.author
        self.creator_id = ctx.message.author.id
        self.channel = ctx.message.channel
        self.volume = 100
        self.muted = False
        self.max_tacks = 5

        self._id = uuid.uuid4()
        self._active = False
        self._initial_start = True
        self._index = 0
        self._tracks = [Track(i + 1, name="No Audio Loaded", guild_id=ctx.guild.id) for i in range(self.max_tacks)]
        self._now_playing = self._tracks[0]

    def __repr__(self):
        """ Used for debugging """
        return f"Player - {self._id} - {self.guild.id}"

    def _get_embed(self):
        """ Loads and generates the description markdown """
        player: lavalink.DefaultPlayer = self.bot.lavalink.player_manager.get(self.guild.id)

        embed = discord.Embed(color=self.bot.colour)
        embed.set_author(name="Audio Deck", icon_url="https://cdn.discordapp.com/emojis/642858638116913202.png?v=1")
        embed.set_footer(text=f"Owner of deck: {self.author.name}", icon_url=self.author.avatar_url)

        desc = f"" \
               f"> **Now Playing:** `{self._now_playing.name if self._now_playing.playing else None}`\n" \
               f"> **Length:** `{self._now_playing.track.duration if self._now_playing.playing else 0}`\n" \
               f"> **Volume:** `{self.volume if not self.muted else 0}%`\n" \
               f"> **Repeat:**  " \
               f"{'<:online:705030764437438565> True' if player.repeat else '<:offline:705030763950899241> False'}\n" \
               f"> **Status:** "

        if player.is_playing:
            desc += f"<:online:705030764437438565> Playing\n"
        else:
            desc += f"<:offline:705030763950899241> Stopped\n"

        desc += "\n**" + "=" * 20 + " Tracks " + "=" * 20 + "**\n"
        embed.description = desc

        for i, track in enumerate(self._tracks):
            text = "<:index:705013516850954290>  \u200b" if i == self._index else ""
            if track.track is not None:
                text += f"[{track}]({track.track.uri})"
            else:
                text += f"{track}"
            if track.playing:
                text += f"\u200b **- [ Active ]** <a:8104LoadingEmote:661571011434643486>"
            elif track.paused and track.id == self._now_playing.id:
                text += f"\u200b **- [ Paused ]**"
            embed.add_field(name="\u200b", value=text, inline=False)
        return embed

    async def update_deck(self, volume=False):
        embed = self._get_embed()
        await self.deck_message.edit(embed=embed)
        if volume:
            player: lavalink.DefaultPlayer = self.bot.lavalink.player_manager.get(self.guild.id)
            if self.muted:
                await player.set_volume(0)
            else:
                await player.set_volume(self.volume)

    async def shift_index(self, offset: int):
        if offset == -1 and not self._index:
            return
        elif offset == 1 and self._index == (self.max_tacks - 1):
            return
        else:
            self._index += offset
            await self.update_deck()

    async def setup(self):
        embed = self._get_embed()
        self.deck_message = await self.channel.send(embed=embed)
        for emoji in self.VALID_EMOJIS:
            await self.deck_message.add_reaction(emoji)
        return self

    async def add_track(self, track: lavalink.AudioTrack):
        slot = self._tracks[self._index]
        slot.name = track.title
        slot.playing = False
        slot.paused = False
        slot.track = track
        self._tracks[self._index] = slot
        await self.update_deck()
        return self

    @property
    def index_point(self):
        return self._index

    async def _disconnected(self):
        await self.deck_message.delete()
        await self.channel.send("**I have been disconnected from the voice call, Stopping deck.**")

    async def play_pause(self, reaction_remove=False):
        player: lavalink.DefaultPlayer = self.bot.lavalink.player_manager.get(self.guild.id)
        track = self._tracks[self._index]
        if track.track is None:
            return
        else:
            if player.is_playing and player.is_connected:
                if not track.paused and reaction_remove and self._now_playing.id == track.id:
                    await player.set_pause(True)
                elif track.paused and not reaction_remove and self._now_playing.id != track.id:
                    await player.play(track.track)
                    track.playing = True
                    track.paused = False
                    track.name = track.track.title
                    self._tracks[self._index] = track
            else:
                if not player.is_connected:
                    return await self._disconnected()
                else:
                    await player.play(track.track)
                    track.playing = True
                    track.paused = False
                    track.name = track.track.title
                    self._tracks[self._index] = track
            await self.update_deck()

    async def toggle_mute(self):
        player: lavalink.DefaultPlayer = self.bot.lavalink.player_manager.get(self.guild.id)
        self.muted = not self.muted
        if self.muted:
            await player.set_volume(0)
        else:
            await player.set_volume(self.volume)



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

    VALID_EMOJIS = ['🔼', '🔽', '🔇', '🔈', '🔊', '⏯️', '🔁', '<:TickNo:640187792911237131>']
    active_players = {}  # Dictionary relating to guild Ids

    def __init__(self, bot):
        self.bot = bot

        if not hasattr(bot, 'lavalink'):  # This ensures the client isn't overwritten during cog reloads.
            bot.lavalink = lavalink.Client(641381762785607698)
            bot.lavalink.add_node('127.0.0.1', 2333, 'youshallnotpass', 'eu', 'default-node')  # Host, Port, Password, Region, Name
            bot.add_listener(bot.lavalink.voice_update_handler, 'on_socket_response')

        lavalink.add_event_hook(self.track_hook)

    @commands.command()
    async def setup(self, ctx: commands.Context):
        """
        + This spawns a embed which acts as the 'deck'
            This will get used for managing which tracks
            are in what section and binded to the relevant reaction.
        """
        if ctx.guild.id not in self.active_players:
            deck = DeckPlayer(ctx, self.bot, self.VALID_EMOJIS)
            self.active_players[ctx.guild.id] = await deck.setup()
        else:
            await ctx.send("<:wellfuck:704784002166554776> **You already have an active deck running."
                           " Please close the existing deck first.**")

    @commands.command(aliases=['at', 'p'])
    async def addtrack(self, ctx: commands.Context, track: str):
        """
        + This spawns a embed which acts as the 'deck'
            This will get used for managing which tracks
            are in what section and binded to the relevant reaction.
        """
        if ctx.guild.id not in self.active_players:
            return await ctx.send("<:wellfuck:704784002166554776> **Sorry! I cant add a track "
                                  "without a active audio deck running. run SETUP first before adding a track**")
        else:
            player = self.bot.lavalink.player_manager.get(ctx.guild.id)

            query = track.strip('<>')

            if not url_rx.match(query):
                query = f'ytsearch:{query}'

            results = await player.node.get_tracks(query)

            if not results or not results['tracks']:
                return await ctx.send(
                    "<:wellfuck:704784002166554776> **Sorry! I didn't find anything with that term.**")

            # Valid loadTypes are:
            #   TRACK_LOADED    - single video/direct URL)
            #   PLAYLIST_LOADED - direct URL to playlist)
            #   SEARCH_RESULT   - query prefixed with either ytsearch: or scsearch:.
            #   NO_MATCHES      - query yielded no results
            #   LOAD_FAILED     - most likely, the video encountered an exception during loading.
            if results['loadType'] == 'PLAYLIST_LOADED':
                tracks = results['tracks']

                #for track in tracks:   todo add playlist support
                #    player.add(requester=ctx.author.id, track=track)

                text = "<:wellfuck:704784002166554776> **Sorry! I dont currently support playlists on a single disc.**"
            else:
                track = results['tracks'][0]
                track = lavalink.models.AudioTrack(track, ctx.author.id, recommended=True)
                deck: DeckPlayer = self.active_players[ctx.guild.id]
                await deck.add_track(track)
                text = f"<:gelati_cute:704784002355036190> **Added audio track to disc {deck.index_point}**"
            await ctx.send(text)

    @classmethod
    def get_player_msg_ids(cls):
        return [player.deck_message.id for player in cls.active_players.values()]

    @classmethod
    def get_player_user_ids(cls):
        return [player.creator_id for player in cls.active_players.values()]

    @classmethod
    async def filter_payload(cls, payload):
        if payload.guild_id not in cls.active_players:
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
            pos = self.VALID_EMOJIS.index(str(payload.emoji))
            player: DeckPlayer = self.active_players[payload.guild_id]

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
            pos = self.VALID_EMOJIS.index(str(payload.emoji))
            player: DeckPlayer = self.active_players[payload.guild_id]
            if not pos:
                await player.shift_index(1)
            elif pos == 1:
                await player.shift_index(-1)
            elif pos == 2:
                await player.

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

    async def track_hook(self, event):
        if isinstance(event, lavalink.events.QueueEndEvent):
            pass

    async def connect_to(self, guild_id: int, channel_id: str):
        """ Connects to the given voicechannel ID. A channel_id of `None` means disconnect. """
        ws = self.bot._connection._get_websocket(guild_id)
        await ws.voice_state(str(guild_id), channel_id)

    def cog_unload(self):
        """ Cog unload handler. This removes any event hooks that were registered. """
        self.bot.lavalink._event_hooks.clear()

    async def cog_before_invoke(self, ctx):
        """ Command before-invoke handler. """
        guild_check = ctx.guild is not None

        if guild_check:
            await self.ensure_voice(ctx)
        return guild_check

    async def cog_command_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send(error.original)

    async def ensure_voice(self, ctx):
        """ This check ensures that the bot and command author are in the same voicechannel. """
        player = self.bot.lavalink.player_manager.create(ctx.guild.id, endpoint=str(ctx.guild.region))

        if not ctx.author.voice or not ctx.author.voice.channel:
            raise commands.CommandInvokeError(
                '<:wellfuck:704784002166554776> **Join a voicechannel first.**')

        if not player.is_connected:
            permissions = ctx.author.voice.channel.permissions_for(ctx.me)

            if not permissions.connect or not permissions.speak:  # Check user limit too?
                raise commands.CommandInvokeError(
                    '<:wellfuck:704784002166554776> **I need the `CONNECT` and `SPEAK` permissions.**')

            player.store('channel', ctx.channel.id)
            await self.connect_to(ctx.guild.id, str(ctx.author.voice.channel.id))
        else:
            if int(player.channel_id) != ctx.author.voice.channel.id:
                raise commands.CommandInvokeError(
                    '<:wellfuck:704784002166554776> **You need to be in my voicechannel.**')


def setup(bot):
    bot.add_cog(Audio(bot))
