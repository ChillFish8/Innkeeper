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


class DeckPlayer:
    FFMPEG_EXE = r"ffmpeg/bin/ffmpeg.exe"

    def __init__(self, ctx):
        self.guild = ctx.message.guild
        self.deck_message = None
        self.author = ctx.message.author
        self.creator_id = ctx.message.author.id
        self.channel = ctx.message.channel
        self._id = uuid.uuid4()
        self._voice_client = self.guild.voice_client
        self._voice_channel = self.author.voice.channel
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
        player = DeckPlayer(ctx)
        result = await player.run_player()
        if not result:
            return
        self.active_players[ctx.guild.id] = player

    @commands.command()
    async def addtrack(self, ctx: commands.Context, track: str):
        """
        + This spawns a embed which acts as the 'deck'
            This will get used for managing which tracks
            are in what section and binded to the relevant reaction.
        """


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
                        "id": video["href"][video["href"].index("=")+1:]
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
