from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime


Base = declarative_base()


class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(170), nullable=False)


class Weather(Base):
    __tablename__ = 'weather_1'
    id = Column(Integer, primary_key=True)
    temperature = Column(String(4), nullable=False)
    wind_speed = Column(String(10), nullable=False)
    curr_weather = Column(String(10), nullable=False)
    city = relationship("City")
    city_id = Column(ForeignKey("cities.id"))
    date = Column(DateTime(), default=datetime.now())

engine = create_engine('sqlite:///weather.db')
if __name__ == "__main__":
    Base.metadata.create_all(engine)
