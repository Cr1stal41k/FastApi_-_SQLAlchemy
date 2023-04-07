# from fastapi import FastAPI
# from router import router
# import uvicorn
#
# app = FastAPI()
#
# @app.get("/")
# async def welcome() -> dict:
#     return {"message": "Hello World"}
#
# app.include_router(router)
#
# if __name__ == '__main__':
#     uvicorn.run('main:app', reload=True)

from enum import Enum
class Product(Enum):
    SHIRT = 1
    TSHIRT = 2
    PANT = 3

class DiscountCalculator():
    def __init__(self, product, cost):
        self.product = product
        self.cost = cost
    def get_discounted_price(self):
        if self.product == Product.SHIRT:
            return self.cost - (self.cost * 0.1)
        elif self.product == Product.TSHIRT:
            return self.cost - (self.cost * 0.15)
        elif self.product == Product.PANT:
            return self.cost - (self.cost * 0.25)

dc_Shirt = DiscountCalculator(Product.SHIRT, 100)
print(dc_Shirt.get_discounted_price())