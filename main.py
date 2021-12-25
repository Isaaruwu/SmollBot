# import discord
# from discord.ext import commands, tasks
# import botconnection
# import json
# from datetime import datetime
# import os
#
# os.chdir('../')
#
# client = discord.Client()
# bot = commands.Bot(command_prefix='.')
#
# replies_and_text = json.load(open('Commands/Help/greetingsandquotes.json', "r", encoding="UTF-8"))
#
#
# # Welcome message
# @tasks.loop(hours=2)
# async def auto_send():
#     channel = await client.fetch_channel(923006044643418165)
#     await channel.send(replies_and_text['Welcome'])
#
#
# # Basic replies
# @client.event
# async def on_message(message):
#     if message.content.startswith('!help'):
#         await message.channel.send(replies_and_text['!help'])
#
#     if message.content.startswith('!hi'):
#         await message.channel.send(f'Hello {message.author.name}!')
#
#     if message.content.startswith('!time'):
#         await message.channel.send(f'Hi {message.author.name}, it is now {datetime.now().strftime("%H:%M:%S")}!')
#
#     if message.content.startswith('!ILY'):
#         await message.channel.send(f"Sorry I don't {message.author.name}...")
#
#     if message.content.startswith('!gif'):
#         channel = await client.fetch_channel(message.channel.id)
#         await channel.send(file=discord.File('gifs/ok.gif'))
#
# if __name__ == '__main__':
#     print('Connecting...')
#
#     @client.event
#     async def on_ready():
#         auto_send.start()
#
#     client.run(botconnection.get_access('info.ini'))
