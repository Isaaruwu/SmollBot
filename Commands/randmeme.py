from discord.ext import commands
import configparser
import praw
import random

CONFIG = configparser.ConfigParser()
CONFIG.read('info.ini')
REDDIT_SECRET = CONFIG['logging']['reddit_secret']
REDDIT_ID = CONFIG['logging']['reddit_id']

REDDIT = praw.Reddit(
    client_id=REDDIT_ID,
    client_secret=REDDIT_SECRET,
    user_agent="SmollBot",
)


class RandomMeme(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def connect_reddit(self):
        memes = REDDIT.subreddit('memes').hot(limit=20)
        meme = [meme for meme in memes]
        return random.choice(meme).url

    @commands.command()
    async def randmeme(self, ctx):
        await ctx.send(self.connect_reddit())


def setup(bot: commands.Bot):
    bot.add_cog(RandomMeme(bot))



