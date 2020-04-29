from discord.ext import commands
import discord
import uuid
import urllib.parse
import aiohttp
import json
from bs4 import BeautifulSoup
import pafy
import asyncio
import concurrent.futures
import shutil
from datetime import datetime, timedelta
import os


class Track:
    def __init__(self, id_, name, guild_id):
        self.id = id_
        self.name = name
        self.playing = False
        self.length = -1
        self.position = 0
        self.pos_index = 0
        self.looping = False
        self.url = None
        self.audio = None
        self.guild_id = guild_id

    def __str__(self):
        return self.name

    def __repr__(self):
        if self.url is not None:
            return f"**{self.id} - [{self.name}]({self.url})**"
        else:
            return f"**{self.id} - {self.name}**"

    def __bool__(self):
        return self.playing

    def load_details(self, pafy_obj: pafy.new, url):
        self.url = url
        self.audio = pafy_obj
        self.name = pafy_obj.title
        self.length = timedelta(seconds=pafy_obj.length)

    async def download(self):
        await Youtube.download_audio(self.audio, id_=str(self.guild_id), path=os.getcwd())


class DeckPlayer:
    """
    **The Class that handles tracks and audio**

    - Stores upto 5 tracks
    - Connects to VC
    - Manages generating and updating the deck embed

    """
    FFMPEG_EXE = r"ffmpeg/bin/ffmpeg.exe"

    def __init__(self, ctx, bot, valid_emojis):
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
        self._voice_client = self.guild.voice_client
        self._voice_channel = self.author.voice.channel if self.author.voice is not None else None

        self._source = None

        self._active = False
        self._initial_start = True
        self._index = 0
        self._tracks = [Track(i + 1, name="No Audio Loaded") for i in range(self.max_tacks)]
        self._now_playing = self._tracks[0]

    def __repr__(self):
        """ Used for debugging """
        return f"Player - {self._id} - {self.guild.id}"

    def _get_embed(self):
        """ Loads and generates the description markdown """

        embed = discord.Embed(color=self.bot.colour)
        embed.set_author(name="Audio Deck", icon_url="https://cdn.discordapp.com/emojis/642858638116913202.png?v=1")
        embed.set_footer(text=f"Owner of deck: {self.author.name}", icon_url=self.author.avatar_url)

        desc = f"" \
               f"> **Now Playing:** `{self._now_playing.name if self._now_playing.playing else None}`\n" \
               f"> **Length:** `{self._now_playing.length if self._now_playing.playing else 0}`\n" \
               f"> **Volume:** `{self.volume if not self.muted else 0}%`\n" \
               f"> **Repeat:**  " \
               f"{'<:online:705030764437438565> True' if self._now_playing.looping else '<:offline:705030763950899241> False'}\n" \
               f"> **Status:** "

        if self._now_playing.playing:
            desc += f"<:online:705030764437438565> Playing\n"
        else:
            desc += f"<:offline:705030763950899241> Stopped\n"

        desc += "\n**" + "=" * 20 + " Tracks " + "=" * 20 + "**\n"
        embed.description = desc

        for i, track in enumerate(self._tracks):
            text = "<:index:705013516850954290>  \u200b" if i == self._index else ""
            text += f"{track}"
            if track.playing:
                text += f"\u200b **- [ Active ]** <a:8104LoadingEmote:661571011434643486>"
            elif self._voice_client.is_paused() and track.id == self._now_playing.id:
                text += f"\u200b **- [ Paused ]**"
            embed.add_field(name="\u200b", value=text, inline=False)
        return embed

    async def _connect(self):
        """ Connects to the voice call and loads the voice channel and client """
        if self._voice_channel is not None:
            if self._voice_client is not None:
                if self._voice_channel and self._voice_client.is_connected():
                    await self._voice_client.move_to(self._voice_channel)
                else:
                    self._voice_client = await self._voice_channel.connect()
            else:
                self._voice_client = await self._voice_channel.connect()
            return True, ""
        else:
            return False, "<:wellfuck:704784002166554776> **I cant join a channel if you are not in one either.**"

    async def run_player(self):
        """ Starts the deck listening for commands etc... """
        if self._initial_start:
            result, info = await self._connect()
            if not result:
                await self.channel.send(info)
                return False
            else:
                embed = self._get_embed()
                self.deck_message = await self.channel.send(embed=embed)

                for emoji in self.VALID_EMOJIS:
                    await self.deck_message.add_reaction(emoji)
                    await asyncio.sleep(0.1)
                return self

    async def update_deck(self, volume=False):
        embed = self._get_embed()
        await self.deck_message.edit(embed=embed)
        if volume:
            if self._source is not None:
                if self.muted:
                    self._source.volume = 0
                else:
                    self._source.volume = self.volume / 100

    async def shift_index(self, offset: int):
        if offset == -1 and not self._index:
            return
        elif offset == 1 and self._index == (self.max_tacks - 1):
            return
        else:
            self._index += offset
            await self.update_deck()

    async def change_vol(self, offset: int):
        if offset == -10 and not self.muted and not self.volume:
            return
        elif offset == 10 and not self.muted and self.volume == 100:
            return
        elif offset == 0 and not self.muted:
            self.muted = True
            await self.update_deck(volume=True)
        elif offset == 1 and self.muted:
            self.muted = False
            await self.update_deck(volume=True)
        else:
            if not self.muted:
                self.volume += offset
                await self.update_deck(volume=True)

    async def toggle_loop(self):
        self._now_playing.looping = not self._now_playing.looping
        await self.update_deck()

    def end_of_track(self, error=None):
        self._source.cleanup()
        self._now_playing.playing = False

    async def check_end(self):
        running = True
        while running:
            if not self._voice_client.is_playing() and not self._voice_client.is_paused():
                self._now_playing.playing = False
                await self.update_deck()
                running = False
                if self._now_playing.looping:
                    self._play_audio(self._now_playing.audio_url)
            await asyncio.sleep(2)

    def _play_audio(self, url):
        self._source = discord.PCMVolumeTransformer(
            discord.FFmpegPCMAudio(executable=self.FFMPEG_EXE,
                                   source=url),
            volume=self.volume / 100)
        self._now_playing.playing = True
        self._voice_client.play(self._source, after=self.end_of_track)
        asyncio.get_event_loop().create_task(self.check_end())

    async def play_pause_track(self, type_='add'):
        if self._voice_client.is_playing():
            if self._tracks[self._index].id == self._now_playing.id:
                self._now_playing.playing = False
                self._voice_client.pause()
                return await self.update_deck()
            else:
                if type_ == "add":
                    self._now_playing.playing = False
                    self._voice_client.stop()
                    self._source.cleanup()
                else:
                    return

        elif self._voice_client.is_paused():
            if self._tracks[self._index].id == self._now_playing.id:
                self._now_playing.playing = True
                self._voice_client.resume()
                return await self.update_deck()
            else:
                if type_ == "add":
                    self._now_playing.playing = False
                    self._voice_client.stop()
                    self._source.cleanup()
                else:
                    return

        track = self._tracks[self._index]
        self._now_playing = track
        self._play_audio(track.audio_url)
        await self.update_deck()

    async def add_track(self, url):
        if url.startswith('https://www.youtube.com/'):
            video = pafy.new(url)
        else:
            result = await Youtube.search(url, limit=1)
            video = pafy.new(result[0]['link'])
            url = result[0]['link']
        self._tracks[self._index].load_details(video, url)


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

    VALID_EMOJIS = ['🔼', '🔽', '🔇', '🔈', '🔊', '⏯️', '🔁', ]
    active_players = {}  # Dictionary relating to guild Ids

    def __init__(self, bot):
        self.bot = bot  # Discord AutoShardedBot

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
            if pos == 0:
                await player.shift_index(-1)  # Shift up
            elif pos == 1:
                await player.shift_index(1)  # Shift down
            elif pos == 2:
                await player.change_vol(0)  # Mute
            elif pos == 3:
                await player.change_vol(-10)  # Lower Vol
            elif pos == 4:
                await player.change_vol(10)  # Raise Vol
            elif pos == 5:
                await player.play_pause_track()
            elif pos == 6:
                await player.toggle_loop()  # Loop / Unloop

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
            player = self.active_players[payload.guild_id]
            if pos == 2:
                await player.change_vol(1)  # UnMute
            elif pos == 5:
                await player.play_pause_track(type_="remove")
            elif pos == 6:
                await player.toggle_loop()  # Loop / Un-loop

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
        player = DeckPlayer(ctx, self.bot, self.VALID_EMOJIS)
        player = await player.run_player()
        if not player:
            return
        self.active_players[ctx.guild.id] = player

    @commands.command()
    async def addtrack(self, ctx: commands.Context, track: str):
        """
        + This spawns a embed which acts as the 'deck'
            This will get used for managing which tracks
            are in what section and binded to the relevant reaction.
        """

        if ctx.guild.id in self.active_players:
            if '&list=' in track:
                return await ctx.send("<:wellfuck:704784002166554776> **Sorry! I dont support playlists.**")
            else:
                player: DeckPlayer = self.active_players[ctx.guild.id]
                if player.creator_id == ctx.author.id:
                    text = await player.add_track(track)
                    await ctx.send(text)
        else:
            return await ctx.send("<:wellfuck:704784002166554776> "
                                  "**Oops! You cant add audio to something that doesnt exit! "
                                  "Make sure you run the** `setup` **command first**")


