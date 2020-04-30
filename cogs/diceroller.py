import random
import re

import discord
from discord.ext import commands


class DiceRoller(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['r'])
    async def roll(self, ctx, *, dice_str: str):
        text = Roll.roll(dice_str)
        if text.startswith("!!"):
            embed = discord.Embed(color=self.bot.colour, description=text[2:])
            embed.set_author(icon_url="https://cdn.discordapp.com/emojis/704784002254503966.png?v=1",
                             name="An error happened:")
            await ctx.send(embed=embed)
        else:
            await ctx.send(text)

    @commands.command()
    async def randstats(self, ctx):
        """ Roll a set of random stats ( 6 * 4d6kh3 ) """

        text = f"**Your rolls:** <:d20:642067624385183753> \n"
        total_ = 0
        for i in range(6):
            dice, totstr, total = Roll.stats_roll('4d6kh3')
            text += f"> **Roll {i + 1})** "
            text += " (".join((totstr, dice)) + ")\n"
            total_ += total
        text += f"> **Total:** `{total_} (+{(total_ - 10) // 2})`"
        await ctx.send(text)

    @commands.command()
    async def charroll(self, ctx, dice_str: str):
        """ Roll a set of dice """
        pass

    async def cog_command_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            return await ctx.send(error.original)


class Roll:

    @classmethod
    def roll(cls, command: str):
        command = Roll.format(command)
        if type(command) == str:
            return command

        total = 0
        throws = ""

        for throw in command:
            neg = -1 if (throw[0] == "-") else 1
            rolls, dice_meta = cls.setup_command(throw.replace("-", ""))

            try:
                roll = RandDice(**dice_meta) * rolls
            except ValueError as e:
                return e

            total += sum(roll) * neg
            throws += f"• {throw}: `{', '.join([str(num) for num in roll])}`\n"
        throws += f"<:d20:642067624385183753> **Roll:** `{total}`"
        return throws

    @classmethod
    def stats_roll(cls, command: str):
        command = Roll.format(command)
        if type(command) == str:
            return command

        total = 0
        throws = ""

        for throw in command:
            neg = -1 if (throw[0] == "-") else 1
            rolls, dice_meta = cls.setup_command(throw.replace("-", ""))

            try:
                roll = RandDice(**dice_meta) * rolls
            except ValueError as e:
                return e

            total += sum(roll) * neg
            throws += f"{', '.join([str(num) for num in roll])}"
        total_mod = (total - 10) // 2
        if total_mod >= 0:
            total_mod = "+" + str(total_mod)
        return throws, f"`{total} ({total_mod})`", total

    @classmethod
    def setup_command(cls, dice_throw: str):
        rolls, dice_meta = dice_throw.split("d")
        rolls = int(rolls) if rolls != "" else 1

        sides = int(dice_meta[:Utilities.index_next_int(dice_meta)])
        dice_meta = dice_meta[Utilities.index_next_int(dice_meta):]
        kh, kl, exp = cls.get_dice_modifiers(dice_meta)

        throws_meta = {"dice_sides": sides, "kh": kh, "kl": kl, "exp": exp}

        return rolls, throws_meta

    @staticmethod
    def format(command):
        command = command.lower()
        state_1 = re.compile("-?\d*d\d+(k[hl]\d+)?(e\d+)?").search
        state_2 = re.compile("-?\d*d\d+(e\d+)?(k[hl]\d+)?").search
        invalid = re.compile("(d\D|^-\d$)").findall
        command = command.replace("-", "+-").replace(" ", "").split("+")
        command_parts = []
        for dice_roll in command:
            if not invalid(dice_roll) and len(dice_roll) > 1:
                option_1 = state_1(dice_roll).group()
                option_2 = state_2(dice_roll).group()
                if dice_roll == option_1 or dice_roll == option_2:
                    command_parts.append(dice_roll)

        if command_parts == command:
            return command_parts
        else:
            command = "+".join(command).replace("+-", "-")
            command_parts = "+".join(command_parts).replace("+-", "-")
            return Utilities.show_error(command, command_parts)

    @staticmethod
    def get_dice_modifiers(meta: str):
        kh = kl = exp = None
        if meta:
            if "e" in meta:
                split = meta.replace("kl", "kh").split("kh")
                split = [item for item in split if item]
                split = [item for item in split if not item.isdigit()][0]
                while not split.isdigit():
                    split = split[1:]
                exp = int(split)

            if "k" in meta:
                split = meta.split("e")
                split = [item for item in split if item]
                split = [item for item in split if not item.isdigit()][0]
                while split[0] not in "hl":
                    split = split[1:]

                if split[0] == "l":
                    kl = int(split[1:])
                else:
                    kh = int(split[1:])

        return kh, kl, exp


class Utilities:

    @classmethod
    def difference(cls, str_1, str_2):
        while len(str_1) != 0 and len(str_2) != 0:
            if str_1[0] == str_2[0]:
                str_1 = str_1[1:]
                str_2 = str_2[1:]
            else:
                return cls.string_lengths(str_1, str_2)

        return cls.string_lengths(str_1, str_2)

    @staticmethod
    def string_lengths(*strings: str, order="desc") -> str:
        reverse = (order == "desc")
        return sorted(strings, key=len, reverse=reverse)[0]

    @staticmethod
    def index_substring(string, sub_string):
        if sub_string not in string:
            return None
        else:
            sub_length = len(sub_string)
            index = 0
            while sub_string not in string[index: index + sub_length + 1]:
                index += 1

            return index + 1

    @staticmethod
    def index_next_int(string: str):
        for count, char in enumerate(string):
            if not char.isdigit():
                return count
            count += 1

        return len(string)

    @classmethod
    def show_error(cls, string, sub_string):
        index = cls.index_substring(string, cls.difference(string, sub_string))
        error_text = f"<:wellfuck:704784002166554776> **An error happened:**\n > `{string}`\n > " \
                     f"`{'-'*index}^` **error near here**\n"
        return error_text


class RandDice:

    max_rolls = 100

    def __init__(self, dice_sides: int, kh: int = None, kl: int = None, exp: int = None):
        self.sides = dice_sides
        self.kh = kh
        self.kl = kl
        self.e = exp

        if kh and kl:
            raise commands.CommandInvokeError(
                "<:wellfuck:704784002166554776> KH and KL cannot be specified on the same throw.")

        if dice_sides == 1 and exp == 1:
            raise commands.CommandInvokeError(
                "<:wellfuck:704784002166554776> **Hold on there, you can't just go around "
                "throwing infinite dice like you own the place!**")

        if self.kh is None:
            self.kh = -1
        if self. kl is None:
            self.kl = -1
        if self.e is None:
            self.e = -1

        if self.kh < 0 and self.kh != -1 or self.kl < 0 and self.kl != -1:
            raise commands.CommandInvokeError(
                "<:wellfuck:704784002166554776> **I'm sorry but you can't keep a negative "
                "number of dice, that just doesn't work does it.**")

    def __mul__(self, other):
        if other > self.max_rolls:
            raise commands.CommandInvokeError(
                "<:wellfuck:704784002166554776> **Sorry but you can only roll a dice up to 100 times, "
                "what do you want a number that big for anyways?**")

        output = []
        for _ in range(other):
            roll = random.randint(1, self.sides)
            output.append(roll)

        output = sorted(output)
        if self.kh != -1:
            output = output[-self.kh:]
        elif self.kl != -1:
            output = output[:self.kl]

        for _ in range(len([num for num in output if num == self.e])):
            output += self * 1

        return output


def setup(bot):
    bot.add_cog(DiceRoller(bot))
