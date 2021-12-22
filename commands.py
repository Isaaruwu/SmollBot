import discord

client = discord.Client()

# Basic replies
@client.event
async def greetings(message):
    if message.content.startswith('/hi'):
        channel = message.channel
        await channel.send('hello uwu')

