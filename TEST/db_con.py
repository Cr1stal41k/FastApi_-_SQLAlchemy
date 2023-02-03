import sqlalchemy
from sqlalchemy.orm import sessionmaker
engine = sqlalchemy.create_engine("sqlite:///DB.db", echo=True)
connection = engine.connect()
Session = sessionmaker(autoflush=False, bind=engine) #создаем сессию подключения к бд
session = Session()