class Youtube:
    """ Handles Youtube downloading etc... """
    opts = {'--hls-prefer-ffmpeg ': ''}

    @staticmethod
    async def search(terms, limit=10):
        """ Searches yt, gets the results back """
        data = YoutubeSearch(search_terms=terms, max_results=limit)
        await data.search()
        return data.videos

    @classmethod
    async def get_info(cls, url):
        """ Gets info on the track / video"""
        video = pafy.new(url, ydl_opts=cls.opts, basic=False)
        return video

    @staticmethod
    async def download_audio(video, id_, path):
        temp = video._title
        video._title = id_
        with concurrent.futures.ThreadPoolExecutor() as pool:
            await asyncio.get_event_loop().run_in_executor(pool, video.getbestaudio().download)
        video._title = temp
        shutil.move(f'./{id_}.webm', f"./{path}/{id_}.webm")
        return f"./{path}/{id_}.webm"


class YoutubeSearch:
    """ Web scrapes youtube - Fast """

    def __init__(self, search_terms: str, max_results=10):
        self.search_terms = search_terms
        self.max_results = max_results
        self.videos = None

    async def search(self):
        """ Sends the request to get the html """
        encoded_search = urllib.parse.quote(self.search_terms)
        BASE_URL = "https://youtube.com"
        url = f"{BASE_URL}/results?search_query={encoded_search}&pbj=1"
        async with aiohttp.ClientSession() as sess:
            async with sess.get(url) as resp:
                html = await resp.text()
                response = BeautifulSoup(html, "lxml")
                results = self.parse_html(response)
        self.videos = results

    def parse_html(self, soup):
        """ Uses lxml (for speed) ideally only wants first option for max speed """
        results = []
        for index, video in enumerate(soup.select(".yt-uix-tile-link")):
            if index < self.max_results:
                if video["href"].startswith("/watch?v="):
                    video_info = {
                        "title": video["title"],
                        "link": video["href"],
                        "id": video["href"][video["href"].index("=") + 1:]
                    }
                    results.append(video_info)
            else:
                return results
        return results

    def to_dict(self):
        return self.videos

    def to_json(self):
        return json.dumps({"videos": self.videos})


def setup(bot):
    bot.add_cog(Audio(bot))
