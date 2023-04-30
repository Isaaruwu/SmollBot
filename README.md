# Discord Bot: SmollBot
This is a Python-based Discord bot that uses the Discord API to provide users with current weather information, generate random memes and replies. The bot utilizes OpenWeatherMap API to retrieve current weather information and PRAW (The Python Reddit API Wrapper) to scrape memes from r/memes. The bot sends a message to the discord server every day at 9am to inform on the current weather. 

## Requirements
- Python 3.6 or higher
- discord.py library (pip install discord.py)
- OpenWeatherMap API key
- PRAW library (pip install praw)

## Commands
The bot currently supports the following commands:

- !hello: Answers with a random greeting message from greetingsandquotes.json 
- !w [location]: Displays the current weather for a specified location.
- !randmeme: Replies with a random meme from r/memes.
- !help: Shows a list of available commands.

## Future Improvements
- Adding playing music features like play, leave, stop, etc.
- Offering more conversational replies 
- Adding additional subreddits to the !randmeme command to provide a wider variety of memes.
- Implementing error handling and user input validation for the !w command.

## Credits
[Discord API](https://discord.com/developers/docs/intro)
[OpenWeatherMap API](https://openweathermap.org/)
[PRAW: The Python Reddit API Wrapper](https://praw.readthedocs.io/en/stable/)
