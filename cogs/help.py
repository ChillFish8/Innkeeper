from discord.ext import commands
import discord


class HelpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        """ The main help command of The Innkeeper"""

        embed = discord.Embed(color=self.bot.colour)
        embed.set_author(name="The Innkeeper help page", icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="The Innkeeper, Powered by CF8, ran by the community.")

        # General Commands
        desc_1 = f"<:discord:642859572524220427>  **General Commands**  <:discord:642859572524220427>\n" \
                 f"`?help` - Brings up this help page.\n" \
                 f"`?setprefix <New Prefix>` - Set a custom Prefix.\n"
        embed.add_field(name="\u200b", value=desc_1, inline=False)

        # Dice Rolling
        desc_2 = f"<:d20:642067624385183753>  **Dice Rolling**  <:d20:642067624385183753>\n" \
                 f"`?roll <dice string>` - Roll a set of dice, e.g. `4d6kh3`\n" \
                 f"`?charoll <dice or custom>` - Roll dice from a custom character's stats.\n" \
                 f"`?randstats` - Rolls the default 4d6kh3 for stats."
        embed.add_field(name="\u200b", value=desc_2, inline=False)

        # Content Commands
        desc_3 = f"<:LOGO:642846268514893844>  **Content lookup**  <:LOGO:642846268514893844>\n" \
                 f"`?spell <spell name>` - Searches for a spell and brings it up.\n" \
                 f"`?class <class name>` - Search for a class\n" \
                 f"`?monster <monster name>` - Searches for a monster and brings it up.\n" \
                 f"`?race <race name>` - Search for a race.\n" \
                 f"`?feat <feat name>` - Search for a feat.\n"
        embed.add_field(name="\u200b", value=desc_3, inline=False)

        # Custom character Commands
        desc_4 = f"<:OP_Bot_Logo_Clear:642858638116913202>  **Custom Characters**  <:OP_Bot_Logo_Clear:642858638116913202>\n" \
                 f"`?loadcharacter` - Load a compatible character into Innkeeper's system.\n" \
                 f"`?removecharacter` - Remove a loaded character from Innkeeper's system.\n"
        embed.add_field(name="\u200b", value=desc_4, inline=False)

        # Dungeon master's commands
        desc_5 = f"<:gelatinous_cute:651475508684652554>  **Dungeon Master's Area**  <:gelatinous_cute:651475508684652554>\n" \
                 f"`?loadaudio` - Load a audio file/url to have Innkeeper play during games.\n" \
                 f"`?play` - Play the loaded audio.\n" \
                 f"`?pause` - Pause the current playing audio track.\n" \
                 f"`?loop` - Loop the current audio track or list.\n" \
                 f"`?stop` - Stop running audio.\n"
        embed.add_field(name="\u200b", value=desc_5, inline=False)

        await ctx.send(embed=embed)


def setup(bot):
    bot.remove_command('help')
    bot.add_cog(HelpCommand(bot))
