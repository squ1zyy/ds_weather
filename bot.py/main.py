import discord 
from discord.ext import commands
from sqlalchemy.orm import Session
from ..ds/another import engine, City

def get_data_from_db(city_name):
    session = Session(bind = engine)

