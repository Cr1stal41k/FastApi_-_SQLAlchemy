from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.orm import declarative_base
import db_con
Base = declarative_base()
class Products(Base):
    __tablename__ = 'Products'
    product_id = Column(Integer, primary_key=True)
    product_name = Column(String(25))
    price = Column(Float)
    paid_for = Column(Boolean)
Base.metadata.create_all(db_con.engine) #создаем таблицу, если она не создана