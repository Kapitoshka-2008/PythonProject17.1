from typing import List
from product import Product

class Category:
    def __init__(self, name: str, description: str, products: List[Product]):
        self.name = name
        self.description = description
        self.products = products

    def middle_price(self) -> float:
        try:
            if not self.products:
                return 0
            total_price = sum(product.price for product in self.products)
            return total_price / len(self.products)
        except ZeroDivisionError:
            return 0 