from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from DataBase.db_main import Weather
from config import TOKEN
import telebot
from telebot import types


engine = create_engine('sqlite:///weather.db')
bot = telebot(TOKEN)


def get_city_from_db(city_name):
    session = Session(bind = engine)
    weather_list = []
    query = session.query(Weather).filter(Weather.city_name == city_name)
    for el in query:
        weather_list.append(f"{el.city_name}: {el.temperature}")
    return weather_list


@bot.message_handler(commands=["start"])
def hello(msg):
    bot.send_message(msg.chat.id, "Holla Amigo!")

@bot.message_handler(commands=["get_weather"])
def get_weather_command(msg):
    city_name = msg.text.split(" ")[1]
    weather_list = get_city_from_db(city_name)
    print(weather_list)
    for weather in weather_list:
        bot.send_message(msg.chat.id, weather)

@bot.message_handler(commands=["weather"])
def button_weather(msg):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Днепр")
    item2=types.KeyboardButton("Львов")
    item3=types.KeyboardButton("Харьков")
    item4=types.KeyboardButton("Лондон")
markup.add(item1, item2, item3, item4)


bot.polling()