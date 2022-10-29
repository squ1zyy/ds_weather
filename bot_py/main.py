from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from DataBase.db_main import Weather
from config import TOKEN
from telebot import TeleBot


engine = create_engine('sqlite:///weather.db')
bot = TeleBot(TOKEN)


def get_city_from_db(city_name):
    session = Session(bind = engine)
    query = session.query(Weather).filter(Weather.city_name == city_name)
    for el in query:
        print(f"{el.city_name}: {el.temperature}")


@bot.message_handler(commands=["start"])
def hello(msg):
    bot.send_message(msg.chat.id, "Hello")

bot.polling()