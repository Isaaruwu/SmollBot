from discord.ext import commands
import json
import random


class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def loading_quotes(self):
        with open('Commands/Help/greetingsandquotes.json') as f:
            file = json.load(f)
        return file

    @commands.command(aliases=["hello"])
    async def about(self, ctx: commands.Context):
        file = self.loading_quotes()
        await ctx.send(random.choice(list(file[1].values())))


def setup(bot: commands.Bot):
    bot.add_cog(Greetings(bot))