from discord.ext import commands
import discord


class DungeonStats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="dungeon")
    async def ai_dungeon_stats(self, ctx, *args):
        def check_commands(value):
            return "--" in value

        def check_arg(value):
            return "--" not in value
        command_list = tuple(filter(check_commands, args))
        args_list = tuple(filter(check_arg, args))
        data = {}
        for com, arg in zip(command_list, args_list):
            data[com] = arg

        show_gpu = data.pop('--gpu', False)
        show_cpu = data.pop('--cpu', False)
        get_all = data.pop('--full', False)
        usage_stats = data.pop('--times_used', False)

        if get_all:
            embed = discord.Embed(color=discord.Colour.magenta())
            embed.description = "```prolog\n" + (25 * "=") + f"Controller" + (25 * "=") + "\n" \
                                "Name: Genesis\n" \
                                "Status: [200 OK]\n" \
                                "Active Connections: 0\n```\n"
            for i in range(0, 2, 2):
                text = f"```prolog\n" \
                       f"Tesla{i}@Innkeeper:~$\n" \
                       f" Status: [200 Online - N/A]\n" \
                       f" Total Load: N/A\n" \
                       f" VRam Used: N/A\n" \
                       f"```"
                embed.add_field(name=(11 * "=") + f"  GPU {i}  " + (11 * "="), value=text, inline=True)
                text = f"```prolog\n" \
                       f"Tesla{i + 1}@Innkeeper:~$\n" \
                       f" Status: [200 Online - N/A]\n" \
                       f" Total Load: N/A\n" \
                       f" VRam Used: N/A\n" \
                       f"```"
                embed.add_field(name=(11 * "=") + f"  GPU {i + 1}  " + (11 * "="), value=text, inline=True)
                embed.add_field(name="\u200b", value="\u200b", inline=False)
            embed.set_author(name=f"{ctx.author} - AI Dungeon system info", icon_url=ctx.author.avatar_url)
            embed.set_footer(text="AI Dungeon is a premium command on The Innkeeper. Powered by CF8")

        else:
            if show_cpu:
                embed = discord.Embed(color=discord.Colour.magenta())
                embed.description = f"stuff todo"
                embed.set_author(name=f"{ctx.author} - AI Dungeon system info", icon_url=ctx.author.avatar_url)
                embed.set_footer(text="AI Dungeon is a premium command on The Innkeeper. Powered by CF8")

            if show_gpu:
                embed = discord.Embed(color=discord.Colour.magenta())
                embed.description = f"stuff todo"
                embed.set_author(name=f"{ctx.author} - AI Dungeon system info", icon_url=ctx.author.avatar_url)
                embed.set_footer(text="AI Dungeon is a premium command on The Innkeeper. Powered by CF8")
            if usage_stats:
                embed = discord.Embed(color=discord.Colour.magenta())
                embed.description = f"stuff todo"
                embed.set_author(name=f"{ctx.author} - AI Dungeon system info", icon_url=ctx.author.avatar_url)
                embed.set_footer(text="AI Dungeon is a premium command on The Innkeeper. Powered by CF8")
            else:
                embed = discord.Embed(color=discord.Colour.magenta())
                embed.description = f"stuff todo"
                embed.set_author(name=f"{ctx.author} - AI Dungeon system info", icon_url=ctx.author.avatar_url)
                embed.set_footer(text="AI Dungeon is a premium command on The Innkeeper. Powered by CF8")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(DungeonStats(bot))
