import discord
from discord.ext import commands
import itertools
import json
import random



class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["hello"])
    async def about(self, ctx: commands.Context):
        with open('Commands/Help/greetingsandquotes.json') as f:
            file = json.load(f)
        await ctx.send(random.choice(list(file[1].values())))


def setup(bot: commands.Bot):
    bot.add_cog(Greetings(bot))