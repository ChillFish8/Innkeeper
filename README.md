# The Innkeeper discord bot

The Innkeeper is one of the most advanced D&D 5e discord bots around, Full Audio intergration, better initative tracking, full compatability dice rolling and fully custom content intergration. Used by over 180,000 Users across discord.

## Commands:
<dl>
  <dt>Content Commands:</dt>
  <dd>
  + <em>?spell</em> - Using a D&D 5e API or pulling from user's custom content<br>
  + <em>?class</em> - Using a D&D 5e API or pulling from user's custom content<br>
  + <em>?race</em> - Using a D&D 5e API or pulling from user's custom content<br>
  + <em>?monster</em> - Using a D&D 5e API or pulling from user's custom content<br>
  </dd>
  
  <dt>Dice Commands:</dt>
  <dd>
  + <em>?roll</em> - Supports complex dice rolling with exploding dice and more!<br>
  + <em>?randstats</em> - Get a standard 6 * 4d6kh3 roll block.<br>
  </dd>
  
  <dt>Audio Commands:</dt>
  <dd>
  + <em>?setup</em> - Used to start the audio deck ready for adding and playing tracks<br>
  + <em>?addtrack</em> - adds a track to the audio deck to play.<br>
  </dd>
</dl>

## Self-Hosting
### Requirements:
- [Discord.py - VOICE](https://pypi.org/project/discord.py/)
- [lxml](https://pypi.org/project/lxml/)
- [Java JDK 11](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html)
- [Lavalink.py](https://pypi.org/project/lavalink/)
- [Pandas](https://pypi.org/project/pandas/)
- [requests](https://pypi.org/project/requests/)
- [bs4](https://pypi.org/project/beautifulsoup4/)

### Creating a config file
- Create a new file called `config.json`
- add the following to the file:
```
{
  "token": "YOUR TOKEN HERE",
  "dev_ids": [YOUR DISCORD ID HERE,],
  "shard_count": 1
}
```

### Getting started:
- NOTE: This assumes you are firmilliar with the python syntax and processes used and is written for a windows user.

1. go to the `Innkeeper` folder and type `cmd` into the file path bar.
2. run `python3 -m venv project-env`
3. run `project-env\Scripts\activate.bat`
4. run `pip install -r requirements.txt`
5. create a [config file](https://github.com/ChillFish8/Innkeeper/blob/master/README.md#creating-a-config-file)
6. run `py main.py` in the venv



