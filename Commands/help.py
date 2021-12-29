import discord
from discord.ext import commands
import itertools


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


def setup(bot: commands.Bot):
    bot.add_cog(Help(bot))
