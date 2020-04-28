import discord
footer = "D&D 5e SRD Content, All rights and content goes to Wizards.com, Powered by CF8"


async def Barbarian(subclass, sata):
    EmbedList = []
    if not subclass:
        Embed = discord.Embed(title="Class - Barbarian  Pg 1",
                              description=("\n"
                                           "        **Hit Points**\n"
                                           "        Hit Dice: `1d12 per Barbarian level`\n"
                                           "        Hit Points at 1st Level: `12 + your Constitution modifier`\n"
                                           "        Hit Points at Higher Levels: `1d12 (or 7) + your"
                                           " Constitution modifier per Barbarian level after 1st`\n"
                                           "\n"
                                           "\n"
                                           "        **Proficiencies**\n"
                                           "        Armor: `Light Armor, Medium Armor, Shields Weapons: "
                                           "Simple Weapons, Martial Weapons Tools: None`\n"
                                           "        Saving Throws: `Strength, Constitution`\n"
                                           "        Skills: `Choose two from Animal Handling, Athletics,"
                                           " Intimidation, Nature, Perception, and Survival`\n"
                                           "\n"
                                           "\n"
                                           "        **Equipment**\n"
                                           "        You start with the following Equipment, in addition "
                                           "to the Equipment granted by your background:\n"
                                           "\n"
                                           "         •(a) a Greataxe or (b) any martial melee weapon\n"
                                           "         •(a) two handaxes or (b) any simple weapon\n"
                                           "         •An explorer’s pack and four javelins\n"
                                           "                                       "), color=Colour)

        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Barbarian  Pg 2",
                              description="The Barbarian", color=Colour)
        Embed.set_image(url="https://cdn.discordapp.com/attachments/638140888949719080/646040223213551635/1.png")
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Barbarian  Pg 3",
                              description=("\n"
                                           "        **Rage**\n"
                                           "        In battle, you fight with primal ferocity. On Your "
                                           "Turn, you can enter a rage as a Bonus Action.\n"
                                           "\n"
                                           "        While raging, you gain the following benefits if you"
                                           " aren't wearing heavy armor:\n"
                                           "\n"
                                           "        • You have advantage on Strength Checks and Strength"
                                           " Saving Throws.\n"
                                           "\n"
                                           "        • When you make a melee weapon Attack using Strength,"
                                           " you gain a +2 bonus to the damage roll. This bonus increases "
                                           "as you level.\n"
                                           "\n"
                                           "        • You have Resistance to bludgeoning, piercing, and "
                                           "slashing damage.\n"
                                           "\n"
                                           "        If you are able to cast Spells, you can't cast them or "
                                           "concentrate on them while raging.\n"
                                           "\n"
                                           "        Your rage lasts for 1 minute. It ends early if you are "
                                           "knocked Unconscious or if Your Turn ends and you haven't attacked a"
                                           " Hostile creature since your last turn or taken damage since then."
                                           " You can also end your rage on Your Turn as a Bonus Action.\n"
                                           "\n"
                                           "        Once you have raged the maximum number of times for your "
                                           "Barbarian level, you must finish a Long Rest before you can rage "
                                           "again. You may rage 2 times at 1st level, 3 at 3rd, 4 at 6th, 5"
                                           " at 12th, and 6 at 17th.\n"
                                           "                                            "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Barbarian  Pg 4",
                              description=("\n"
                                           "        **Unarmored Defense**\n"
                                           "        While you are not wearing any armor, your Armor Class"
                                           " equals 10 + your Dexterity modifier + your Constitution modifier. "
                                           "You can use a Shield and still gain this benefit.\n"
                                           "\n"
                                           "        **Danger Sense**\n"
                                           "        At 2nd level, you gain an uncanny sense of when things"
                                           " nearby aren't as they should be, giving you an edge when you dodge"
                                           " away from danger. You have advantage on Dexterity Saving Throws "
                                           "against Effects that you can see, such as traps and Spells. To gain "
                                           "this benefit, you can't be Blinded, Deafened, or Incapacitated.\n"
                                           "\n"
                                           "        **Reckless Attack**\n"
                                           "        Starting at 2nd level, you can throw aside all concern "
                                           "for defense to Attack with fierce desperation. When you make your"
                                           " first Attack on Your Turn, you can decide to Attack recklessly. "
                                           "Doing so gives you advantage on melee weapon Attack rolls using "
                                           "Strength during this turn, but Attack rolls against you have advantage "
                                           "until your next turn.\n"
                                           "                                      "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Barbarian  Pg 5",
                              description=("\n"
                                           "        **Primal Path**\n"
                                           "        At 3rd level, you choose a path that shapes the"
                                           " Nature of your rage, such as the Path of the Berserker."
                                           " Your choice grants you features at 3rd level and again "
                                           "at 6th, 10th, and 14th levels.\n"
                                           "\n"
                                           "        **Ability Score Improvement**\n"
                                           "        When you reach 4th level, and again at 8th, 12th,"
                                           " 16th, and 19th level, you can increase one ability score "
                                           "of your choice by 2, or you can increase two Ability Scores"
                                           " of your choice by 1. As normal, you can’t increase an "
                                           "ability score above 20 using this feature.\n"
                                           "\n"                                           
                                           "        **Extra Attack**\n"
                                           "        Beginning at 5th level, you can Attack twice, "
                                           "instead of once, whenever you take the Attack action on Your Turn.\n"
                                           "\n"
                                           "        **Fast Movement**\n"
                                           "        Starting at 5th level, your speed increases by 10 "
                                           "feet while you aren't wearing Heavy Armor.\n"
                                           "                                      "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Barbarian  Pg 6",
                              description=("\n"
                                           "        **Feral Instinct**\n"
                                           "        By 7th level, your instincts are so honed that you have"
                                           " advantage on Initiative rolls.\n"
                                           "\n"
                                           "        Additionally, if you are surprised at the beginning of "
                                           "Combat and aren't Incapacitated, you can act normally on your"
                                           " first turn, but only if you enter your rage before doing anything"
                                           " else on that turn.\n"
                                           "\n"
                                           "        **Brutal Critical**\n"
                                           "        Beginning at 9th level, you can roll one additional weapon "
                                           "damage die when determining the extra damage for a critical hit"
                                           " with a melee Attack.\n"
                                           "\n"
                                           "        This increases to two additional dice at 13th level and "
                                           "three additional dice at 17th level.\n"
                                           "\n"
                                           "        **Relentless Rage**\n"
                                           "        Starting at 11th level, your rage can keep you fighting "
                                           "despite grievous wounds. If you drop to 0 Hit Points while you're "
                                           "raging and don't die outright, you can make a DC 10 Constitution "
                                           "saving throw. If you succeed, you drop to 1 hit point instead.\n"
                                           "\n"
                                           "        Each time you use this feature after the first, "
                                           "the DC increases by 5. When you finish a short or Long Rest, the "
                                           "DC resets to 10.\n"
                                           ""), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Barbarian  Pg 7",
                              description=("\n"
                                           "**Persistent Rage**\n"
                                           "Beginning at 15th level, your rage is so fierce that it ends "
                                           "early only if you fall Unconscious or if you choose to end it.\n"
                                           "\n"
                                           "**Indomitable Might**\n"
                                           "Beginning at 18th level, if your total for a Strength check is "
                                           "less than your Strength score, you can use that score in place "
                                           "of the total.\n"
                                           "\n"
                                           "**Primal Champion**\n"
                                           "At 20th level, you embody the power of the wilds. Your Strength "
                                           "and Constitution scores increase by 4. Your maximum for those scores"
                                           " is now 24.\n"
                                           ""), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Barbarian | Sub-Classes | Pg 8",
                              description="""
**Sub-Classes**
`Path of the Berserker`
                                      """, color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        await ClassPager(EmbedList, Data=sata)


async def Bard(Subclass, Data):
    global Colour
    EmbedList = []
    if not Subclass:
        Embed = discord.Embed(title="Class - Bard  Pg 1",
                              description=("\n"
                                           "**Hit Points**\n"
                                           "Hit Dice: `1d8 per bard level`\n"
                                           "Hit Points at 1st Level: `8 + your Constitution modifier`\n"
                                           "Hit Points at Higher Levels: `1d8 (or 5) + your Constitution"
                                           " modifier per bard level after 1st`\n"
                                           "\n"
                                           "**Starting Proficiencies**\n"
                                           "You are proficient with the following items, in addition "
                                           "to any proficiencies provided by your race or Background.\n"
                                           "\n"
                                           "**Armor: Light Armor**\n"
                                           "Weapons: `Simple Weapons, hand crossbows, longswords, "
                                           "rapiers, shortswords`\n"
                                           "Tools: `three Musical Instruments of your choice`\n"
                                           "Saving `Throws: Dexterity, Charisma`\n"
                                           "Skills: `Choose any three.`\n"
                                           "\n"
                                           "**Starting Equipment**\n"
                                           "You start with the following items, plus anything provided"
                                           " by your Background.\n"
                                           "\n"
                                           "• (a) a Rapier, (b) a Longsword, or (c) any simple weapon\n"
                                           "• (a) a Diplomat's Pack or (b) an Entertainer's Pack\n"
                                           "• (a) a lute or (b) any other musical instrument\n"
                                           "• Leather Armor, and a Dagger                \n"
                                           ""), color=Colour)

        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Bard  Pg 2",
                              description="Table: The Bard ", color=Colour)
        Embed.set_image(url="https://cdn.discordapp.com/attachments/638140888949719080/646405274701266949/2.png")
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Bard  Pg 3",
                              description=("\n"
                                           "**Bardic Inspiration**\n"
                                           "You can inspire others through stirring words or music."
                                           "To do so, you use a Bonus Action on Your Turn to choose "
                                           "one creature other than yourself within 60 feet of you who "
                                           "can hear you. That creature gains one Bardic Inspiration die, a d6.\n"
                                           "\n"
                                           "Once within the next 10 minutes, the creature can roll "
                                           "the die and add the number rolled to one ability check,"
                                           " Attack roll, or saving throw it makes. The creature can"
                                           " wait until after it rolls The D20 before deciding to use"
                                           " the Bardic Inspiration die, but must decide before the"
                                           " DM says whether the roll succeeds or fails. Once the Bardic "
                                           "Inspiration die is rolled, it is lost. A creature can have "
                                           "only one Bardic Inspiration die at a time.\n"
                                           "\n"
                                           "You can use this feature a number of times equal to your"
                                           " Charisma modifier (a minimum of once). You regain any "
                                           "expended uses when you finish a Long Rest.\n"
                                           "\n"
                                           "Your Bardic Inspiration die changes when you reach certain "
                                           "levels in this class. The die becomes a d8 at 5th level, a "
                                           "d10 at 10th level, and a d12 at 15th level.               \n"
                                           ""), color=Colour)

        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Bard  Pg 4",
                              description=("\n"
                                           "**Spellcasting**\n"
                                           "You have learned to untangle and reshape the fabric of reality "
                                           "in harmony with your wishes and music. Your Spells are part of"
                                           " your vast repertoire, magic that you can tune to different "
                                           "situations. See chapter 10 for the general rules of Spellcasting"
                                           " and chapter 11 for the bard spell list.\n"
                                           "\n"
                                           "**Cantrips**\n"
                                           "\n"
                                           "You know two Cantrips of your choice from the bard spell list."
                                           " You learn additional bard Cantrips of your choice at higher "
                                           "levels, learning a 3rd cantrip at 4th level and a 4th at 10th level.\n"
                                           "\n"
                                           "**Spell Slots**\n"
                                           "\n"
                                           "The Bard table shows how many Spell Slots you have to cast "
                                           "your Spells of 1st level and higher. To cast one of these Spells, "
                                           "you must expend a slot of the spell's level or higher. You regain"
                                           " all expended Spell Slots when you finish a Long Rest.\n"
                                           "\n"
                                           "For example, if you know the 1st-level spell Cure Wounds "
                                           "and have a 1st-level and a 2nd-level spell slot available, "
                                           "you can cast Cure Wounds using either slot.\n"
                                           ""), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Bard  Pg 5",
                              description=("\n"
                                           "**Spells Known of 1st Level and Higher**\n"
                                           "\n"
                                           "You know four 1st-level Spells of your choice from the bard spell list.\n"
                                           "\n"
                                           "You learn an additional bard spell of your choice at each "
                                           "level except 12th, 16th, 19th, and 20th. Each of these Spells"
                                           " must be of a level for which you have Spell Slots. For instance,"
                                           " when you reach 3rd level in this class, you can learn one new"
                                           " spell of 1st or 2nd level.\n"
                                           "\n"
                                           "Additionally, when you gain a level in this class, you can "
                                           "choose one of the Bard Spells you know and replace it with another "
                                           "spell from the bard spell list, which also must be of a level for"
                                           " which you have Spell Slots.\n"
                                           "\n"
                                           "**Spellcasting Ability**\n"
                                           "\n"
                                           "Charisma is your Spellcasting Ability for your Bard Spells."
                                           " Your magic comes from the heart and soul you pour into the"
                                           " Performance of your music or oration. You use your Charisma "
                                           "whenever a spell refers to your Spellcasting Ability. "
                                           "In addition, you use your Charisma modifier when setting "
                                           "the saving throw DC for a bard spell you cast and when "
                                           "Making an Attack roll with one.\n"
                                           "\n"
                                           "`Spell save DC = 8 + your Proficiency Bonus + your Charisma "
                                           "modifier`\n"
                                           "`Spell Attack modifier = your Proficiency Bonus + your "
                                           "Charisma modifier`\n"
                                           "\n"
                                           "**Ritual Casting**\n"
                                           "\n"
                                           "You can cast any bard spell you know as a ritual if that"
                                           " spell has the ritual tag.\n"
                                           "\n"
                                           "**Spellcasting Focus**\n"
                                           "\n"
                                           "You can use a musical instrument (see \"Equipment\") as a "
                                           "Spellcasting focus for your Bard Spells.                              \n"
                                           "                              "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Bard  Pg 6",
                              description=("\n"
                                           "**Jack of All Trades**\n"
                                           "Starting at 2nd level, you can add half your Proficiency Bonus,"
                                           " rounded down, to any ability check you make that doesn't "
                                           "already include your Proficiency Bonus.\n"
                                           "\n"
                                           "**Song of Rest**\n"
                                           "Beginning at 2nd level, you can use soothing music or oration"
                                           " to help revitalize your wounded allies during a Short Rest. "
                                           "If you or any friendly creatures who can hear your Performance"
                                           " regain Hit Points by spending Hit Dice at the end of the Short"
                                           " Rest, each of those creatures regains an extra 1d6 Hit Points.\n"
                                           "\n"
                                           "The extra Hit Points increase when you reach certain levels in "
                                           "this class: to 1d8 at 9th level, to 1d10 at 13th level, and to "
                                           "1d12 at 17th level.\n"
                                           "\n"
                                           "**Bard College**\n"
                                           "At 3rd level, you delve into the advanced Techniques of a bard "
                                           "college of your choice, such as the College of Lore. Your choice "
                                           "grants you features at 3rd level and again at 6th and 14th level.\n"
                                           "                          "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Bard  Pg 7",
                              description=("\n"
                                           "**Expertise**\n"
                                           "At 3rd level, choose two of your skill proficiencies."
                                           " Your Proficiency Bonus is doubled for any ability check "
                                           "you make that uses either of the chosen proficiencies.\n"
                                           "\n"
                                           "At 10th level, you can choose another two skill "
                                           "proficiencies to gain this benefit.\n"
                                           "\n"
                                           "**Ability Score Improvement**\n"
                                           "When you reach 4th level, and again at 8th, 12th, "
                                           "16th, and 19th level, you can increase one ability score of "
                                           "your choice by 2, or you can increase two Ability Scores of "
                                           "your choice by 1. As normal, you can’t increase an ability "
                                           "score above 20 using this feature.\n"
                                           "\n"
                                           "**Font of Inspiration**\n"
                                           "Beginning when you reach 5th level, you regain all "
                                           "of your expended uses of Bardic Inspiration when you finish a "
                                           "short or Long Rest.                              \n"
                                           "                              "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Bard  Pg 8",
                              description=("\n"
                                           "**Countercharm**\n"
                                           "At 6th level, you gain the ability to use musical "
                                           "notes or words of power to disrupt mind-influencing "
                                           "Effects. As an action, you can start a Performance "
                                           "that lasts until the end of your next turn. During "
                                           "that time, you and any friendly creatures within 30 "
                                           "feet of you have advantage on Saving Throws against "
                                           "being Frightened or Charmed. A creature must be able "
                                           "to hear you to gain this benefit. The Performance ends"
                                           " early if you are Incapacitated or silenced or if you "
                                           "voluntarily end it (no action required).\n"
                                           "\n"
                                           "**Magical Secrets**\n"
                                           "By 10th level, you have plundered magical knowledge f"
                                           "rom a wide spectrum of disciplines. Choose two Spells "
                                           "from any class, including this one. A spell you choose "
                                           "must be of a level you can cast, as shown on the Bard table,"
                                           " or a cantrip.\n"
                                           "\n"                                           
                                           "The chosen Spells count as Bard Spells for you and are "
                                           "included in the number in the Spells Known column of the Bard table.\n"
                                           "\n"
                                           "You learn two additional Spells from any class at 14th "
                                           "level and again at 18th level.\n"
                                           "\n"
                                           "**Superior Inspiration**\n"
                                           "At 20th level, when you roll Initiative and have no "
                                           "uses of Bardic Inspiration left, you regain one use.                              \n"
                                           "                    "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Bard | Colleges | Pg 8",
                              description=("\n"
                                           "`College of Lore`\n"
                                           "`College of Eloquence (UA)`\n"
                                           "`College of Glamour`\n"
                                           "`College of Whispers`\n"
                                           "                    "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        return EmbedList


async def Cleric(Subclass, Data):
    global Colour
    EmbedList = []
    if not Subclass:
        Embed = discord.Embed(title="Class - Cleric  Pg 1",
                              description=("\n"
                                           "**Hit Points**\n"
                                           "Hit Dice: `1d8 per Cleric level`\n"
                                           "Hit Points at 1st Level: `8 + your Constitution modifier`\n"
                                           "Hit Points at Higher Levels: `1d8 (or 5) + your Constitution"
                                           " modifier per Cleric level after 1st`\n"
                                           "\n"                                           
                                           "**Starting Proficiencies**\n"
                                           "You are proficient with the following items, in addition to any "
                                           "proficiencies provided by your race or Background.\n"
                                           "\n"
                                           "Armor: `Light Armor, Medium Armor, Shields`\n"
                                           "Weapons: `Simple Weapons`\n"
                                           "Tools: `none`\n"
                                           "Saving Throws: `Wisdom, Charisma`\n"
                                           "Skills: `Choose two from History, Insight, Medicine, Persuasion,"
                                           " and Religion`\n"
                                           "\n"
                                           "**Starting Equipment**\n"
                                           "You start with the following items, plus anything provided by "
                                           "your Background.\n"
                                           "\n"
                                           "• (a) a mace or (b) a Warhammer (if proficient)\n"
                                           "• (a) Scale Mail, (b) Leather Armor, or (c) Chain Mail (if proficient)\n"
                                           "• (a) a Light Crossbow and 20 bolts or (b) any simple weapon\n"
                                           "• (a) a Priest's Pack or (b) an Explorer's Pack\n"
                                           "• A Shield and a holy Symbol\n"
                                           "                            "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Cleric  Pg 2",
                              description="Table: The Cleric ", color=Colour)
        Embed.set_image(url="https://cdn.discordapp.com/attachments/638140888949719080/646412368188014610/3.png")
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Cleric  Pg 3",
                              description=("\n"
                                           "**Spellcasting**\n"
                                           "As a conduit for divine power, you can cast Cleric Spells. See "
                                           "chapter 10 for the general rules of Spellcasting and chapter "
                                           "11 for a selection of Cleric Spells.\n"
                                           "\n"
                                           "**Cantrips**\n"
                                           "\n"
                                           "At 1st level, you know three Cantrips of your choice from the "
                                           "Cleric spell list. You learn additional Cleric Cantrips of your"
                                           " choice at higher levels, as shown in the Cantrips Known column of the Cleric table.\n"
                                           "\n"
                                           "**Preparing and Casting Spells**\n"
                                           "\n"
                                           "The Cleric table shows how many Spell Slots you have to cast your"
                                           " Spells of 1st level and higher. To cast one of these Spells, you"
                                           " must expend a slot of the spell's level or higher. You regain all"
                                           " expended Spell Slots when you finish a Long Rest.\n"
                                           "\n"
                                           "You prepare the list of Cleric Spells that are available for you to"
                                           " cast, choosing from the Cleric spell list. When you do so, choose a"
                                           " number of Cleric Spells equal to your Wisdom modifier + your Cleric "
                                           "level (minimum of one spell). The Spells must be of a level for which "
                                           "you have Spell Slots.\n"
                                           "\n"
                                           "For example, if you are a 3rd-level Cleric, you have four 1st-level "
                                           "and two 2nd-level Spell Slots. With a Wisdom of 16, your list of prepared"
                                           " Spells can include six Spells of 1st or 2nd level, in any combination."
                                           " If you prepare the 1st-level spell Cure Wounds, you can cast it using "
                                           "a 1st-level or 2nd-level slot. Casting the spell doesn't remove it "
                                           "from your list of prepared Spells.\n"
                                           "\n"
                                           "You can change your list of prepared Spells when you finish a Long "
                                           "Rest. Preparing a new list of Cleric Spells requires time spent in "
                                           "prayer and meditation: at least 1 minute per Spell Level for each "
                                           "spell on your list.\n"
                                           "                                    "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Cleric  Pg 4",
                              description=("\n"
                                           "**Spellcasting Ability**\n"
                                           "\n"
                                           "Wisdom is your Spellcasting Ability for your Cleric Spells. "
                                           "The power of your Spells comes from your devotion to your deity. "
                                           "You use your Wisdom whenever a Cleric spell refers to your "
                                           "Spellcasting Ability. In addition, you use your Wisdom modifier"
                                           " when setting the saving throw DC for a Cleric spell you "
                                           "cast and when Making an Attack roll with one.\n"
                                           "\n"
                                           "`Spell save DC = 8 + your Proficiency Bonus + your Wisdom "
                                           "modifier`\n"
                                           "`Spell Attack modifier = your Proficiency Bonus + your Wisdom "
                                           "modifier`\n"
                                           "\n"
                                           "**Ritual Casting**\n"
                                           "\n"
                                           "You can cast a Cleric spell as a ritual if that spell has the "
                                           "ritual tag and you have the spell prepared.\n"
                                           "\n"
                                           "**Spellcasting Focus**\n"
                                           "\n"
                                           "You can use a holy Symbol (see \"Equipment\") as a "
                                           "Spellcasting focus for your Cleric Spells.\n"
                                           "                     "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Cleric  Pg 5",
                              description=("\n"
                                           "**Divine Domain**\n"
                                           "Choose one domain related to your deity, such as Life. "
                                           "The Life Domain is detailed at the end of the class "
                                           "description, and provides examples of gods associated "
                                           "with it. Your choice grants you Domain Spells and other"
                                           " features when you choose it at 1st level. It also grants"
                                           " you additional ways to use Channel Divinity when you gain"
                                           " that feature at 2nd level, and additional benefits at 6th,"
                                           " 8th, and 17th levels.\n"
                                           "\n"
                                           "**Domain Spells**\n"
                                           "\n"
                                           "Each domain has a list of spells-its domain spells-that "
                                           "you gain at the Cleric levels noted in the domain description."
                                           " Once you gain a domain spell, you always have it prepared, "
                                           "and it doesn't count against the number of Spells you can "
                                           "prepare each day.\n"
                                           "\n"
                                           "If you have a domain spell that doesn't appear on the "
                                           "Cleric spell list, the spell is nonetheless a Cleric spell "
                                           "for you.\n"
                                           "                    "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Cleric  Pg 6",
                              description=("\n"
                                           "**Channel Divinity**\n"
                                           "At 2nd level, you gain the ability to channel divine energy "
                                           "directly from your deity, using that energy to fuel magical "
                                           "Effects. You start with two such effects: Turn Undead and an"
                                           " effect determined by your domain. Some domains grant you "
                                           "additional Effects as you advance in levels, as noted in the"
                                           " domain description.\n"
                                           "\n"
                                           "When you use your Channel Divinity, you choose which effect"
                                           " to create. You must then finish a short or Long Rest to use"
                                           "your Channel Divinity again.\n"
                                           "\n"
                                           "Some Channel Divinity Effects require Saving Throws. When "
                                           "you use such an effect from this class, the DC equals your "
                                           "Cleric spell save DC.\n"
                                           "\n"
                                           "Beginning at 6th level, you can use your Channel Divinity "
                                           "twice between rests, and beginning at 18th level, you can "
                                           "use it three times between rests. When you finish a short "
                                           "or Long Rest, you regain your expended uses.\n"
                                           "                            "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Cleric  Pg 7",
                              description=("\n"
                                           "**Channel Divinity: Turn Undead**\n"
                                           "As an action, you present your holy Symbol and speak a prayer "
                                           "censuring the Undead. Each Undead that can see or hear you within"
                                           " 30 feet of you must make a Wisdom saving throw. If the creature "
                                           "fails its saving throw, it is turned for 1 minute or until it "
                                           "takes any damage.\n"
                                           "\n"
                                           "A turned creature must spend its turns trying to move as far away "
                                           "from you as it can, and it can't willingly move to a space within "
                                           "30 feet of you. It also can't take reactions. For its action, it "
                                           "can use only the Dash action or try to escape from an effect that "
                                           "prevents it from moving. If there's nowhere to move, the creature"
                                           "can use the Dodge action.\n"
                                           "                    "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Cleric  Pg 8",
                              description=("\n"
                                           "**Ability Score Improvement**\n"
                                           "When you reach 4th level, and again at 8th, 12th, 16th,"
                                           " and 19th level, you can increase one ability score of "
                                           "your choice by 2, or you can increase two Ability Scores "
                                           "of your choice by 1. As normal, you can’t increase an "
                                           "ability score above 20 using this feature.\n"
                                           "\n"
                                           "**Destroy Undead**\n"
                                           "Starting at 5th level, when an Undead of CR 1/2 or lower "
                                           "fails its saving throw against Your Turn Undead feature, "
                                           "the creature is instantly destroyed.\n"
                                           "\n"
                                           "**Divine Intervention**\n"
                                           "Beginning at 10th level, you can call on your deity to "
                                           "intervene on your behalf when your need is great.\n"
                                           "\n"
                                           "Imploring your deity's aid requires you to use your action. "
                                           "Describe the assistance you seek, and roll percentile dice."
                                           " If you roll a number equal to or lower than your Cleric level,"
                                           " your deity intervenes. The DM chooses the Nature of the "
                                           "intervention; the effect of any Cleric spell or Cleric domain "
                                           "spell would be appropriate. If your deity intervenes, you can't"
                                           " use this feature again for 7 days. Otherwise, you can use it "
                                           "again after you finish a Long Rest.\n"
                                           "\n"
                                           "At 20th level, your call for intervention succeeds automatically,"
                                           " no roll required.\n"
                                           ""), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Cleric  Pg 9",
                              description=("\n"
                                           "**Ability Score Improvement**\n"
                                           "When you reach 4th level, and again at 8th, 12th, 16th, and 19th "
                                           "level, you can increase one ability score of your choice by 2,"
                                           " or you can increase two Ability Scores of your choice by 1. "
                                           "As normal, you can’t increase an ability score above 20 using "
                                           "this feature.\n"
                                           "\n"
                                           "**Destroy Undead**\n"
                                           "Starting at 5th level, when an Undead of CR 1/2 or lower fails "
                                           "its saving throw against Your Turn Undead feature, the creature"
                                           " is instantly destroyed.\n"
                                           "\n"
                                           "**Divine Intervention**\n"
                                           "Beginning at 10th level, you can call on your deity to "
                                           "intervene on your behalf when your need is great.\n"
                                           "\n"
                                           " Imploring your deity's aid requires you to use your"
                                           " action. Describe the assistance you seek, and roll"
                                           " percentile dice. If you roll a number equal to or "
                                           "lower than your Cleric level, your deity intervenes. "
                                           "The DM chooses the Nature of the intervention; the "
                                           "effect of any Cleric spell or Cleric domain spell would "
                                           "be appropriate. If your deity intervenes, you can't use "
                                           "this feature again for 7 days. Otherwise, you can use it "
                                           "again after you finish a Long Rest.\n"
                                           "\n"
                                           "At 20th level, your call for intervention succeeds"
                                           "automatically, no roll required.                              \n"
                                           ""), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Cleric | Domains | Pg 10",
                              description=("\n"
                                           "`Life Domain`\n"
                                           "`Arcana`\n"
                                           "`Death`\n"
                                           "`Forge`\n"
                                           "`Grave`\n"
                                           "`Light`\n"
                                           "`Protection (UA)`\n"
                                           "`Tempest`\n"
                                           "`War`\n"
                                           "`Trickery`\n"
                                           "`Knowledge`\n"
                                           ""), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        return EmbedList


async def Druid(Subclass, Data):
    global Colour
    EmbedList = []
    if not Subclass:
        Embed = discord.Embed(title="Class - Druid  Pg 1 / 11",
                              description=("\n"
                                           "**Hit Points**\n"
                                           "Hit Dice: `1d8 per druid level`\n"
                                           "Hit Points at 1st Level: `8 + your Constitution modifier`\n"
                                           "Hit Points at Higher Levels: `1d8 (or 5) + your Constitution"
                                           " modifier per druid level after 1st`\n"
                                           "\n"
                                           "**Starting Proficiencies**\n"
                                           "You are proficient with the following items, in addition to any "
                                           "Proficiencies provided by your race or Background.\n"
                                           "\n"
                                           "Armor: `Light Armor, Medium Armor, Shields (druids will not wear"
                                           " armor or use Shields made of metal)`\n"
                                           "Weapons: `clubs, daggers, darts, javelins, maces, quarterstaffs,"
                                           " scimitars, sickles, slings, spears`\n"
                                           "Tools: `Herbalism Kit`\n"
                                           "Saving Throws: `Intelligence, Wisdom`\n"
                                           "Skills: `Choose two from Arcana, Animal Handling, Insight,"
                                           " Medicine, Nature, Perception, Religion, and Survival`\n"
                                           "\n"
                                           "**Starting Equipment**\n"
                                           "You start with the following items, plus anything provided "
                                           "by your Background.\n"
                                           "\n"
                                           "• (a) a Wooden Shield or (b) any simple weapon\n"
                                           "• (a) a Scimitar or (b) any simple melee weapon\n"
                                           "• Leather Armor, an Explorer's Pack, and a druidic focus\n"
                                           "\n"
                                           ""), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Druid  Pg 2 / 11",
                              description="Table: The Druid ", color=Colour)
        Embed.set_image(url="https://cdn.discordapp.com/attachments/638140888949719080/646467680320356393/4.png")
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Druid  Pg 3 / 11",
                              description=("\n"
                                           "**Druidic**\n"
                                           "You know Druidic, the Secret language of druids. "
                                           "You can speak the language and use it to leave "
                                           "hidden messages. You and others who know this "
                                           "language automatically spot such a Message. "
                                           "Others spot the message's presence with a successful "
                                           "DC 15 Wisdom (Perception) check but can't decipher"
                                           " it without magic.\n"), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Druid  Pg 4 / 11",
                              description=("\n"
                                           "**Spellcasting**\n"
                                           "Drawing on the divine essence of Nature itself, you can cast"
                                           " Spells to shape that essence to your will. See chapter 10 for "
                                           "the general rules of Spellcasting and chapter 11 for the druid "
                                           "spell list.\n"
                                           "\n"
                                           "**Cantrips**\n"
                                           "\n"
                                           "At 1st level, you know two Cantrips of your choice from the"
                                           " druid spell list. You learn additional druid Cantrips of your "
                                           "choice at higher levels, as shown in the Cantrips Known column "
                                           "of the Druid table.\n"
                                           "\n"
                                           "**Preparing and Casting Spells**\n"
                                           "\n"
                                           "The Druid table shows how many Spell Slots you have to"
                                           " cast your Spells of 1st level and higher. To cast one of these "
                                           "Druid Spells, you must expend a slot of the spell's level or higher."
                                           " You regain all expended Spell Slots when you finish a Long Rest.\n"
                                           "\n"
                                           "You prepare the list of Druid Spells that are available "
                                           "for you to cast, choosing from the druid spell list. When you do so,"
                                           " choose a number of Druid Spells equal to your Wisdom modifier +"
                                           " your druid level (minimum of one spell). The Spells must be of "
                                           "a level for which you have Spell Slots.\n"
                                           "\n"
                                           "For example, if you are a 3rd-level druid, you have four "
                                           "1st-level and two 2nd-level Spell Slots. With a Wisdom of 16, your "
                                           "list of prepared Spells can include six Spells of 1st or 2nd level,"
                                           " in any combination. If you prepare the 1st-level spell Cure Wounds,"
                                           " you can cast it using a 1st-level ar 2nd-level slot. Casting the "
                                           "spell doesn't remove it from your list of prepared Spells.\n"
                                           "\n"
                                           "You can also change your list of prepared Spells when you"
                                           " finish a Long Rest. Preparing a new list of Druid Spells requires"
                                           " time spent in prayer and meditation: at least 1 minute per Spell "
                                           "Level for each spell on your list.\n"
                                           ""), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Druid  Pg 5 / 11",
                              description=("\n"
                                           "**Spellcasting Ability**\n"
                                           "\n"
                                           "Wisdom is your Spellcasting Ability for your Druid Spells,"
                                           " since your magic draws upon your devotion and Attunement "
                                           "to Nature. You use your Wisdom whenever a spell refers to"
                                           " your Spellcasting Ability. In addition, you use your Wisdom"
                                           " modifier when setting the saving throw DC for a druid spell "
                                           "you cast and when Making an Attack roll with one.\n"
                                           "\n"
                                           "`Spell save DC = 8 + your Proficiency Bonus + your Wisdom modifier`\n"
                                           "`Spell Attack modifier = your Proficiency Bonus + your Wisdom modifier`\n"
                                           "\n"
                                           "**Ritual Casting**\n"
                                           "\n"
                                           "You can cast a druid spell as a ritual if that spell has the ritual "
                                           "tag and you have the spell prepared.\n"
                                           "\n"
                                           "**Spellcasting Focus**\n"
                                           "\n"
                                           "You can use a druidic focus (see \"Equipment\") as a Spellcasting "
                                           "focus for your Druid Spells.\n"
                                           "                            "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Druid  Pg 6 / 11",
                              description=("\n"
                                           "**Wild Shape**\n"
                                           "Starting at 2nd level, you can use your action to magically"
                                           " assume the shape of a beast that you have seen before."
                                           " You can use this feature twice. You regain expended uses"
                                           " when you finish a short or Long Rest.\n"
                                           "\n"
                                           "Your druid level determines the Beasts you can transform "
                                           "into, as shown in the Beast Shapes table. At 2nd level,"
                                           " for example, you can transform into any beast that has a "
                                           "Challenge rating of 1/4 or lower that doesn't have a flying"
                                           " or swimming speed.\n"
                                           " "), color=Colour)
        Embed.set_image(url="https://cdn.discordapp.com/attachments/638140888949719080/646468623376056340/4-2.png")
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Druid | Beast Shape Part 1 | Pg 7 / 11",
                              description=("\n"
                                           "You can stay in a beast shape for a number of hours equal to half"
                                           " your druid level (rounded down). You then revert to your normal "
                                           "form unless you expend another use of this feature. You can rever"
                                           "t to your normal form earlier by using a Bonus Action on Your Turn"
                                           ". You automatically revert if you fall Unconscious, drop to 0 Hit"
                                           " Points, or die.\n"
                                           "\n"
                                           "While you are transformed, the following rules apply:\n"
                                           "\n"
                                           "• Your game Statistics are replaced by the Statistics of the beast,"
                                           " but you retain your Alignment, personality, and Intelligence, Wisdom,"
                                           " and Charisma scores. You also retain all of your skill and saving throw"
                                           " Proficiencies, in addition to gaining those of the creature. If the "
                                           "creature has the same proficiency as you and the bonus in its stat"
                                           " block is higher than yours, use the creature's bonus instead of yours."
                                           " If the creature has any legendary or Lair Actions, you can't use them.\n"
                                           "• When you transform, you assume the beast's Hit Points and Hit Dice. "
                                           "When you revert to your normal form, you return to the number of Hit "
                                           "Points you had before you transformed. However, if you revert as a "
                                           "result of Dropping to 0 Hit Points, any excess damage carries over to "
                                           "your normal form. For example, if you take 10 damage in animal form "
                                           "and have only 1 hit point left, you revert and take 9 damage. As long "
                                           "as the excess damage doesn't reduce your normal form to 0 Hit Points,"
                                           " you aren't knocked Unconscious.\n"
                                           " "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Druid | Beast Shape Part 2 |  Pg 8 / 11",
                              description=("\n"
                                           "• You can't cast Spells, and your ability to speak or take any action"
                                           " that requires hands is limited to the capabilities of your beast form."
                                           " Transforming doesn't break your Concentration on a spell you've already"
                                           " cast, however, or prevent you from taking Actions that are part of a"
                                           " spell, such as Call Lightning, that you've already cast.\n"
                                           "• You retain the benefit of any features from your class, race, or "
                                           "other source and can use them if the new form is physically capable of "
                                           "doing so. However, you can't use any of your Special Senses, such as "
                                           "Darkvision, unless your new form also has that sense.\n"
                                           "• You choose whether your Equipment falls to the ground in your space,"
                                           " merges into your new form, or is worn by it. Worn Equipment functions"
                                           " as normal, but the DM decides whether it is practical for the new form "
                                           "to wear a piece of Equipment, based on the creature's shape and size. "
                                           "Your Equipment doesn't change size or shape to match the new form, and "
                                           "any Equipment that the new form can't wear must either fall to the ground "
                                           "or merge with it. Equipment that merges with the form has no effect until "
                                           "you leave the form.\n"
                                           "                                "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Druid  Pg 9 / 11",
                              description=("\n"
                                           "**Druid Circle**\n"
                                           "At 2nd level, you choose to Identify with a circle of druids,"
                                           " such as the Circle of the Land. Your choice grants you features"
                                           " at 2nd level and again at 6th, 10th, and 14th level.\n"
                                           "\n"
                                           "**Ability Score Improvement**\n"
                                           "When you reach 4th level, and again at 8th, 12th, 16th, and 19th "
                                           "level, you can increase one ability score of your choice by 2, or "
                                           "you can increase two Ability Scores of your choice by 1. As normal,"
                                           " you can’t increase an ability score above 20 using this feature.\n"
                                           "\n"
                                           "**Timeless Body**\n"
                                           "Starting at 18th level, the primal magic that you wield causes you "
                                           "to age more slowly. For every 10 years that pass, your body ages "
                                           "only 1 year.\n"
                                           "\n"
                                           "                            "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Druid  Pg 10 / 11",
                              description=("\n"
                                           "**Beast Spells**\n"
                                           "Beginning at 18th level, you can cast many of your Druid Spells"
                                           " in any shape you assume using Wild Shape. You can perform the "
                                           "somatic and verbal Components of a druid spell while in a beast"
                                           " shape, but you aren't able to provide material Components.\n"
                                           "\n"
                                           "**Archdruid**\n"
                                           "At 20th level, you can use your Wild Shape an unlimited number "
                                           "of times.\n"
                                           "\n"
                                           "Additionally, you can ignore the verbal and somatic Components"
                                           " of your Druid Spells, as well as any material Components that "
                                           "lack a cost and aren't consumed by a spell. You gain this benefit "
                                           "in both your normal shape and your beast shape from Wild Shape.\n"
                                           "                                    "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Druid | Domains | Pg 11 / 11",
                              description="""
        `Circle of the moon`     
        `Circle of the land`                               
                                    """, color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        return EmbedList


async def Fighter(Subclass, Data):
    global Colour
    EmbedList = []
    if not Subclass:
        Embed = discord.Embed(title="Class - Fighter  Pg 1 / 6",
                              description=("\n"
                                           "**Hit Points**\n"
                                           "Hit Dice: `1d10 per Fighter level`   \n"
                                           "Hit Points at 1st Level: `10 + your Constitution modifier`\n"
                                           "Hit Points at Higher Levels: `1d10 (or 6) + your Constitution"
                                           " modifier per Fighter level after 1st`\n"
                                           "\n"
                                           "**Starting Proficiencies**\n"
                                           "You are proficient with the following items, in addition to "
                                           "any Proficiencies provided by your race or Background.\n"
                                           "\n"
                                           "Armor: `Light Armor, Medium Armor, Heavy Armor, Shields`\n"
                                           "Weapons: `Simple Weapons, Martial Weapons`\n"
                                           "Tools: `none`\n"
                                           "Saving `Throws: Strength, Constitution`\n"
                                           "Skills: `Choose two Skills from Acrobatics, Animal Handling,"
                                           " Athletics, History, Insight, Intimidation, Perception, and Survival`\n"
                                           "\n"
                                           "**Starting Equipment**\n"
                                           "You start with the following items, plus anything provided"
                                           " by your Background.\n"
                                           "\n"
                                           "• (a) Chain Mail or (b) leather, Longbow, and 20 Arrows\n"
                                           "• (a) a martial weapon and a Shield or (b) two Martial Weapons\n"
                                           "• (a) a Light Crossbow and 20 bolts or (b) two handaxes\n"
                                           "• (a) a Dungeoneer's Pack or (b) an Explorer's Pack\n"
                                           "                                            "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Fighter  Pg 2 / 6",
                              description="Table: The Fighter ", color=Colour)
        Embed.set_image(url="https://cdn.discordapp.com/attachments/638140888949719080/647795178350051348/5.png")
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Fighter  Pg 3 / 6",
                              description=("\n"
                                           "**Fighting Style**\n"
                                           "You adopt a particular style of fighting as your specialty. "
                                           "Choose a Fighting Style from the list of optional features. "
                                           "You can't take the same Fighting Style option more than once,"
                                           " even if you get to choose again.\n"
                                           "**Archery**\n"
                                           "You gain a +2 bonus to Attack rolls you make with Ranged Weapons.\n"
                                           "\n"
                                           "**Defense**\n"
                                           "While you are wearing armor, you gain a +1 bonus to AC.\n"
                                           "\n"
                                           "**Dueling**\n"
                                           "When you are wielding a melee weapon in one hand and no"
                                           " other Weapons, you gain a +2 bonus to Damage Rolls with that weapon.\n"
                                           "\n"
                                           "**Great Weapon Fighting**\n"
                                           "When you roll a 1 or 2 on a damage die for an Attack you "
                                           "make with a melee weapon that you are wielding with two hands, "
                                           "you can reroll the die and must use the new roll, even if the n"
                                           "ew roll is a 1 or a 2. The weapon must have the Two-Handed or"
                                           " Versatile property for you to gain this benefit.\n"
                                           "\n"
                                           "**Protection**\n"
                                           "When a creature you can see attacks a target other than"
                                           " you that is within 5 feet of you, you can use your Reaction to "
                                           "impose disadvantage on the Attack roll. You must be wielding a "
                                           "Shield.\n"
                                           "\n"
                                           "**Two-Weapon Fighting**\n"
                                           "When you engage in two-weapon fighting, you can add your "
                                           "ability modifier to the damage of the second Attack.\n"), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Fighter  Pg 4 / 6",
                              description=("\n"
                                           "**Second Wind**\n"
                                           "You have a limited well of stamina that you can draw on "
                                           "to protect yourself from harm. On Your Turn, you can use "
                                           "a Bonus Action to regain Hit Points equal to 1d10 + your"
                                           " Fighter level.\n"
                                           "\n"
                                           "Once you use this feature, you must finish a short or "
                                           "Long Rest before you can use it again.\n"
                                           "\n"
                                           "**Action Surge**\n"
                                           "Starting at 2nd level, you can push yourself beyond your "
                                           "normal limits for a moment. On Your Turn, you can take one"
                                           " additional action on top of your regular action and a "
                                           "possible Bonus Action.\n"
                                           "\n"
                                           "Once you use this feature, you must finish a short or "
                                           "Long Rest before you can use it again. Starting at 17th "
                                           "level, you can use it twice before a rest, but only once"
                                           " on the same turn. "),
                              color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Fighter  Pg 5 / 6",
                              description=("\n"
                                           "**Martial Archetype**\n"
                                           "At 3rd level, you choose an archetype that you strive"
                                           " to emulate in your Combat styles and Techniques, such as"
                                           " Champion. The archetype you choose grants you features at "
                                           "3rd level and again at 7th, 10th, 15th, and 18th level.\n"
                                           "\n"
                                           "**Ability Score Improvement**\n"
                                           "When you reach 4th level, and again at 6th, 8th, 12th,"
                                           " 14th, 16th, and 19th level, you can increase one ability "
                                           "score of your choice by 2, or you can increase two Ability "
                                           "Scores of your choice by 1. As normal, you can’t increase an"
                                           " ability score above 20 using this feature.\n"
                                           "\n"
                                           "**Extra Attack**\n"
                                           "Beginning at 5th level, you can Attack twice, instead "
                                           "of once, whenever you take the Attack action on Your Turn.\n"
                                           "\n"
                                           "The number of attacks increases to three when you"
                                           " reach 11th level in this class and to four when you reach"
                                           " 20th level in this class.\n"
                                           "\n"
                                           "**Indomitable**\n"
                                           "Beginning at 9th level, you can reroll a saving "
                                           "throw that you fail. If you do so, you must use the new roll,"
                                           " and you can't use this feature again until you finish a Long Rest.\n"
                                           "\n"
                                           "You can use this feature twice between long rests starting at"
                                           " 13th level and three times between long rests starting at 17th level."),
                              color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Fighter | Martial Archetypes | Pg 6 / 6",
                              description="""
                `Champion`
                `Gunslinger`     
                `Rune Knight (UA)`                               
                                            """, color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        return EmbedList


async def Monk(Subclass, Data):
    global Colour
    EmbedList = []
    if not Subclass:
        Embed = discord.Embed(title="Class - Monk  Pg 1 / 12",
                              description=("\n"
                                           "**Hit Points**\n"
                                           "Hit Dice: `1d8 per monk level`\n"
                                           "Hit Points at 1st Level: `8 + your Constitution modifier`\n"
                                           "Hit Points at Higher Levels: `1d8 (or 5) + your "
                                           "Constitution modifier per monk level after 1st`\n"
                                           "\n"
                                           "**Starting Proficiencies**\n"
                                           "You are proficient with the following items, in "
                                           "addition to any Proficiencies provided by your race or Background.\n"
                                           "\n"
                                           "Armor: `none`\n"
                                           "Weapons: `Simple Weapons, shortswords`\n"
                                           "Tools: `any one type of artisan's tools or any one"
                                           " musical Instrument of your choice`\n"
                                           "Saving Throws: `Strength, Dexterity`\n"
                                           "Skills: `Choose two from Acrobatics, Athletics,"
                                           " History, Insight, Religion, and Stealth`\n"
                                           "\n"
                                           "**Starting Equipment**\n"
                                           "You start with the following items, plus anything"
                                           " provided by your Background.\n"
                                           "\n"
                                           "• (a) a Shortsword or (b) any simple weapon\n"
                                           "• (a) a Dungeoneer's Pack or (b) an Explorer's Pack\n"
                                           "• 10 darts"), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Monk  Pg 2 / 12",
                              description="Table: The Monk ", color=Colour)
        Embed.set_image(url="https://cdn.discordapp.com/attachments/638140888949719080/647828547481894941/6.png")
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Monk  Pg 3 / 12",
                              description=("\n"
                                           "**Unarmored Defense**\n"
                                           "Beginning at 1st level, while you are wearing no armor and "
                                           "not wielding a Shield, your AC equals 10 + your Dexterity"
                                           " modifier + your Wisdom modifier.\n"
                                           "\n"
                                           "**Martial Arts**\n"
                                           "Your practice of martial arts gives you mastery of Combat "
                                           "styles that use unarmed strikes and monk Weapons, which are "
                                           "shortswords and any simple Melee Weapons that don't have the "
                                           "Two-Handed or heavy property.\n"
                                           "\n"
                                           "You gain the following benefits while you are unarmed or"
                                           " wielding only monk Weapons and you aren't wearing armor or "
                                           "wielding a Shield.\n"
                                           "\n"
                                           "• You can use Dexterity instead of Strength for the Attack"
                                           " and Damage Rolls of your unarmed strikes and monk Weapons.\n"
                                           "\n"
                                           "• You can roll a d4 in place of the normal damage of your "
                                           "Unarmed Strike or monk weapon.\n"
                                           "\n"
                                           "• When you use the Attack action with an Unarmed Strike or a "
                                           "monk weapon on Your Turn, you can make one Unarmed Strike as a "
                                           "Bonus Action. For example, if you take the Attack action and "
                                           "Attack with a Quarterstaff, you can also make an Unarmed Strike "
                                           "as a Bonus Action, assuming you haven't already taken a Bonus"
                                           " Action this turn.\n"
                                           "\n"
                                           "Certain monasteries use specialized forms of the monk Weapons."
                                           " For example, you might use a club that is two lengths of wood "
                                           "connected by a short chain (called a nunchaku) or a Sickle with a "
                                           "shorter, straighter blade (called a kama). Whatever name you use "
                                           "for a monk weapon, you can use the game Statistics provided for "
                                           "the weapon.\n"
                                           "        "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Monk  Pg 4 / 12",
                              description=("\n"
                                           "**Ki**\n"
                                           "Starting at 2nd level, your Training allows you to "
                                           "harness The Mystic energy of ki. Your access to this"
                                           " energy is represented by a number of ki points. Your"
                                           " monk level determines the number of points you have"
                                           ", as shown in the Ki Points column of the Monk table.\n"
                                           "\n"
                                           "You can spend these points to fuel various ki features."
                                           " You start knowing three such features: Flurry of Blows, "
                                           "Patient Defense, and Step of the Wind. You learn more ki"
                                           " features as you gain levels in this class.\n"
                                           "\n"
                                           "When you spend a ki point, it is unavailable until you"
                                           " finish a short or Long Rest, at the end of which you draw "
                                           "all of your expended ki back into yourself. You must spend"
                                           " at least 30 minutes of the rest meditating to regain your ki points.\n"
                                           "\n"
                                           "Some of your ki features require your target to make a"
                                           " saving throw to resist the feature's Effects. The saving "
                                           "throw DC is calculated as follows:\n"
                                           "\n"
                                           "**Ki save DC** = `8 + your Proficiency Bonus + your Wisdom"
                                           " modifier`\n"
                                           "        "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Monk  Pg 5 / 12",
                              description=("\n"
                                           "**Flurry of Blows**\n"
                                           "Immediately after you take the Attack action on Your "
                                           "Turn, you can spend 1 ki point to make two unarmed "
                                           "strikes as a Bonus Action.\n"
                                           "\n"
                                           "**Patient Defense**\n"
                                           "You can spend 1 ki point to take the Dodge action as a "
                                           "Bonus Action on Your Turn.\n"
                                           "\n"
                                           "**Step of the Wind**\n"
                                           "You can spend 1 ki point to take the Disengage or Dash "
                                           "action as a Bonus Action on Your Turn, and your jump "
                                           "distance is doubled for the turn.\n"
                                           "        "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Monk  Pg 6 / 12",
                              description=("\n"
                                           "**Unarmored Movement**\n"
                                           "Starting at 2nd level, your speed increases by 10 feet "
                                           "while you are not wearing armor or wielding a Shield. "
                                           "This bonus increases when you reach certain monk levels,"
                                           " as shown in the Monk table.\n"
                                           "\n"
                                           "At 9th level, you gain the ability to move along vertical "
                                           "surfaces and across liquids on Your Turn without Falling "
                                           "during the move.\n"
                                           "\n"
                                           "**Monastic Tradition**\n"
                                           "When you reach 3rd level, you commit yourself to a monastic "
                                           "tradition, such as the Way of the Open Hand. Your tradition "
                                           "grants you features at 3rd level and again at 6th, 11th, and 17th level.\n"
                                           ""), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Monk  Pg 7 / 12",
                              description=("\n"
                                           "**Deflect Missiles**\n"
                                           "Starting at 3rd level, you can use your Reaction to deflect or "
                                           "catch the missile when you are hit by a ranged weapon Attack. "
                                           "When you do so, the damage you take from the Attack is reduced"
                                           " by 1d 10 + your Dexterity modifier + your monk level.\n"
                                           "\n"
                                           "If you reduce the damage to 0, you can catch the missile if it "
                                           "is small enough for you to hold in one hand and you have at least "
                                           "one hand free. If you catch a missile in this way, you can spend "
                                           "1 ki point to make a ranged Attack (range 20 feet/60 feet) with "
                                           "the weapon or piece of Ammunition you just caught, as part of the"
                                           " same Reaction. You make this Attack with proficiency, regardless"
                                           " of your weapon Proficiencies, and the missile counts as a monk "
                                           "weapon for the Attack.\n"
                                           "                        "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Monk  Pg 8 / 12",
                              description=("\n"
                                           "**Ability Score Improvement**\n"
                                           "When you reach 4th level, and again at 8th, 12th, 16th, and"
                                           " 19th level, you can increase one ability score of your choice "
                                           "by 2, or you can increase two Ability Scores of your choice by "
                                           "1. As normal, you can’t increase an ability score above 20 "
                                           "using this feature.\n"
                                           "\n"
                                           "**Slow Fall**\n"
                                           "Beginning at 4th level, you can use your Reaction when you "
                                           "fall to reduce any Falling damage you take by an amount equal "
                                           "to five times your monk level.\n"
                                           "\n"
                                           "**Extra Attack**\n"
                                           "Beginning at 5th level, you can Attack twice, instead of "
                                           "once, whenever you take the Attack action on Your Turn.\n"
                                           "                        "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Monk  Pg 9 / 12",
                              description=("\n"
                                           "**Stunning Strike**\n"
                                           "Starting at 5th level, you can interfere with the flow "
                                           "of ki in an opponent's body. When you hit another creature "
                                           "with a melee weapon Attack, you can spend 1 ki point to "
                                           "attempt a stunning strike. The target must succeed on a "
                                           "Constitution saving throw or be Stunned until the end"
                                           " of your next turn.\n"
                                           "\n"
                                           "**Ki-Empowered Strikes**\n"
                                           "Starting at 6th level, your unarmed strikes count as "
                                           "magical for the purpose of overcoming Resistance and "
                                           "immunity to nonmagical attacks and damage.\n"
                                           "\n"
                                           "**Stillness of Mind**\n"
                                           "Starting at 7th level, you can use your action to end "
                                           "one effect on yourself that is causing you to be Charmed "
                                           "or Frightened.\n"
                                           "\n"
                                           "**Evasion**\n"
                                           "At 7th level, your instinctive agility lets you dodge "
                                           "out of the way of certain area Effects, such as a blue "
                                           "dragon's lightning breath or a Fireball spell. When you"
                                           " are subjected to an effect that allows you to make a "
                                           "Dexterity saving throw to take only half damage, you "
                                           "instead take no damage if you succeed on the saving"
                                           " throw, and only half damage if you fail.\n"
                                           ""), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Monk  Pg 10 / 12",
                              description=("\n"
                                           "**Purity of Body**\n"
                                           "At 10th level, your mastery of the ki flowing through you "
                                           "makes you immune to disease and poison.\n"
                                           "\n"
                                           "**Tongue of the Sun and Moon**\n"
                                           "Starting at 13th level, you learn to touch the ki of other"
                                           " minds so that you understand all spoken Languages. Moreover,"
                                           " any creature that can understand a language can "
                                           "understand what you say.\n"
                                           "\n"
                                           "**Diamond Soul**\n"
                                           "Beginning at 14th level, your mastery of ki grants you "
                                           "proficiency in all Saving Throws.\n"
                                           "\n"
                                           "Additionally, whenever you make a saving throw and fail, you"
                                           " can spend 1 ki point to reroll it and take the second result.\n"
                                           "\n"
                                           "**Timeless Body**\n"
                                           "At 15th level, your ki sustains you so that you suffer "
                                           "none of the frailty of old age, and you can't be aged"
                                           " magically. You can still die of old age, however. In "
                                           "addition, you no longer need food or water.\n"
                                           "\n"
                                           ""), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Monk  Pg 11 / 12",
                              description=("\n"
                                           "**Empty Body**\n"
                                           "Beginning at 18th level, you can use your action"
                                           " to spend 4 ki points to become Invisible for 1 "
                                           "minute. During that time, you also have Resistance "
                                           "to all damage but force damage.\n"
                                           "\n"
                                           "Additionally, you can spend 8 ki points to cast"
                                           " the Astral Projection spell, without needing "
                                           "material Components. When you do so, you can't "
                                           "take any other creatures with you.\n"
                                           "\n"
                                           "**Perfect Soul**\n"
                                           "At 20th level, when you roll for Initiative an"
                                           "d have no ki points remaining, you regain 4 ki points.\n"
                                           "\n"
                                           ""), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Monk | Monastic Traditions | Pg 12 / 12",
                              description="""
                        `Way of the Shadow`
                        `Way of the Open Hand`     
                        `Way of the Kensei`                               
                                                    """, color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        return EmbedList


async def Paladin(Subclass, Data):
    global Colour
    EmbedList = []
    if not Subclass:
        Embed = discord.Embed(title="Class - Paladin  Pg 1 / 14",
                              description=("        \n"
                                           "**Hit Points**\n"
                                           "Hit Dice: `1d10 per Paladin level`\n"
                                           "Hit Points at 1st Level: `10 + your Constitution modifier`\n"
                                           "Hit Points at Higher Levels: `1d10 (or 6) + your "
                                           "Constitution modifier per Paladin level after 1st`\n"
                                           "\n"
                                           "**Starting Proficiencies**\n"
                                           "You are proficient with the following items, in "
                                           "addition to any Proficiencies provided by your race or Background.\n"
                                           "\n"
                                           "Armor: `Light Armor, Medium Armor, Heavy Armor, Shields`\n"
                                           "Weapons: `Simple Weapons, Martial Weapons`\n"
                                           "Tools: `none`\n"
                                           "Saving Throws: `Wisdom, Charisma`\n"
                                           "Skills: `Choose two from Athletics, Insight, "
                                           "Intimidation, Medicine, Persuasion, and Religion`\n"
                                           "\n"
                                           "**Starting Equipment**\n"
                                           "You start with the following items, plus anything "
                                           "provided by your Background.\n"
                                           "\n"
                                           "• (a) a martial weapon and a Shield or (b) two Martial Weapons\n"
                                           "• (a) five javelins or (b) any simple melee weapon\n"
                                           "• (a) a Priest's Pack or (b) an Explorer's Pack\n"
                                           "• Chain Mail and a holy Symbol\n"
                                           "\n"
                                           "Alternatively, you may start with 5d4 x 10 gp to "
                                           "buy your own Equipment."), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Paladin  Pg 2 / 14",
                              description="Table: The Paladin ", color=Colour)
        Embed.set_image(url="https://cdn.discordapp.com/attachments/638140888949719080/649721165266550814/7.png")
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Paladin  Pg 3 / 14",
                              description=("\n"
                                           "**Divine Sense**\n"
                                           "The presence of strong evil registers on your Senses like a "
                                           "noxious odor, and powerful good rings like heavenly music in"
                                           " your ears. As an action, you can open your awareness to detect"
                                           " such forces. Until the end of your next turn, you know the location"
                                           " of any Celestial, fiend, or Undead within 60 feet of you that is not"
                                           " behind total cover. You know the type (celestial, fiend, or undead) "
                                           "of any being whose presence you sense, but not its identity (the Vampire"
                                           " Count Strahd von Zarovich, for instance). Within the same radius, you "
                                           "also detect the presence of any place or object that has been consecrated"
                                           " or desecrated, as with the Hallow spell.\n"
                                           "\n"
                                           "You can use this feature a number of times equal to 1 + your "
                                           "Charisma modifier. When you finish a Long Rest, you regain all "
                                           "expended uses.\n"
                                           "\n"
                                           "**Lay on Hands**\n"
                                           "Your blessed touch can heal wounds. You have a pool of Healing"
                                           " power that replenishes when you take a Long Rest. With that pool,"
                                           " you can restore a total number of Hit Points equal to "
                                           "your Paladin level x 5.\n"
                                           "\n"
                                           "As an action, you can touch a creature and draw power from the "
                                           "pool to restore a number of Hit Points to that creature, up to the "
                                           "maximum amount remaining in your pool.\n"
                                           "\n"
                                           "Alternatively, you can expend 5 Hit Points from your pool of "
                                           "Healing to cure the target of one disease or neutralize one poison "
                                           "affecting it. You can cure multiple Diseases and neutralize multiple "
                                           "Poisons with a single use of Lay on Hands, expending Hit Points "
                                           "separately for each one.\n"
                                           "\n"
                                           "This feature has no effect on Undead and constructs."), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Paladin  Pg 4 / 14",
                              description=("\n"
                                           "**Fighting Style**\n"
                                           "At 2nd level, you adopt a style of fighting as your "
                                           "specialty. Choose one of the following options. You "
                                           "can’t take a Fighting Style option more than once, "
                                           "even if you later get to choose again.\n"
                                           "\n"
                                           "`Defense`\n"
                                           "While you are wearing armor, you gain a +1 bonus to AC.\n"
                                           "\n"
                                           "`Dueling`\n"
                                           "When you are wielding a melee weapon in one hand and no "
                                           "other Weapons, you gain a +2 bonus to Damage Rolls with that weapon.\n"
                                           "\n"
                                           "`Great Weapon Fighting`\n"
                                           "When you roll a 1 or 2 on a damage die for an Attack "
                                           "you make with a melee weapon that you are wielding with"
                                           " two hands, you can reroll the die and must use the new "
                                           "roll. The weapon must have the Two-Handed or Versatile"
                                           " property for you to gain this benefit.\n"
                                           "\n"
                                           "`Protection`\n"
                                           "When a creature you can see attacks a target other than "
                                           "you that is within 5 feet of you, you can use your reaction"
                                           " to impose disadvantage on the Attack roll. You must be"
                                           " wielding a Shield.\n"
                                           "                "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Paladin  Pg 5 / 14",
                              description=("\n"
                                           "**Divine Smite**\n"
                                           "Starting at 2nd level, when you hit a creature with a "
                                           "melee weapon Attack, you can expend one spell slot to"
                                           " deal radiant damage to the target, in addition to the"
                                           " weapon's damage. The extra damage is 2d8 for a "
                                           "1st-level spell slot, plus 1d8 for each Spell Level "
                                           "higher than 1st, to a maximum of 5d8. The damage "
                                           "increases by 1d8 if the target is an Undead or a fiend.\n"
                                           "                "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Paladin  Pg 6 / 14",
                              description=("\n"
                                           "        **Unarmored Movement**\n"
                                           "        Starting at 2nd level, your speed increases by 10 "
                                           "feet while you are not wearing armor or wielding a Shield."
                                           " This bonus increases when you reach certain monk levels, "
                                           "as shown in the Monk table.\n"
                                           "\n"
                                           "        At 9th level, you gain the ability to move along "
                                           "vertical surfaces and across liquids on Your Turn without "
                                           "Falling during the move.\n"
                                           "\n"
                                           "        **Monastic Tradition**\n"
                                           "        When you reach 3rd level, you commit yourself to"
                                           " a monastic tradition, such as the Way of the Open Hand."
                                           " Your tradition grants you features at 3rd level and again "
                                           "at 6th, 11th, and 17th level.\n"
                                           "                        "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Paladin  Pg 7 / 14",
                              description=("\n"
                                           "        **Deflect Missiles**\n"
                                           "        Starting at 3rd level, you can use your Reaction to deflect"
                                           " or catch the missile when you are hit by a ranged weapon Attack. "
                                           "When you do so, the damage you take from the Attack is reduced by "
                                           "1d 10 + your Dexterity modifier + your monk level.\n"
                                           "\n"
                                           "        If you reduce the damage to 0, you can catch the missile "
                                           "if it is small enough for you to hold in one hand and you have at "
                                           "least one hand free. If you catch a missile in this way, you can "
                                           "spend 1 ki point to make a ranged Attack (range 20 feet/60 feet) "
                                           "with the weapon or piece of Ammunition you just caught, as part of"
                                           " the same Reaction. You make this Attack with proficiency, regardless"
                                           " of your weapon Proficiencies, and the missile counts as a monk"
                                           " weapon for the Attack.\n"
                                           "\n"
                                           "**Spellcasting**\n"
                                           "By 2nd level, you have learned to draw on Divine Magic through "
                                           "meditation and prayer to cast Spells as a Cleric does. See chapter"
                                           " 10 for the general rules of Spellcasting and chapter 11"
                                           " for the Paladin spell list.\n"
                                           "                    "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Paladin | Spell Casting Continued | Pg 8 / 14",
                              description=("\n"
                                           "**Preparing and Casting Spells**\n"
                                           "\n"
                                           "The Paladin table shows how many Spell Slots you have to "
                                           "cast your Spells. To cast one of your Paladin Spells of 1st"
                                           " level or higher, you must expend a slot of the spell's level"
                                           " or higher. You regain all expended Spell Slots when you finish "
                                           "a Long Rest.\n"
                                           "\n"
                                           "You prepare the list of Paladin Spells that are available "
                                           "for you to cast, choosing from the Paladin spell list. When"
                                           " you do so, choose a number of Paladin Spells equal to your "
                                           "Charisma modifier + half your Paladin level, rounded down (minimum "
                                           "of one spell). The Spells must be of a level for which"
                                           " you have Spell Slots.\n"
                                           "\n"
                                           "For example, if you are a 5th-level Paladin, you have four"
                                           " 1st-level and two 2nd-level Spell Slots. With a Charisma "
                                           "of 14, your list of prepared Spells can include four Spells"
                                           " of 1st or 2nd level, in any combination. If you prepare the"
                                           " 1st-level spell Cure Wounds, you can cast it using a 1st-level"
                                           " or a 2nd-level slot. Casting the spell doesn't remove it from "
                                           "your list of prepared Spells.\n"
                                           "\n"
                                           "You can change your list of prepared Spells when you finish "
                                           "a Long Rest. Preparing a new list of Paladin Spells "
                                           "requires time spent in prayer and meditation: at least "
                                           "1 minute per Spell Level for each spell on your list.\n"
                                           "\n"
                                           "                                "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Paladin | Spell Casting Continued | Pg 9 / 14",
                              description=("\n"
                                           "**Spellcasting Ability**\n"
                                           "\n"
                                           "Charisma is your Spellcasting Ability for your "
                                           "Paladin Spells, since their power derives from the "
                                           "Strength of your convictions. You use your Charisma "
                                           "whenever a spell refers to your Spellcasting Ability"
                                           ". In addition, you use your Charisma modifier when "
                                           "setting the saving throw DC for a Paladin spell you "
                                           "cast and when Making an Attack roll with one.\n"
                                           "\n"
                                           "Spell save DC = 8 + your Proficiency Bonus + your"
                                           " Charisma modifier\n"
                                           "Spell Attack modifier = your Proficiency Bonus + "
                                           "your Charisma modifier\n"
                                           "\n"
                                           "**Spellcasting Focus**\n"
                                           "\n"
                                           "You can use a holy Symbol as a Spellcasting focus for"
                                           " your Paladin Spells. "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Paladin  Pg 10 / 14",
                              description=("\n"
                                           "**Divine Health**\n"
                                           "By 3rd level, the Divine Magic flowing through you makes you"
                                           " immune to disease.\n"
                                           "\n"
                                           "**Sacred Oath**\n"
                                           "When you reach 3rd level, you swear the oath that binds you as a "
                                           "Paladin forever. Up to this time you have been in a preparatory"
                                           " stage, committed to the path but not yet sworn to it. Now you "
                                           "choose an oath, such as the Oath of Devotion.\n"
                                           "\n"
                                           "Your choice grants you features at 3rd level and again at 7th, "
                                           "15th, and 20th level. Those features include oath Spells and the "
                                           "Channel Divinity feature.\n"
                                           "\n"
                                           "**Oath Spells**\n"
                                           "Each oath has a list of associated Spells. You gain access to "
                                           "these Spells at the levels specified in the oath description. "
                                           "Once you gain access to an oath spell, you always have it prepared."
                                           " Oath Spells don’t count against the number of Spells you can "
                                           "prepare each day.\n"
                                           "If you gain an oath spell that doesn’t appear on the Paladin"
                                           "spell list, the spell is nonetheless a Paladin spell for you. \n"
                                           "\n"), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Paladin  Pg 11 / 14",
                              description=("\n"
                                           "**Channel Divinity**\n"
                                           "Your oath allows you to channel divine energy to"
                                           " fuel magical Effects. Each Channel Divinity option"
                                           " provided by your oath explains how to use it.\n"
                                           "\n"
                                           "When you use your Channel Divinity, you choose "
                                           "which option to use. You must then finish a short or"
                                           " Long Rest to use your Channel Divinity again.\n"
                                           "\n"
                                           "Some Channel Divinity Effects require Saving "
                                           "Throws. When you use such an effect from this class,"
                                           " the DC equals your Paladin spell save DC.\n"
                                           "\n"
                                           "**Ability Score Improvement**\n"
                                           "When you reach 4th level, and again at 8th,"
                                           " 12th, 16th, and 19th level, you can increase one "
                                           "ability score of your choice by 2, or you can increase "
                                           "two Ability Scores of your choice by 1. As normal, you "
                                           "can’t increase an ability score above 20 using this feature.\n"
                                           "\n"
                                           "**Extra Attack**\n"
                                           "Beginning at 5th level, you can Attack "
                                           "twice, instead of once, whenever you take the Attack action "
                                           "on Your Turn.\n"
                                           "\n"
                                           ""), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Paladin  Pg 12 / 14",
                              description=("\n"
                                           "**Aura of Protection**\n"
                                           "Starting at 6th level, whenever you or a friendly creature"
                                           " within 10 feet of you must make a saving throw, the creature "
                                           "gains a bonus to the saving throw equal to your Charisma "
                                           "modifier (with a minimum bonus of +1). You must be conscious"
                                           " to grant this bonus.\n"
                                           "\n"
                                           "At 18th level, the range of this aura increases to 30 feet.\n"
                                           "\n"
                                           "**Aura of Courage**\n"
                                           "Starting at 10th level, you and friendly creatures within 10 feet "
                                           "of you can't be Frightened while you are conscious.\n"
                                           "\n"
                                           "At 18th level, the range of this aura increases to 30 feet.\n"
                                           "            "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Paladin  Pg 13 / 14",
                              description=("\n"
                                           "**Improved Divine Smite**\n"
                                           "By 11th level, you are so suffused with righteous might that all "
                                           "your melee weapon strikes carry divine power with them. Whenever "
                                           "you hit a creature with a melee weapon, the creature takes an extra "
                                           "1d8 radiant damage. If you also use your Divine Smite with an Attack,"
                                           " you add this damage to the extra damage of your Divine Smite.\n"
                                           "\n"
                                           "**Cleansing Touch**\n"
                                           "Beginning at 14th level, you can use your action to end one spell"
                                           " on yourself or on one willing creature that you touch.\n"
                                           "\n"
                                           "You can use this feature a number of times equal to your Charisma "
                                           "modifier (a minimum of once). You regain expended uses when you "
                                           "finish a Long Rest.\n"
                                           "\n"
                                           "**Sacred Oaths**\n"
                                           "Becoming a Paladin involves taking vows that commit the Paladin"
                                           " to the cause of righteousness, an active path of fighting wickedness."
                                           " The final oath, taken when he or she reaches 3rd level, is the"
                                           " culmination of all the paladin’s Training. Some characters with "
                                           "this class don’t consider themselves true paladins until they have"
                                           " reached 3rd level and made this oath. For others, the actual "
                                           "swearing of the oath is a formality, an official stamp on what "
                                           "has always been true in the paladin’s heart.\n"
                                           "                    "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Paladin | Oaths | Pg 14 / 14",
                              description="""
                                `Oath of Devotion`
                                `Oath Breaker`     
                                `Oath of the Aegis`                               
                                                            """, color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        return EmbedList


async def Ranger(Subclass, Data):
    global Colour
    EmbedList = []
    if not Subclass:
        Embed = discord.Embed(title="Class - Ranger  Pg 1 / 12",
                              description=("        \n"
                                           "**Hit Points**\n"
                                           "Hit Dice: `1d10 per Ranger level`\n"
                                           "Hit Points at 1st Level: `10 + your Constitution modifier`\n"
                                           "Hit Points at Higher Levels: `1d10 (or 6) + your Constitution"
                                           " modifier per Ranger level after 1st`\n"
                                           "\n"
                                           "**Starting Proficiencies**\n"
                                           "You are proficient with the following items, in addition to any "
                                           "Proficiencies provided by your race or Background.\n"
                                           "\n"
                                           "Armor: `Light Armor, Medium Armor, Shields`\n"
                                           "Weapons: `Simple Weapons, Martial Weapons`\n"
                                           "Tools: `none`\n"
                                           "Saving `Throws: Strength, Dexterity`\n"
                                           "Skills: `Choose three from Animal Handling, Athletics, Insight, "
                                           "Investigation, Nature, Perception, Stealth, and Survival`\n"
                                           "\n"
                                           "**Starting Equipment**\n"
                                           "You start with the following items, plus anything provided "
                                           "by your Background.\n"
                                           "\n"
                                           "• (a) Scale Mail or (b) Leather Armor\n"
                                           "• (a) two shortswords or (b) two simple Melee Weapons\n"
                                           "• (a) a Dungeoneer's Pack or (b) an Explorer's Pack\n"
                                           "• A Longbow and a Quiver of 20 Arrows\n"), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Ranger  Pg 2 / 12",
                              description="Table: The Ranger ", color=Colour)
        Embed.set_image(url="https://cdn.discordapp.com/attachments/638140888949719080/649733141308768291/8.png")
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Ranger  Pg 3 / 12",
                              description=("\n"
                                           "**Favored Enemy**\n"
                                           "Beginning at 1st level, you have significant experience "
                                           "studying, tracking, hunting, and even talking to a certain type of enemy.\n"
                                           "\n"
                                           "Choose a type of favored enemy: Aberrations, Beasts,"
                                           " Celestials, constructs, Dragons, Elementals, fey, Fiends,"
                                           " Giants, Monstrosities, oozes, Plants, or Undead. Alternatively,"
                                           " you can select two races of Humanoid (such as Gnolls and orcs) "
                                           "as favored enemies.\n"
                                           "\n"
                                           "You have advantage on Wisdom (Survival) checks to track "
                                           "your favored enemies, as well as on Intelligence Checks to"
                                           " recall information about them.\n"
                                           "\n"
                                           "When you gain this feature, you also learn one language "
                                           "of your choice that is spoken by your favored enemies, if they "
                                           "speak one at all.\n"
                                           "\n"                                           
                                           "You choose one additional Favored Enemy, as well as an "
                                           "associated language, at 6th and 14th level. As you gain levels, "
                                           "your choices should reflect the types of Monsters you have "
                                           "encountered on your Adventures.\n"), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Ranger  Pg 4 / 12",
                              description=("\n"
                                           "**Natural Explorer**\n"
                                           "You are particularly familiar with one type of natural Environment"
                                           " and are adept at traveling and surviving in such regions. Choose "
                                           "one type of favored terrain: Arctic, coast, Desert, Forest, Grassland,"
                                           " Mountain, swamp, or The Underdark. When you make an Intelligence or"
                                           " Wisdom check related to your favored terrain, your Proficiency Bonus "
                                           "is doubled if you are using a skill that you're proficient in.\n"
                                           "\n"
                                           "While traveling for an hour or more in your favored terrain, you "
                                           "gain the following benefits:\n"
                                           "\n"
                                           "    • Difficult terrain doesn't slow your group's Travel.\n"
                                           "    • Your group can't become lost except by magical means.\n"
                                           "    • Even when you are engaged in another Activity While Traveling "
                                           "(such as foraging, navigating, or tracking), you remain alert to danger.\n"
                                           "    • If you are traveling alone, you can move stealthily at a normal"
                                           " pace.\n"
                                           "    • When you Forage, you find twice as much food as you normally"
                                           " would.\n"
                                           "    • While tracking other creatures, you also learn their exact"
                                           " number, their sizes, and how long ago they passed through the area.\n"
                                           "\n"
                                           "You choose additional favored terrain types at 6th and 10th level.\n"
                                           "                        "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Ranger  Pg 5 / 12",
                              description=("\n"
                                           "**Spellcasting**\n"
                                           "By the time you reach 2nd level, you have learned to use the "
                                           "magical essence of Nature to cast Spells, much as a druid does.\n"
                                           "\n"
                                           "**Spell Slots**\n"
                                           "\n"
                                           "The Ranger table shows how many Spell Slots you have to cast "
                                           "your Spells of 1st level and higher. To cast one of these Spells,"
                                           " you must expend a slot of the spell's level or higher. You regain"
                                           " all expended Spell Slots when you finish a Long Rest.\n"
                                           "\n"
                                           "For example, if you know the 1st-level spell Animal Friendship "
                                           "and have a 1st-level and a 2nd-level spell slot available, you "
                                           "can cast Animal Friendship using either slot. \n"), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Ranger  Pg 6 / 12",
                              description=("\n"
                                           "**Spells Known of 1st Level and Higher**\n"
                                           "\n"
                                           "You know two 1st-level Spells of your choice from the Ranger "
                                           "spell list.\n"
                                           "\n"
                                           "You learn an additional Ranger spell of your choice at each "
                                           "odd numbered level thereafter. Each of these Spells must be of a level"
                                           " for which you have Spell Slots. For instance, when you reach 5th "
                                           "level in this class, you can learn one new spell of 1st or 2nd level.\n"
                                           "\n"
                                           "Additionally, when you gain a level in this class, you can "
                                           "choose one of the Ranger Spells you know and replace it with another "
                                           "spell from the Ranger spell list, which also must be of a level for "
                                           "which you have Spell Slots.\n"
                                           "\n"
                                           "**Spellcasting Ability**\n"
                                           "\n"
                                           "Wisdom is your Spellcasting Ability for your Ranger Spells, "
                                           "since your magic draws on your Attunement to Nature. You use your "
                                           "Wisdom whenever a spell refers to your Spellcasting Ability. In "
                                           "addition, you use your Wisdom modifier when setting the saving "
                                           "throw DC for a Ranger spell you cast and when Making an Attack "
                                           "roll with one.\n"
                                           "\n"
                                           "Spell save DC = 8 + your Proficiency Bonus + your Wisdom modifier\n"
                                           "Spell Attack modifier = your Proficiency Bonus + your Wisdom modifier\n"
                                           " "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Ranger  Pg 7 / 12",
                              description=("\n"
                                           "**Fighting Style**\n"
                                           "At 2nd level, you adopt a particular style of "
                                           "fighting as your specialty. Choose one of the following "
                                           "options. You can’t take a Fighting Style option more than once, "
                                           "even if you later get to choose again.\n"
                                           "\n"
                                           "`Archery`\n"
                                           "You gain a +2 bonus to Attack rolls you make with "
                                           "Ranged Weapons.\n"
                                           "\n"
                                           "`Defense`\n"
                                           "While you are wearing armor, you gain a +1 bonus to AC. \n"
                                           "\n"
                                           "`Dueling`\n"
                                           "When you are wielding a melee weapon in one hand and no "
                                           "other Weapons, you gain a +2 bonus to Damage Rolls with that weapon.\n"
                                           "\n"
                                           "`Two-Weapon Fighting`\n"
                                           "When you engage in two-weapon fighting, you can add your "
                                           "ability modifier to the damage of the second Attack.\n"
                                           "\n"), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Ranger  Pg 8 / 12",
                              description=("\n"
                                           "**Ranger Archetype**\n"
                                           "At 3rd level, you choose an archetype that you strive to emulate, "
                                           "such as the Hunter. Your choice grants features at 3rd level, and "
                                           "again at 7th, 11th, and 15th level.\n"
                                           "\n"
                                           "**Primeval Awareness**\n"
                                           "Beginning at 3rd level, you can use your action and expend one Ranger "
                                           "spell slot to focus your awareness on the region around you. For 1 minute"
                                           " per level of the spell slot you expend, you can sense whether the "
                                           "following"
                                           " types of creatures are present within 1 mile of you (or within up to 6 "
                                           "miles if you are in your favored terrain): Aberrations, Celestials, Dragons,"
                                           " Elementals, fey, Fiends, and Undead. This feature doesn't reveal the"
                                           " creatures' location or number.\n"
                                           "\n"
                                           "**Ability Score Improvement**\n"
                                           "When you reach 4th level, and again at 8th, 12th, 16th, and 19th level,"
                                           " you can increase one ability score of your choice by 2, or you can increase "
                                           "two Ability Scores of your choice by 1. As normal, you can’t increase an"
                                           " ability score above 20 using this feature.\n"
                                           "                                        "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Ranger  Pg 9 / 12",
                              description=("\n"
                                           "**Extra Attack**\n"
                                           "Beginning at 5th level, you can Attack twice, instead of once,"
                                           " whenever you take the Attack action on Your Turn.\n"
                                           "\n"
                                           "**Land's Stride**\n"
                                           "Starting at 8th level, moving through nonmagical difficult terrain "
                                           "costs you no extra Movement. You can also pass through nonmagical Plants"
                                           " without being slowed by them and without taking damage from them if they"
                                           " have thorns, spines, or a similar hazard.\n"
                                           "\n"
                                           "In addition, you have advantage on Saving Throws against Plants that are"
                                           " magically created or manipulated to impede Movement, such those created "
                                           "by the Entangle spell.\n"
                                           " "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Ranger  Pg 10 / 12",
                              description=("\n"
                                           "**Hide in Plain Sight**\n"
                                           "Starting at 10th level, you can spend 1 minute creating camouflage "
                                           "for yourself. You must have access to fresh mud, dirt, Plants, soot,"
                                           " and other naturally occurring materials with which to create your "
                                           "camouflage.\n"
                                           "\n"
                                           "Once you are camouflaged in this way, you can try to hide by"
                                           " pressing yourself up against a solid surface, such as a tree or wall, "
                                           "that is at least as tall and wide as you are. You gain a +10 bonus to "
                                           "Dexterity (Stealth) checks as long as you remain there without moving "
                                           "or taking Actions. Once you move or take an action or a Reaction, you "
                                           "must camouflage yourself again to gain this benefit.\n"
                                           "\n"
                                           "**Vanish**\n"
                                           "Starting at 14th level, you can use the Hide action as a Bonus "
                                           "Action on Your Turn. Also, you can't be tracked by nonmagical means,"
                                           " unless you choose to leave a trail.\n"
                                           "\n"
                                           "**Feral Senses**\n"
                                           "At 18th level, you gain preternatural Senses that help you "
                                           "fight creatures you can't see. When you Attack a creature you can't "
                                           "see, your inability to see it doesn't impose disadvantage on your "
                                           "Attack rolls against it. You are also aware of the location of any "
                                           "Invisible creature within 30 feet of you, provided that the creature "
                                           "isn't hidden from you and you aren't Blinded or Deafened.\n"
                                           "\n"
                                           "        "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Ranger  Pg 11 / 12",
                              description=("\n"
                                           "**Foe Slayer**\n"
                                           "At 20th level, you become an unparalleled Hunter of your enemies."
                                           " Once on each of your turns, you can add your Wisdom modifier to "
                                           "the Attack roll or the damage roll of an Attack you make against "
                                           "one of your favored enemies. You can choose to use this feature "
                                           "before or after the roll, but before any Effects of the roll are"
                                           " applied.\n"
                                           "\n"
                                           "**Ranger Archetypes**\n"
                                           "A classic expression of the Ranger ideal is the Hunter.\n"
                                           "                                                        "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Ranger | Archetypes | Pg 12 / 12",
                              description="""
                                        `Hunter`                             
                                                                    """, color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        return EmbedList


async def Rogue(Subclass, Data):
    global Colour
    EmbedList = []
    if not Subclass:
        Embed = discord.Embed(title="Class - Rogue  Pg 1 / 8",
                              description=("        \n"
                                           "**Hit Points**\n"
                                           "Hit Dice: `1d8 per rogue level`\n"
                                           "Hit Points at 1st Level: `8 + your Constitution modifier`\n"
                                           "Hit Points at Higher Levels: `1d8 (or 5) + your Constitution"
                                           " modifier per rogue level after 1st`\n"
                                           "\n"
                                           "**Starting Proficiencies**\n"
                                           "You are proficient with the following items, "
                                           "in addition to any Proficiencies provided by your race or Background.\n"
                                           "\n"
                                           "Armor: `Light Armor`\n"
                                           "Weapons: `Simple Weapons, hand crossbows, longswords, "
                                           "rapiers, shortswords`\n"
                                           "Tools: `Thieves' Tools`\n"
                                           "Saving Throws: `Dexterity, Intelligence `\n"
                                           "Skills: `Choose four from Acrobatics, Athletics, "
                                           "Deception, Insight, Intimidation, Investigation, Perception, "
                                           "Performance. Persuasion, Sleight of Hand, and Stealth`\n"
                                           "\n"
                                           "**Starting Equipment**\n"
                                           "You start with the following items, plus anything provided "
                                           "by your Background.\n"
                                           "\n"
                                           "• (a) a Rapier or (b) a Shortsword\n"
                                           "• (a) a Shortbow and Quiver of 20 Arrows or (b) a Shortsword\n"
                                           "• (a) a Burglar's Pack, (b) a Dungeoneer's Pack, or (c) an"
                                           " Explorer's Pack\n"
                                           "• Leather Armor, two daggers, and Thieves' Tools\n"
                                           "        "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Rouge  Pg 2 / 8",
                              description="Table: The Rouge ", color=Colour)
        Embed.set_image(url="https://cdn.discordapp.com/attachments/638140888949719080/649740830768365582/9.png")
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Rogue  Pg 3 / 8",
                              description=("\n"
                                           "**Expertise**\n"
                                           "At 1st level, choose two of your skill "
                                           "Proficiencies, or one of your skill Proficiencies"
                                           " and your proficiency with Thieves' Tools. Your Proficiency"
                                           " Bonus is doubled for any ability check you make that uses"
                                           " either of the chosen Proficiencies.\n"
                                           "\n"
                                           "At 6th level, you can choose two more of"
                                           " your Proficiencies (in Skills or with thieves' "
                                           "tools) to gain this benefit.\n"
                                           "\n"
                                           "**Sneak Attack**\n"
                                           "Beginning at 1st level, you know how to "
                                           "strike subtly and exploit a foe's distraction. Once "
                                           "per turn, you can deal an extra 1d6 damage to one creature "
                                           "you hit with an Attack if you have advantage on the Attack"
                                           " roll. The Attack must use a Finesse or a ranged weapon.\n"
                                           "\n"
                                           "You don't need advantage on the Attack roll "
                                           "if another enemy of the target is within 5 feet of it, "
                                           "that enemy isn't Incapacitated, and you don't have "
                                           "disadvantage on the Attack roll.\n"
                                           "\n"
                                           "The amount of the extra damage increases as "
                                           "you gain levels in this class, as shown in the Sneak "
                                           "Attack column of the Rogue table.\n"), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Rogue  Pg 4 / 8",
                              description=("\n"
                                           "**Thieves' Cant**\n"
                                           "During your rogue Training you learned thieves'"
                                           " cant, a Secret mix of dialect, jargon, and code"
                                           " that allows you to hide messages in seemingly "
                                           "normal conversation. Only another creature that "
                                           "knows thieves' cant understands such messages."
                                           " It takes four times longer to convey such a Message "
                                           "than it does to speak the same idea plainly.\n"
                                           "\n"
                                           "In addition, you understand a set of Secret signs"
                                           " and symbols used to convey short, simple messages,"
                                           " such as whether an area is dangerous or the territory "
                                           "of a thieves' guild, whether loot is nearby, or whether"
                                           " the people in an area are easy marks or will provide a"
                                           " Safe House for thieves on the run.\n"
                                           "\n"
                                           "**Cunning Action**\n"
                                           "Starting at 2nd level, your quick thinking and"
                                           " agility allow you to move and act quickly. You can take"
                                           " a Bonus Action on each of your turns in Combat. This "
                                           "action can be used only to take the Dash, Disengage, or Hide action.\n"
                                           "\n"
                                           "                                "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Rogue  Pg 5 / 8",
                              description=("\n"
                                           "**Roguish Archetype**\n"
                                           "At 3rd level, you choose an archetype that you "
                                           "emulate in the exercise of your rogue Abilities, "
                                           "such as Thief. Your archetype choice grants you "
                                           "features at 3rd level and then again at 9th, 13th, and 17th level.\n"
                                           "\n"
                                           "**Ability Score Improvement**\n"
                                           "When you reach 4th level, and again at 8th, 10th, "
                                           "12th, 16th, and 19th level, you can increase one ability "
                                           "score of your choice by 2, or you can increase two Ability"
                                           " Scores of your choice by 1. As normal, you can’t increase"
                                           " an ability score above 20 using this feature.\n"
                                           "\n"
                                           "**Uncanny Dodge**\n"
                                           "Starting at 5th level, when an attacker that you can "
                                           "see hits you with an Attack, you can use your Reaction "
                                           "to halve the attack's damage against you.\n"
                                           "        "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Rogue  Pg 6 / 8",
                              description=("\n"
                                           "**Evasion**\n"
                                           "Beginning at 7th level, you can nimbly dodge out of the "
                                           "way of certain area Effects, such as a red dragon's fiery"
                                           " breath or an Ice Storm spell. When you are subjected to "
                                           "an effect that allows you to make a Dexterity saving throw"
                                           " to take only half damage, you instead take no damage if you "
                                           "succeed on the saving throw, and only half damage if you fail.\n"
                                           "\n"
                                           "**Reliable Talent**\n"
                                           "By 11th level, you have refined your chosen Skills until "
                                           "they approach perfection. Whenever you make an ability check"
                                           " that lets you add your Proficiency Bonus, you can treat a "
                                           "d20 roll of 9 or lower as a 10.\n"
                                           "\n"
                                           "**Blindsense**\n"
                                           "Starting at 14th level, if you are able to hear, you are aware"
                                           " of the location of any hidden or Invisible creature within "
                                           "10 feet of you.\n"
                                           "\n"
                                           "**Slippery Mind**\n"
                                           "By 15th level, you have acquired greater mental Strength. "
                                           "You gain proficiency in Wisdom Saving Throws.\n"
                                           "         "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Rogue  Pg 7 / 8",
                              description=("\n"
                                           "**Elusive**\n"
                                           "Beginning at 18th level, you are so evasive that attackers"
                                           " rarely gain the upper hand against you. No Attack roll has "
                                           "advantage against you while you aren't Incapacitated.\n"
                                           "\n"
                                           "**Stroke of Luck**\n"
                                           "At 20th level, you have an uncanny knack for succeeding"
                                           " when you need to. If your Attack misses a target within"
                                           " range, you can turn the miss into a hit. Alternatively,"
                                           " if you fail an ability check, you can treat The D20 roll as a 20.\n"
                                           "\n"
                                           "Once you use this feature, you can't use it again until "
                                           "you finish a short or Long Rest.\n"
                                           "\n"
                                           "**Roguish Archetypes**\n"
                                           "Rogues have many features in Common, including their "
                                           "emphasis on perfecting their Skills, their precise and "
                                           "deadly approach to Combat, and their increasingly quick"
                                           " reflexes. But different rogues steer those talents in "
                                           "varying directions, embodied by the rogue archetypes. "
                                           "Your choice of archetype is a reflection of your focus—not "
                                           "necessarily an indication of your chosen profession, but "
                                           "a description of your preferred Techniques.\n"
                                           "\n"
                                           "        "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Rogue | Archetypes | Pg 8 / 8", description="""
            `Theif`
            `Assasin`
            `Arcane Trickster`             """, color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        return EmbedList


async def Sorcerer(Subclass, Data):
    global Colour
    EmbedList = []
    if not Subclass:
        Embed = discord.Embed(title="Class - Sorcerer  Pg 1 / 10",
                              description=("        \n"
                                           "**Hit Points**\n"
                                           "Hit Dice: `1d6 per Sorcerer level`\n"
                                           "Hit Points at 1st Level: `6 + your Constitution modifier`\n"
                                           "Hit Points at Higher Levels: `1d6 (or 4) + "
                                           "your Constitution modifier per Sorcerer level after 1st`\n"
                                           "\n"
                                           "**Starting Proficiencies**\n"
                                           "You are proficient with the following items,"
                                           " in addition to any Proficiencies provided by your race or Background.\n"
                                           "\n"
                                           "Armor: `none`\n"
                                           "Weapons: `daggers, darts, slings, quarterstaffs,"
                                           " light crossbows`\n"
                                           "Tools: `none`\n"
                                           "Saving Throws: `Constitution, Charisma`\n"
                                           "Skills: `Choose two from Arcana, Deception,"
                                           " Insight, Intimidation, Persuasion, and Religion`\n"
                                           "\n"
                                           "**Starting Equipment**\n"
                                           "You start with the following items, "
                                           "plus anything provided by your Background.\n"
                                           "\n"
                                           "• (a) a Light Crossbow and 20 bolts or (b) any simple weapon\n"
                                           "• (a) a Component pouch or (b) an arcane focus\n"
                                           "• (a) a Dungeoneer's Pack or (b) an Explorer's Pack\n"
                                           "• Two daggers\n"
                                           "        "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Sorcerer  Pg 2 / 10",
                              description="Table: The Sorcerer ", color=Colour)
        Embed.set_image(url="https://cdn.discordapp.com/attachments/638140888949719080/650102719490555950/10.png")
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Sorcerer  Pg 3 / 10",
                              description=("\n"
                                           "**Spellcasting**\n"
                                           "An event in your past, or in the life of a parent or ancestor,"
                                           " left an indelible mark on you, infusing you with Arcane Magic."
                                           " This font of magic, whatever its Origin, fuels your Spells."
                                           " See chapter 10 for the general rules of Spellcasting and "
                                           "chapter 11 for the Sorcerer spell list.\n"
                                           "\n"
                                           "**Cantrips**\n"
                                           "\n"
                                           "At 1st level, you know four Cantrips of your choice from "
                                           "the Sorcerer spell list. You learn an additional Sorcerer "
                                           "cantrip of your choice at 4th level and another at 10th level.\n"
                                           "\n"
                                           "**Spell Slots**\n"
                                           "\n"
                                           "The Sorcerer table shows how many Spell Slots you have "
                                           "to cast your Spells of 1st level and higher. To cast one "
                                           "of these Sorcerer Spells, you must expend a slot of the spell's "
                                           "level or higher. You regain all expended Spell Slots when you "
                                           "finish a Long Rest.\n"
                                           "\n"
                                           "For example, if you know the 1st-level spell Burning "
                                           "Hands and have a 1st-level and a 2nd-level spell slot "
                                           "available, you can cast Burning Hands using either slot.\n"
                                           "\n"
                                           "        "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Sorcerer  Pg 4 / 10",
                              description=("\n"
                                           "**Spells Known of 1st Level and Higher**\n"
                                           "\n"
                                           "You know two 1st-level Spells of your choice "
                                           "from the Sorcerer spell list.\n"
                                           "\n"
                                           "You learn an additional Sorcerer spell of your "
                                           "choice at each level except 12th, 14th, 16th, 18th,"
                                           " 19th, and 20th. Each of these Spells must be of a "
                                           "level for which you have Spell Slots. For instance, "
                                           "when you reach 3rd level in this class, you can learn "
                                           "one new spell of 1st or 2nd level.\n"
                                           "\n"
                                           "Additionally, when you gain a level in this "
                                           "class, you can choose one of the Sorcerer Spells you "
                                           "know and replace it with another spell from the Sorcerer"
                                           " spell list, which also must be of a level for which you"
                                           " have Spell Slots.\n"
                                           "\n"
                                           "**Spellcasting Ability**\n"
                                           "\n"
                                           "Charisma is your Spellcasting Ability for your"
                                           " Sorcerer Spells, since the power of your magic relies on "
                                           "your ability to project your will into the world. You use "
                                           "your Charisma whenever a spell refers to your Spellcasting "
                                           "Ability. In addition, you use your Charisma modifier when "
                                           "setting the saving throw DC for a Sorcerer spell you cast "
                                           "and when Making an Attack roll with one.\n"
                                           "\n"
                                           "Spell save DC = `8 + your Proficiency Bonus "
                                           "+ your Charisma modifier`\n"
                                           "Spell Attack modifier = `your Proficiency Bonus"
                                           " + your Charisma modifier`\n"
                                           "\n"
                                           "**Spellcasting Focus**\n"
                                           "\n"
                                           "You can use an arcane focus as a Spellcasting "
                                           "focus for your Sorcerer Spells.\n"
                                           "                                "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Sorcerer  Pg 5 / 10",
                              description=("\n"
                                           "**Sorcerous Origin**\n"
                                           "Choose a sorcerous Origin, which describes "
                                           "the source of your innate magical power, "
                                           "such as Draconic Bloodline.\n"
                                           "\n"
                                           "Your choice grants you features when you choose"
                                           " it at 1st level and again at 6th, 14th, and 18th level.\n"
                                           "\n"
                                           "**Font of Magic**\n"
                                           "At 2nd level, you tap into a deep wellspring of magic"
                                           " within yourself. This wellspring is represented by "
                                           "sorcery points, which allow you to create a variety "
                                           "of magical Effects.\n"
                                           "        "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Sorcerer  Pg 6 / 10",
                              description=("\n"
                                           "**Sorcery Points**\n"
                                           "You have 2 sorcery points, and you gain one additional "
                                           "point every time you level up, to a maximum of 20 at level "
                                           "20. You can never have more sorcery points than shown on the"
                                           " table for your level. You regain all spent sorcery points"
                                           " when you finish a Long Rest.\n"
                                           "\n"
                                           "**Flexible Casting**\n"
                                           "You can use your sorcery points to gain"
                                           " additional Spell Slots, or sacrifice Spell "
                                           "Slots to gain additional sorcery points. You "
                                           "learn other ways to use your sorcery points as"
                                           " you reach higher levels.\n"
                                           "\n"
                                           "Creating Spell Slots. You can transform "
                                           "unexpected sorcery points into one spell slot "
                                           "as a Bonus Action on Your Turn. The created Spell"
                                           " Slots Vanish at the end of a Long Rest. The Creating "
                                           "Spell Slots table shows the cost of creating a spell "
                                           "slot of a given level. You can create Spell Slots no higher"
                                           " in level than 5th.\n"
                                           "\n"
                                           "Table: Creating Spell Slots Spell Slot\n"
                                           "Level 	Sorcery points\n"
                                           "1st 	2\n"
                                           "2nd 	3\n"
                                           "3rd 	5\n"
                                           "4th 	6\n"
                                           "5th 	7\n"
                                           "Converting a Spell Slot to Sorcery Points."
                                           " As a Bonus Action on Your Turn, you can "
                                           "expend one spell slot and gain a number"
                                           " of sorcery points equal to the slot's level.\n"
                                           "         "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Sorcerer  Pg 7 / 10",
                              description=("\n"
                                           "**Metamagic**\n"
                                           "At 3rd level, you gain the ability to twist "
                                           "your Spells to suit your needs. You gain two of "
                                           "the following Metamagic options of your choice. "
                                           "You gain another one at 10th and 17th level.\n"
                                           "\n"
                                           "You can use only one Metamagic option on a "
                                           "spell when you cast it, unless otherwise noted.\n"
                                           "\n"
                                           "**Careful Spell**\n"
                                           "When you Cast a Spell that forces other "
                                           "creatures to make a saving throw, you can protect some "
                                           "of those creatures from the spell’s full force. To do so"
                                           ", you spend 1 sorcery point and choose a number of those"
                                           " creatures up to your Charisma modifier (minimum of one creature). "
                                           "A chosen creature automatically succeeds on its saving throw"
                                           "against the spell.\n"
                                           "\n"
                                           "**Distant Spell**\n"
                                           "When you Cast a Spell that has a range of"
                                           " 5 feet or greater, you can spend 1 sorcery point to double "
                                           "the range of the spell.\n"
                                           "\n"
                                           "When you Cast a Spell that has a range of "
                                           "touch, you can spend 1 sorcery point to make the range of "
                                           "the spell 30 feet.\n"
                                           "\n"
                                           "**Empowered Spell**\n"
                                           "When you roll damage for a spell, you can "
                                           "spend 1 sorcery point to reroll a number of the damage dice"
                                           " up to your Charisma modifier (minimum of one)."
                                           " You must use the new rolls.\n"
                                           "\n"
                                           "You can use Empowered Spell even if you have "
                                           "already used a different Metamagic option during the "
                                           "casting of the spell.\n"
                                           "\n"
                                           "**Extended Spell**\n"
                                           "When you Cast a Spell that has a Duration of 1"
                                           " minute or longer, you can spend 1 sorcery point to double"
                                           " its Duration, to a maximum Duration of 24 hours.\n"
                                           "        "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Sorcerer  Pg 8 / 10",
                              description=("\n"
                                           "**Heightened Spell**\n"
                                           "When you Cast a Spell that forces a creature to make "
                                           "a saving throw to resist its Effects, you can spend 3 "
                                           "sorcery points to give one target of the spell disadvantage "
                                           "on its first saving throw made against the spell.\n"
                                           "\n"
                                           "**Quickened Spell**\n"
                                           "When you Cast a Spell that has a Casting Time of 1 "
                                           "action, you can spend 2 sorcery points to change the "
                                           "Casting Time to 1 Bonus Action for this casting.\n"
                                           "\n"
                                           "**Subtle Spell**\n"
                                           "When you Cast a Spell, you can spend 1 sorcery point "
                                           "to cast it without any somatic or verbal Components.\n"
                                           "\n"
                                           "**Twinned Spell**\n"
                                           "When you Cast a Spell that Targets only one creature "
                                           "and doesn’t have a range of self, you can spend a number"
                                           " of sorcery points equal to the spell’s level to target a second"
                                           " creature in range with the same spell (1 sorcery point "
                                           "if the spell is a cantrip).\n"
                                           "\n"
                                           "To be eligible, a spell must be incapable of targeting "
                                           "more than one creature at the spell’s current level. For"
                                           " example, Magic Missile and Scorching Ray aren’t eligible, "
                                           "but Ray of Frost is.\n"), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Sorcerer  Pg 9 / 10",
                              description=("\n"
                                           "**Ability Score Improvement**\n"
                                           "When you reach 4th level, and again at"
                                           " 8th, 12th, 16th, and 19th level, you can "
                                           "increase one ability score of your choice"
                                           " by 2, or you can increase two Ability Scores"
                                           " of your choice by 1. As normal, you can’t increase"
                                           " an ability score above 20 using this feature.\n"
                                           "\n"
                                           "**Sorcerous Restoration**\n"
                                           "At 20th level, you regain 4 expended "
                                           "sorcery points whenever you finish a Short Rest.\n"
                                           "\n"
                                           "**Sorcerous Origins**\n"
                                           "Different sorcerers claim different"
                                           " Origins for their innate magic, such as a Draconic Bloodline.\n"
                                           "         "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Sorcerer | Sorcerous Origins | Pg 10 / 10",
                              description=('\n'
                                           '`Draconic Blood line`\n'
                                           '`Wild Magic`\n'
                                           '`Shadow Magic`\n'
                                           ''), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        return EmbedList


async def Warlock(Subclass, Data):
    global Colour
    EmbedList = []
    if not Subclass:
        Embed = discord.Embed(title="Class - Warlock  Pg 1 / 15",
                              description=("        \n"
                                           "**Hit Points**\n"
                                           "Hit Dice: `1d8 per Warlock level`\n"
                                           "Hit Points at 1st Level: `8 + your Constitution modifier`\n"
                                           "Hit Points at Higher Levels: `1d8 (or 5) + your "
                                           "Constitution modifier per Warlock level after 1st`\n"
                                           "\n"
                                           "**Starting Proficiencies**\n"
                                           "You are proficient with the following items, "
                                           "in addition to any Proficiencies provided by your race or Background.\n"
                                           "\n"
                                           "Armor: `Light Armor`\n"
                                           "Weapons: `Simple Weapons`\n"
                                           "Tools: `none`\n"
                                           "Saving Throws: `Wisdom, Charisma`\n"
                                           "Skills: `Choose two Skills from Arcana, Deception, "
                                           "History, Intimidation, Investigation, Nature, and Religion`\n"
                                           "\n"
                                           "**Starting Equipment**\n"
                                           "You start with the following items, plus anything"
                                           " provided by your Background.\n"
                                           "\n"
                                           "• (a) a Light Crossbow and 20 bolts or (b) any simple weapon\n"
                                           "• (a) a Component pouch or (b) an arcane focus\n"
                                           "• (a) a Scholar's Pack or (b) a Dungeoneer's Pack\n"
                                           "• Leather Armor, any simple weapon, and two daggers\n"
                                           "                "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Warlock  Pg 2 / 15",
                              description="Table: The Warlock ", color=Colour)
        Embed.set_image(url="https://cdn.discordapp.com/attachments/638140888949719080/650107654399590420/11.png")
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Warlock  Pg 3 / 15",
                              description=("\n"
                                           "**Otherworldly Patron**\n"
                                           "At 1st level, you have struck a bargain with an otherworldly "
                                           "being of your choice, such as The Fiend. Your choice grants "
                                           "you features at 1st level and again at 6th, 10th, and 14th level.\n"
                                           "\n"
                                           "**Pact Magic**\n"
                                           "Your arcane Research and the magic bestowed on you by your"
                                           " patron have given you facility with Spells. See chapter 10"
                                           " for the general rules of Spellcasting and chapter 11 for the"
                                           " Warlock spell list.\n"
                                           "\n"
                                           "**Cantrips**\n"
                                           "\n"
                                           "You know two Cantrips of your choice from the Warlock spell "
                                           "list. You learn additional Warlock Cantrips of your choice at"
                                           " higher levels, as shown in the Cantrips Known column of the"
                                           " Warlock table.\n"
                                           "                "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Warlock  Pg 4 / 15",
                              description=("\n"
                                           "**Spell Slots**\n"
                                           "\n"
                                           "The Warlock table shows how many Spell Slots you "
                                           "have. The table also shows what the level of those"
                                           " slots is; all of your Spell Slots are the same level. To cast "
                                           "one of your Warlock Spells of 1st level or higher, you must expend"
                                           " a spell slot. You regain all expended Spell Slots when you finish"
                                           " a short or Long Rest.\n"
                                           "\n"
                                           "For example, when you are 5th level, you have two "
                                           "3rd-level Spell Slots. To cast the 1st-level spell Thunderwave,"
                                           " you must spend one of those slots, and you cast it as a 3rd-level "
                                           "spell.\n"
                                           "\n"
                                           "**Spells Known of 1st Level and Higher**\n"
                                           "\n"
                                           "At 1st level, you know two 1st-level Spells of your "
                                           "choice from the Warlock spell list.\n"
                                           "\n"
                                           "You learn a new Warlock spell every time you gain a "
                                           "level from 2 through 9, as well as at level 19. A spell you"
                                           " choose must be of a level no higher than what's shown in the "
                                           "table's Slot Level column for your level. When you reach 6th "
                                           "level, for example, you learn a new Warlock spell, which can "
                                           "be 1st, 2nd, or 3rd level.\n"
                                           "\n"
                                           "Additionally, when you gain a level in this class, you"
                                           " can choose one of the Warlock Spells you know and replace it"
                                           " with another spell from the Warlock spell list, which also "
                                           "must be of a level for which you have Spell Slots.\n"
                                           "\n"
                                           "**Spellcasting Ability**\n"
                                           "\n"
                                           "Charisma is your Spellcasting Ability for your Warlock "
                                           "Spells, so you use your Charisma whenever a spell refers to your "
                                           "Spellcasting Ability. In addition, you use your Charisma modifier"
                                           " when setting the saving throw DC for a Warlock spell you cast and "
                                           "when Making an Attack roll with one.\n"
                                           "\n"
                                           "Spell save DC = `8 + Proficiency Bonus + Charisma modifier`\n"
                                           "Spell Attack modifier = `Proficiency bonus + Charisma modifier`\n"
                                           "\n"
                                           "**Spellcasting Focus**\n"
                                           "\n"
                                           "You can use an arcane focus as a Spellcasting focus for your"
                                           " Warlock Spells.\n"
                                           "                                        "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Warlock  Pg 5 / 15",
                              description=("\n"
                                           "**Eldritch Invocations**\n"
                                           "In your study of occult lore, you have unearthed Eldritch "
                                           "Invocations, fragments of forbidden knowledge that imbue "
                                           "you with an abiding magical ability.\n"
                                           "\n"
                                           "At 2nd level, you gain two Eldritch Invocations of your "
                                           "choice. Your invocation options are detailed at the end of "
                                           "the class description. When you gain certain Warlock levels, "
                                           "you gain additional invocations of your choice.\n"
                                           "\n"
                                           "Additionally, when you gain a level in this class, you can "
                                           "choose one of the invocations you know and replace it with "
                                           "another invocation that you could learn at that level. A le"
                                           "vel prerequisite in an invocation refers to Warlock level,"
                                           " not character level.\n"
                                           "\n"
                                           "**Pact Boon**\n"
                                           "At 3rd level, your otherworldly patron bestows a gift upon "
                                           "you for your loyal service. You gain one of the following "
                                           "features of your choice.\n"
                                           "                "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Warlock  Pg 6 / 15",
                              description=("\n"
                                           "**Pact of the Chain**\n"
                                           "You learn the Find Familiar spell and can cast it "
                                           "as a ritual. The spell doesnt count against your number "
                                           "of Spells known.\n"
                                           "\n"
                                           "When you cast the spell, you can choose one of the "
                                           "normal forms for your familiar or one of the following "
                                           "Special forms: imp, Pseudodragon, Quasit, or Sprite.\n"
                                           "\n"
                                           "Additionally, when you take the Attack action, you can "
                                           "forgo one of your own attacks to allow your familiar to"
                                           " make one Attack of its own with its Reaction.\n"
                                           "\n"
                                           "**Pact of the Blade**\n"
                                           "You can use your action to create a pact weapon in your"
                                           " empty hand. You can choose the form that this melee "
                                           "weapon takes each time you create it. You are proficient with it "
                                           "while you wield it. This weapon counts as magical for the purpose "
                                           "of overcoming Resistance and immunity to non-magical attacks and damage.\n"
                                           "\n"
                                           "Your pact weapon disappears if it is more than 5 feet away "
                                           "from you for 1 minute or more. It also disappears if "
                                           "you use this feature again, if you dismiss the weapon "
                                           "(no action required), or if you die.\n"
                                           "\n"
                                           "You can transform one Magic Weapon into your pact weapon"
                                           " by performing a Special ritual while you hold the "
                                           "weapon. You perform the ritual over the course of 1 hour,"
                                           " which can be done during a Short Rest. You can then dismiss "
                                           "the weapon, shunting it into an extra-dimensional space, and "
                                           "it appears whenever you create your pact weapon thereafter."
                                           " You can’t affect an artifact or a sentient weapon in this way."
                                           " The weapon ceases being your pact weapon if you die, if you"
                                           " perform the 1-hour ritual on a different weapon, or if you "
                                           "use a 1-hour ritual to break your bond to it. The weapon appears"
                                           " at your feet if it is in the extradimensional space when the"
                                           " bond breaks.\n"
                                           "\n"
                                           "**Pact of the Tome**\n"
                                           "Your patron gives you a grimoire called a Book of Shadows."
                                           " When you gain this feature, choose three Cantrips from any "
                                           "class’s spell list (the three needn’t be from the same list). "
                                           "While the book is on your person, you can cast those Cantrips "
                                           "at will. They don’t count against your number of Cantrips known."
                                           " If they don’t appear on the Warlock spell list, "
                                           "they are nonetheless Warlock Spells for you.\n"
                                           "\n"
                                           "If you lose your Book of Shadows, you can perform a 1-hour"
                                           " Ceremony to receive a replacement from your patron. This Ceremony "
                                           "can be performed during a short or Long Rest, and it destroys the "
                                           "previous book. The book turns to ash when you die.\n"
                                           "                 "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Warlock  Pg 7 / 15",
                              description=("\n"
                                           "**Ability Score Improvement**\n"
                                           "When you reach 4th level, and again at 8th, 12th, 16th, and "
                                           "19th level, you can increase one ability score of your choice"
                                           " by 2, or you can increase two Ability Scores of your choice by 1."
                                           " As normal, you can’t increase an ability score above 20 "
                                           "using this feature.\n"
                                           "\n"
                                           "**Mystic Arcanum**\n"
                                           "At 11th level, your patron bestows upon you a magical Secret "
                                           "called an arcanum. Choose one 6th-level spell from the Warlock "
                                           "spell list as this arcanum.\n"
                                           "\n"
                                           "You can cast your arcanum spell once without expending a spell"
                                           " slot. You must finish a Long Rest before you can do so again.\n"
                                           "\n"
                                           "At higher levels, you gain more Warlock Spells of your choice "
                                           "that can be cast in this way: one 7th-level spell at 13th level,"
                                           " one 8th-level spell at 15th level, and one 9th-level spell at 17th "
                                           "level. You regain all uses of your Mystic Arcanum when you finish a Long Rest.\n"
                                           "\n"
                                           "**Eldritch Master**\n"
                                           "At 20th level, you can draw on your inner reserve of mystical "
                                           "power while entreating your patron to regain expended Spell Slots."
                                           " You can spend 1 minute entreating your patron for aid to regain "
                                           "all your expended Spell Slots from your Pact Magic feature. Once "
                                           "you regain Spell Slots with this feature, you must finish a Long Rest "
                                           "before you can do so again.\n"
                                           "                "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Warlock  Pg 8 / 15",
                              description=("\n"
                                           "**Eldritch Invocations**\n"
                                           "If an eldritch invocation has Prerequisites, "
                                           "you must meet them to learn it. You can learn the invocation "
                                           "at the same time that you meet its Prerequisites. A level "
                                           "prerequisite refers to your level in this class.\n"
                                           "\n"
                                           "8*Agonizing Blast**\n"
                                           "Prerequisite: Eldritch Blast cantrip\n"
                                           "\n"
                                           "When you cast Eldritch Blast, add your Charisma modifier"
                                           " to the damage it deals on a hit.\n"
                                           "\n"
                                           "**Armor of Shadows**\n"
                                           "You can cast Mage Armor on yourself at will, without expending "
                                           "a spell slot or material Components.\n"
                                           "\n"
                                           "**Ascendant Step**\n"
                                           "Prerequisite: 9th level\n"
                                           "\n"
                                           "You can cast Levitate on yourself at will, without expending a "
                                           "spell slot or material Components.\n"
                                           "\n"
                                           "**Beast Speech**\n"
                                           "You can cast Speak with Animals at will, without expending a spell slot.\n"
                                           "\n"
                                           "**Beguiling Influence**\n"
                                           "You gain proficiency in the Deception and Persuasion Skills.\n"
                                           "        "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Warlock  Pg 9 / 15",
                              description=("\n"
                                           "**Bewitching Whispers**\n"
                                           "Prerequisite: 7th level\n"
                                           "\n"
                                           "You can cast Compulsion once using a Warlock spell slot. "
                                           "You can’t do so again until you finish a Long Rest.\n"
                                           "\n"
                                           "**Book of Ancient Secrets**\n"
                                           "Prerequisite: Pact of the Tome feature\n"
                                           "\n"
                                           "You can now inscribe magical Rituals in your Book of Shadows. "
                                           "Choose two 1st-level Spells that have the ritual tag from any class’s "
                                           "spell list (the two needn’t be from the same list). The Spells appear"
                                           " in the book and don’t count against the number of Spells you know. With"
                                           " your Book of Shadows in hand, you can cast the chosen Spells as Rituals. "
                                           "You can’t cast the Spells except as Rituals, unless you’ve learned them by "
                                           "some other means. You can also cast a Warlock spell you know as a ritual"
                                           " if it has the ritual tag.\n"
                                           "\n"
                                           "On your Adventures, you can add other ritual Spells to your Book "
                                           "of Shadows. When you find such a spell, you can add it to the book if "
                                           "the spell’s level is equal to or less than half your Warlock level "
                                           "(rounded up) and if you can spare the time to transcribe the spell. For "
                                           "each level of the spell, the transcription process takes 2 hours and costs"
                                           " 50 gp for the rare inks needed to inscribe it.\n"
                                           "\n"
                                           "**Chains of Carceri**\n"
                                           "Prerequisite: 15th level, Pact of the Chain feature\n"
                                           "\n"
                                           "You can cast Hold Monster at will—targeting a Celestial, fiend,"
                                           " or elemental—without expending a spell slot or material Components."
                                           " You must finish a Long Rest before you can use this invocation on the "
                                           "same creature again.\n"
                                           "\n"
                                           "                 "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Warlock  Pg 10 / 15",
                              description=("\n"
                                           "**Devil’s Sight**\n"
                                           "You can see normally in Darkness, both magical and nonmagical, to a"
                                           " distance of 120 feet.\n"
                                           "\n"
                                           "**Dreadful Word**\n"
                                           "Prerequisite: 7th level\n"
                                           "\n"
                                           "You can cast Confusion once using a Warlock spell slot. You can’t do so"
                                           " again until you finish a Long Rest.\n"
                                           "\n"
                                           "**Eldritch Sight**\n"
                                           "You can cast Detect Magic at will, without expending a spell slot.\n"
                                           "\n"
                                           "**Eldritch Spear**\n"
                                           "Prerequisite: Eldritch Blast cantrip\n"
                                           "\n"
                                           "When you cast Eldritch Blast, its range is 300 feet.\n"
                                           "\n"
                                           "**Eyes of the Rune Keeper**\n"
                                           "You can read all writing.\n"
                                           "                         "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Warlock  Pg 11 / 15",
                              description=('\n'
                                           '**Fiendish Vigor**\n'
                                           'You can cast False Life on yourself at will as a 1st-level spell,'
                                           ' without expending a spell slot or material Components.\n'
                                           '\n'
                                           '**Gaze of Two Minds**\n'
                                           'You can use your action to touch a willing Humanoid and perceive through its                                           '
                                           ' Senses until the end of your next turn. As long as the creature is on the '
                                           'same plane of existence as you, you can use your action on subsequent '
                                           'turns to maintain this connection, extending the Duration until the end'
                                           ' of your next turn. While perceiving through the other creature’s Senses'
                                           ', you benefit from any Special Senses possessed by that creature, '
                                           'and you are Blinded and Deafened to your own surroundings.\n'
                                           '\n'
                                           '**Lifedrinker**\n'
                                           'Prerequisite: 12th level, Pact of the Blade feature\n'
                                           '\n'
                                           'When you hit a creature with your pact weapon, the creature takes extra '
                                           'necrotic damage equal to your Charisma modifier (minimum 1).\n '
                                           '\n'
                                           '**Mask of Many Faces**\n'
                                           'You can cast Disguise Self at will, without expending a spell slot.\n'
                                           '\n'
                                           '                         '), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Warlock  Pg 12 / 15",
                              description=("\n"
                                           "**Master of Myriad Forms**\n"
                                           "Prerequisite: 15th level\n"
                                           "\n"
                                           "You can cast Alter Self at will, without expending a spell slot.\n"
                                           "\n"
                                           "**Minions of Chaos**\n"
                                           "Prerequisite: 9th level\n"
                                           "\n"
                                           "You can cast Conjure Elemental once using a Warlock spell slot. You can’t "
                                           "do so again until you finish a Long Rest.\n "
                                           "\n"
                                           "**Mire the Mind**\n"
                                           "Prerequisite: 5th level\n"
                                           "\n"
                                           "You can cast slow once using a Warlock spell slot. You can’t do so again "
                                           "until you finish a Long Rest.\n "
                                           "\n"
                                           "**Misty Visions**\n"
                                           "You can cast Silent Image at will, without expending a spell slot or "
                                           "material Components.\n "
                                           "\n"
                                           "**One with Shadows**\n"
                                           "Prerequisite: 5th level\n"
                                           "\n"
                                           "When you are in an area of dim light or Darkness, you can use your action "
                                           "to become Invisible until you move or take an action or a Reaction.\n "
                                           "\n"
                                           "**Otherworldly Leap**\n"
                                           "Prerequisite: 9th level\n"
                                           "\n"
                                           "You can cast jump on yourself at will, without expending a spell slot or "
                                           "material Components.\n "
                                           "                                 "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Warlock  Pg 13 / 15",
                              description=("\n"
                                           "**Repelling Blast**\n"
                                           "Prerequisite: Eldritch Blast cantrip\n"
                                           "\n"
                                           "When you hit a creature with Eldritch Blast, you can push the creature up "
                                           "to 10 feet away from you in a straight line.\n "
                                           "\n"
                                           "**Sculptor of Flesh**\n"
                                           "Prerequisite: 7th level\n"
                                           "\n"
                                           "You can cast Polymorph once using a Warlock spell slot. You can’t do so "
                                           "again until you finish a Long Rest.\n "
                                           "\n"
                                           "**Sign of Ill Omen**\n"
                                           "Prerequisite: 5th level\n"
                                           "\n"
                                           "You can cast Bestow Curse once using a Warlock spell slot. You can’t do "
                                           "so again until you finish a Long Rest.\n "
                                           "\n"
                                           "**Thief of Five Fates**\n"
                                           "You can cast bane once using a Warlock spell slot. You can’t do so again "
                                           "until you finish a Long Rest.\n "
                                           "\n"
                                           "**Thirsting Blade**\n"
                                           "Prerequisite: 5th level, Pact of the Blade feature\n"
                                           "\n"
                                           "You can Attack with your pact weapon twice, instead of once, whenever you "
                                           "take the Attack action on Your Turn.\n "
                                           "                                         "), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Warlock  Pg 14 / 15",
                              description=('\n'
                                           '**Visions of Distant Realms**\n'
                                           'Prerequisite: 15th level\n'
                                           '\n'
                                           'You can cast Arcane Eye at will, without expending a spell slot.\n'
                                           '\n'
                                           '**Voice of the Chain Master**\n'
                                           'Prerequisite: Pact of the Chain feature\n'
                                           '\n'
                                           'You can communicate telepathically with your familiar and perceive '
                                           'through your familiar’s Senses as long as you are on the same plane of '
                                           'existence.\n '
                                           '\n'
                                           'Additionally, while perceiving through your familiar’s Senses, you can '
                                           'also speak through your familiar in your own voice, even if your familiar '
                                           'is normally incapable of Speech.\n '
                                           '\n'
                                           '**Whispers of the Grave**\n'
                                           'Prerequisite: 9th level\n'
                                           '\n'
                                           'You can cast Speak with Dead at will, without expending a spell slot.\n'
                                           '\n'
                                           '**Witch Sight**\n'
                                           'Prerequisite: 15th level\n'
                                           '\n'
                                           'You can see the true form of any Shapechanger or creature concealed by '
                                           'Illusion or Transmutation magic while the creature is within 30 feet of '
                                           'you and within line of sight.\n '
                                           '                                                 '), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        Embed = discord.Embed(title="Class - Warlock | Warlock Packs | Pg 15 / 15",
                              description=("\n"
                                           "**Otherworldly Patrons**\n"
                                           "The beings that serve as Patrons for warlocks are mighty inhabitants of "
                                           "Other Planes of existence—not gods, but almost godlike in their power. "
                                           "Various Patrons give their warlocks access to different powers and "
                                           "invocations, and expect significant favors in return.\n "
                                           "\n"
                                           "Some Patrons collect warlocks, doling out mystic knowledge relatively "
                                           "freely or boasting of their ability to bind mortals to their will. Other "
                                           "Patrons bestow their power only grudgingly, and might make a pact with "
                                           "only one Warlock. Warlocks who serve the same patron might view each "
                                           "other as allies, Siblings, or Rivals.\n "
                                           "\n"
                                           "`Hex Blade`\n"
                                           "`The Fiend`                            \n"
                                           ""), color=Colour)
        Embed.set_footer(text=footer)
        EmbedList.append(Embed)
        return EmbedList


async def wizard(subclass):
    embed_list = []
    if not subclass:
        embed = discord.Embed(title="Class - Wizard  Pg 1 / 7",
                              description=("        \n"
                                           "**Hit Points**\n"
                                           "Hit Dice: `1d6 per Wizard level`\n"
                                           "Hit Points at 1st Level: `6 + your Constitution modifier`\n"
                                           "Hit Points at Higher Levels: `1d6 (or 4) + your Constitution modifier per Wizard level after 1st`\n"
                                           "\n"
                                           "**Starting Proficiencies**\n"
                                           "You are proficient with the following items, in addition to any Proficiencies provided by your race or Background.\n"
                                           "\n"
                                           "Armor: `none`\n"
                                           "Weapons: `daggers, darts, slings, quarterstaff, light crossbows`\n"
                                           "Tools: `none`\n"
                                           "Saving Throws: `Intelligence, Wisdom`\n"
                                           "Skills: `Choose two from Arcana, History, Insight, Investigation, Medicine, and Religion`\n"
                                           "\n"
                                           "**Starting Equipment**\n"
                                           "You start with the following items, plus anything provided by your Background.\n"
                                           "\n"
                                           "• (a) a Quarterstaff or (b) a Dagger\n"
                                           "• (a) a Component pouch or (b) an arcane focus\n"
                                           "• (a) a Scholar's Pack or (b) an Explorer's Pack\n"
                                           "• A Spellbook\n"
                                           "\n"
                                           "                "), color=Colour)
        embed.set_footer(text=footer)
        embed_list.append(embed)
        embed = discord.Embed(title="Class - Wizard  Pg 2 / 7",
                              description="Table: The Wizard ", color=Colour)
        embed.set_image(url="https://cdn.discordapp.com/attachments/638140888949719080/650111455823265803/12.png")
        embed.set_footer(text=footer)
        embed_list.append(embed)
        embed = discord.Embed(title="Class - Wizard  Pg 3 / 7",
                              description=("\n"
                                           "**Spellcasting**\n"
                                           "As a student of Arcane Magic, you have a Spellbook containing Spells that show the first glimmerings of your true power.\n"
                                           "\n"
                                           "**Cantrips**\n"
                                           "\n"
                                           "At 1st level, you know three Cantrips of your choice from the Wizard spell list. You learn additional Wizard Cantrips of your choice at higher levels, as shown in the Cantrips Known column of the Wizard table.\n"
                                           "\n"
                                           "**Spellbook**\n"
                                           "\n"
                                           "At 1st level, you have a Spellbook containing six 1st-level Wizard Spells of your choice. Your Spellbook is the repository of the Wizard Spells you know, except your Cantrips, which are fixed in your mind.\n"
                                           "                "), color=Colour)
        embed.set_footer(text=footer)
        embed_list.append(embed)
        embed = discord.Embed(title="Class - Wizard  Pg 4 / 7",
                              description=("\n"
                                           "**Preparing and Casting Spells**\n"
                                           "\n"
                                           "The Wizard table shows how many Spell Slots you have to cast your Spells of 1st level and higher. To cast one of these Spells, you must expend a slot of the spell's level or higher. You regain all expended Spell Slots when you finish a Long Rest.\n"
                                           "\n"
                                           "You prepare the list of Wizard Spells that are available for you to cast. To do so, choose a number of Wizard Spells from your Spellbook equal to your Intelligence modifier + your Wizard level (minimum of one spell). The Spells must be of a level for which you have Spell Slots.\n"
                                           "\n"
                                           "For example, if you're a 3rd-level Wizard, you have four 1st-level and two 2nd-level Spell Slots. With an Intelligence of 16, your list of prepared Spells can include six Spells of 1st or 2nd level, in any combination, chosen from your Spellbook. If you prepare the 1st-level spell Magic Missile, you can cast it using a 1st-level or a 2nd-level slot. Casting the spell doesn't remove it from your list of prepared Spells.\n"
                                           "\n"
                                           "You can change your list of prepared Spells when you finish a Long Rest. Preparing a new list of Wizard Spells requires time spent studying your Spellbook and memorizing the incantations and gestures you must make to cast the spell: at least 1 minute per Spell Level for each spell on your list.\n"
                                           "\n"
                                           "**Spellcasting Ability**\n"
                                           "\n"
                                           "Intelligence is your Spellcasting Ability for your Wizard Spells, since you learn your Spells through dedicated study and memorization. You use your Intelligence whenever a spell refers to your Spellcasting Ability. In addition, you use your Intelligence modifier when setting the saving throw DC for a Wizard spell you cast and when Making an Attack roll with one.\n"
                                           "\n"
                                           "Spell save DC = 8 + your Proficiency Bonus + your Intelligence modifier\n"
                                           "Spell Attack modifier = your Proficiency Bonus + your Intelligence modifier\n"
                                           "                                        "), color=Colour)
        embed.set_footer(text=footer)
        embed_list.append(embed)
        embed = discord.Embed(title="Class - Wizard  Pg 5 / 7",
                              description=("\n"
                                           "**Ritual Casting**\n"
                                           "\n"
                                           "You can cast a Wizard spell as a ritual if that spell has the ritual tag and you have the spell in your Spellbook. You don't need to have the spell prepared.\n"
                                           "\n"
                                           "**Spellcasting Focus**\n"
                                           "\n"
                                           "You can use an arcane focus as a Spellcasting focus for your Wizard Spells.\n"
                                           "\n"
                                           "Learning Spells of 1st Level and Higher\n"
                                           "\n"
                                           "Each time you gain a Wizard level, you can add two Wizard Spells of your choice to your Spellbook for free. Each of these Spells must be of a level for which you have Spell Slots, as shown on the Wizard table. On your Adventures, you might find other Spells that you can add to your Spellbook (see “Your Spellbook”).\n"
                                           "\n"
                                           "**Arcane Recovery**\n"
                                           "You have learned to regain some of your magical energy by studying your Spellbook. Once per day when you finish a Short Rest, you can choose expended Spell Slots to recover. The Spell Slots can have a combined level that is equal to or less than half your Wizard level (rounded up), and none of the slots can be 6th level or higher.\n"
                                           "\n"
                                           "For example, if you’re a 4th-level Wizard, you can recover up to two levels worth of Spell Slots. You can recover either a 2nd-level spell slot or two 1st-level Spell Slots.\n"
                                           "\n"
                                           "**Arcane Tradition**\n"
                                           "When you reach 2nd level, you choose an arcane tradition, shaping your practice of magic through one of eight schools, such as Evocation. Your choice grants you features at 2nd level and again at 6th, 10th, and 14th level.\n"
                                           "                "), color=Colour)
        embed.set_footer(text=footer)
        embed_list.append(embed)
        embed = discord.Embed(title="Class - Wizard  Pg 6 / 7",
                              description=("\n"
                                           "**Ability Score Improvement**\n"
                                           "When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two Ability Scores of your choice by 1. As normal, you can’t increase an ability score above 20 using this feature.\n"
                                           "\n"
                                           "**Spell Mastery**\n"
                                           "At 18th level, you have achieved such mastery over certain Spells that you can cast them at will. Choose a 1st-level Wizard spell and a 2nd-level Wizard spell that are in your Spellbook. You can cast those Spells at their lowest level without expending a spell slot when you have them prepared. If you want to cast either spell at a higher level, you must expend a spell slot as normal.\n"
                                           "\n"
                                           "By spending 8 hours in study, you can exchange one or both of the Spells you chose for different Spells of the same levels.\n"
                                           "\n"
                                           "**Signature Spells**\n"
                                           "When you reach 20th level, you gain mastery over two powerful Spells and can cast them with little effort. Choose two 3rd-level Wizard Spells in your Spellbook as your signature Spells. You always have these Spells prepared, they don't count against the number of Spells you have prepared, and you can cast each of them once at 3rd level without expending a spell slot. When you do so, you can't do so again until you finish a short or Long Rest.\n"
                                           "\n"
                                           "If you want to cast either spell at a higher level, you must expend a spell slot as normal.\n"
                                           "\n"), color=Colour)
        embed.set_footer(text=footer)
        embed_list.append(embed)
        embed = discord.Embed(title="Class - Sorcerer | Wizard Subclasses | Pg 7 / 7",
                              description=("\n"
                                           "**Arcane Traditions**\n"
                                           "\n"
                                           "The study of Wizardry is ancient, stretching back to the earliest mortal discoveries of magic. It is firmly established in fantasy gaming worlds, with various traditions dedicated to its complex study.\n"
                                           "\n"
                                           "The most Common arcane traditions in the multiverse revolve around The Schools of Magic. Wizards through the ages have cataloged thousands of Spells, grouping them into eight categories called schools. In some places, these traditions are literally schools. In other institutions, the schools are more like academic departments, with rival faculties competing for students and funding. Even wizards who train apprentices in the solitude of their own towers use the division of magic into schools as a learning device, since the Spells of each school require mastery of different Techniques.\n"
                                           "\n"
                                           "`School of Evocation`\n"
                                           "`Onomancy (UA)`                                                                                   \n"
                                           "                                                                                    "), color=Colour)
        embed.set_footer(text=footer)
        embed_list.append(embed)
        return embed_list
