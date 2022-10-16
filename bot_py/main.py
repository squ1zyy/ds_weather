import discord 
from discord.ext import commands
from sqlalchemy.orm import Session
from get_weather import engine, City
from config import config

intents = discord.Intents.default()
intents.message_content = True


def get_city_from_db(city_name):
    session = Session(bind = engine)
    query = session.query(City).filter(City.name == city_name).first
    return "Success"

client = commands.Bot(command_prefix=config['prefix'], intents=intents)


@client.command()
async def hello(ctx):
    ctx.send(f"Hello")