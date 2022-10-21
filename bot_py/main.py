import discord 
from discord.ext import commands
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from DataBase.db_main import Weather
# from config import config

intents = discord.Intents.default()
intents.message_content = True


engine = create_engine('sqlite:///weather.db')


def get_city_from_db(city_name):
    session = Session(bind = engine)
    query = session.query(Weather).filter(Weather.city_name == city_name)
    for el in query:
        print(el.city_name)

# client = commands.Bot(command_prefix=config['prefix'], intents=intents)

get_city_from_db("Dnipro")

# @client.command()
# async def hello(ctx):
#     ctx.send(f"Hello")

# @client.command()
# async def help(ctx):
#     ctx.send(f"Now i don't do the help in this bot. Pls wait..")