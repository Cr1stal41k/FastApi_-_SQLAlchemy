from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
import db_con


Base = declarative_base()

# Класс для создания таблицы в БД
class Quotes(Base):
    __tablename__ = 'Цитаты'
    index = Column(Integer, primary_key=True, index=True, autoincrement=True)
    quote = Column(String)
    song = Column(String)
    author = Column(String)


Base.metadata.create_all(db_con.engine)  # Создаем таблицу, если она не создана
