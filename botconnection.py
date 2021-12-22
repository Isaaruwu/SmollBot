import discord
import os
import configparser

bot_name = 'SmollBot'


def get_access(filename):
    config = configparser.ConfigParser()
    config.read(filename)
    token = config['logging']['token']
    client = discord.Client()

    print(f'{bot_name} has connected to Discord!')  # Line #5

    return token


