from datetime import datetime
import discord
from discord.ext import commands, tasks
import configparser
import json
import requests
import schedule


CONFIG = configparser.ConfigParser()
CONFIG.read('info.ini')
API_KEY = CONFIG['logging']['weather_key']
CITY = '6077246'

URL = f'http://api.openweathermap.org/data/2.5/weather?id={CITY}&appid={API_KEY}&units=metric'


class MorningMessage(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.welcome.start()

    # def check_time(self):
    #     return datetime.now().strftime('%H:%M') == '09:00'

    @tasks.loop(seconds=57)
    async def welcome(self):
        await self.bot.wait_until_ready()
        now = datetime.now().strftime('%H:%M')
        data = json.loads(requests.get(URL).content)

        channel = await self.bot.fetch_channel(927546991163084871)

        if now[:2] == '09' and now[3:] == '00':
            embed = discord.Embed(colour=0x00FFFF,
                                  title="Today's Weather ⛅",
                                  description=f"Montreal"
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

            await channel.send(f"Good morning @everyone ☕ ! "
                               f"Hope you're having a fantastic morning, here's the weather for today!", embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(MorningMessage(bot))
