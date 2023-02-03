from fastapi import FastAPI
import uvicorn
from db_con import session
from models import Products
from pydantic import BaseModel

app = FastAPI()

class Product(BaseModel):
    product_id: int
    product_name: str
    price: float
    paid_for: bool

#Проверка, есть ли данный продукт в базе
@app.get('/check{product}')
def check_product(product: str):
    for i in session.query(Products):
        if product in i.product_name:
            return {'message': f'Такой продукт есть: {product}',
                    'product_id': i.product_id,
                    'price': i.price,
                    'paid_for': i.paid_for}

#Добавление продукта в БД
@app.post('/create_product/{product}')
def create_product(products: Product):
    product = Products(product_id=products.product_id, product_name=products.product_name, price=products.price, paid_for=products.paid_for)
    session.add(product)
    session.commit()
    return {'product_id': products.product_id, 'product_name': products.product_name, 'price': products.price, 'paid_for': products.paid_for}

#Обновление информации о продукте в БД
@app.put('/update_product/{product}')
def update_product(products: Product):
    product = session.query(Products).get(products.product_id)
    product.price = products.price
    product.product_name = products.product_name
    product.paid_for = products.paid_for
    session.commit()
    return {'product_id': products.product_id, 'product_name': products.product_name, 'price': products.price,
            'paid_for': products.paid_for}

#Удаление продукта из базы
@app.delete('/delete_product/{product}')
def delete_product(product_id: int):
    product = session.query(Products).get(product_id)
    session.delete(product)
    session.commit()
    return {'Удаление товара ID': product_id}

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)