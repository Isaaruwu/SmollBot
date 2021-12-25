import discord
from discord.ext import commands
from utils.getcommands import get_extensions

import os
import configparser

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


# # Welcome auto-message
# replies_and_text = json.load(open('../Commands/Help/greetingsandquotes.json', "r", encoding="UTF-8"))
#
#
# @tasks.loop(hours=2)
# async def auto_send():
#     channel = await client.fetch_channel(923006044643418165)
#     await channel.send(replies_and_text['Welcome'])

if __name__ == '__main__':
    print(os.getcwd())

    smollbot = create_bot('info.ini')[0]
    smollbot.run(create_bot('info.ini')[1])

    # @client.event
    # async def on_ready():
    #     auto_send.start()



