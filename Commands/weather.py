from datetime import datetime
import discord
from discord.ext import commands
import configparser
import json
import requests


CONFIG = configparser.ConfigParser()
CONFIG.read('info.ini')
API_KEY = CONFIG['logging']['weather_key']


class Weather(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def w(self, ctx):
        city = ctx.message.content[3:]
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
        data = json.loads(requests.get(url).content)

        channel = await self.bot.fetch_channel(923006044643418165)

        embed = discord.Embed(colour=0x00FFFF,
                              title="Today's Weather ⛅",
                              description=f"{city[0].upper() + city[1:]}"
                              )

        text = (
               f"*Right now the temperature is {data['main']['temp']}°C "
               f"with {data['weather'][0]['description']} 🤗\n"
               f"Today's temperature might swing between {data['main']['temp_max']}°C"
               f" and {data['main']['temp_max']}°C."
               f"\n\n> If you wish to get the weather for another city type !w (city)*"
        )

        embed.add_field(name='🌿🌿🌿', value=text, inline=True)
        embed.set_footer(text=f"SmolleBot - Weather")

        await channel.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(Weather(bot))