class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity 