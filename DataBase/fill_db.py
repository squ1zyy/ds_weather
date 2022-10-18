import requests
from sqlalchemy.orm import Session
from db_main import City, Weather, engine
from schedule import run_pending, every 


def fill_cities():
    session = Session(bind=engine)
    cities_list = ["Dnipro", "Kharkiv", "Lviv", "London"]
    cities_obj_list = [City(name=city_name) for city_name in cities_list]
    session.add_all(cities_obj_list)
    session.commit()
    return 'Success'


def fill_weather():
    session = Session(bind=engine)
    query = session.query(City)
    city_objects = query.all()
    weather_obj_list = []
    for el in city_objects:
        city_name = el.name
        req = requests.get('https://api.openweathermap.org/data/2.5/weather',
              params={'appid': 'dc4782cd45700c18c29efd99522de225',
                      'units': 'metric',
                      'q': city_name})
        print(city_name)
        city_id = el.id
        temperature = req.json()['main']['temp']
        wind_speed = req.json()['wind']['speed']
        curr_weather = req.json()['weather'][0]['main']
        weather_obj = Weather(temperature=temperature, wind_speed=wind_speed, 
                            curr_weather=curr_weather, city_id=city_id)
        weather_obj_list.append(weather_obj)


    print(weather_obj_list)
    session.add_all(weather_obj_list)
    session.commit()
    return 'Success'


def main():
    every(5).minutes.do(fill_weather(engine))
    run_pending()

if __name__ == '__main__':
    every(5).minutes.do(main)