import discord
from discord.ext import commands
import itertools


class HelpCommand(commands.HelpCommand):
    async def send_bot_help(self, mapping):
        ctx = self.context
        text = ""

        # embed = discord.Embed(
        #     title=f"Here are all the available command for {ctx.bot.user.name}!",
        #     color=discord.Color(0xFF5BAE),
        # )
        # embed.set_thumbnail(url=ctx.me.avatar_url)
        #
        # embed.add_field(name="_ _")


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        bot.remove_command(name='help')

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(colour=0xEF1E0D,
                              timestamp=ctx.message.created_at,
                              title='Help commands',
                              description=f"Here's all {ctx.bot.user.name} can do!"
                              )
        embed.set_thumbnail(url=ctx.me.avatar_url)

        embed.add_field(name='Quotes 📣', value='> hello\n> cheesy\n> movie', inline=True)
        embed.add_field(name='Memes 😎', value='\n> randmeme\n> randgif\n> AIwaifu', inline=True)
        embed.add_field(name='Music 🎧', value='> join / leave\n> play url\n> pause\n> skip ', inline=True)

        embed.set_footer(text=f"SmolleBot - Help commands")
        await ctx.send(embed=embed)

    # def cog_unload(self):
    #     # Setting help command to the previous help command
    #     # so if this cog unloads the help command restores to previous
    #     self.bot.help_command = self.bot._original_help_command


def setup(bot: commands.Bot):
    bot.add_cog(Help(bot))
