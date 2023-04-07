import sqlalchemy
from sqlalchemy.orm import sessionmaker
import pandas as pd

# Создание движка для подключения БД
engine = sqlalchemy.create_engine("sqlite:///DB.db", echo=True)
connection = engine.connect()
Session = sessionmaker(autoflush=False, bind=engine)  # Создаем сессию подключения к БД
session = Session()

# Чтение данных из Excel
file = 'database/df.xlsx'
df = pd.read_excel(file, sheet_name='Лист1')