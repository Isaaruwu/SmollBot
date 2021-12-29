import discord
import schedule
from discord.ext import commands
from utils.getcommands import get_extensions

import os
import configparser

from datetime import datetime

bot_name = 'SmollBot'


def create_bot(filename):
    config = configparser.ConfigParser()
    config.read(filename)
    intents = discord.Intents.default()
    intents.members = True
    token = config['logging']['token']

    bot = commands.Bot(
        command_prefix='!',
        activity=discord.Game(name=f"ugh..")
    )

    for ext in get_extensions():
        bot.load_extension(ext)

    print(f'{bot_name} has connected to Discord!')  # Line #5

    return bot, token


if __name__ == '__main__':
    schedule.run_all()
    smollbot, token = create_bot('info.ini')
    smollbot.run(token)



