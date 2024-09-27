
class Product:
    name: str
    price: int
    quantity: int
    description: str


    def __init__(self, name, description, price, quantity):
        self.name = name
        self.__price = price
        self.description = description
        self.quantity = quantity


    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."


    def __add__(self, other):
        return self.__price * self.quantity + other.__price * other.quantity


    def price_(self, value: float):
        if value <= 0:
            return 'Цена не должна быть нулевая или отрицательная'
        else:
            self.__price = value


    @classmethod
    def new_product(cls, prod_inf: dict):
        return cls(prod_inf['name'], prod_inf['description'], prod_inf['price'], prod_inf['quantity'])


    @property
    def price(self):
        return self.__price

class Category:
    category_count = 0
    product_count = 0
    description: str
    name: str


    def __init__(self, name, description, products=None):
        self.description = description
        self.__products = products if products else []
        self.name = name
        self.category_count += 1
        self.product_count = len(self.__products)
        Category.category_count += 1


    def __str__(self):
        return f"{self.name}, количество продуктов: {self.product_count} шт."


    @property
    def get_product(self):
        for product in self.__products:
            return f"{product.name}, {product.price} руб. Остаток: {product.quantity}."


    def add_product(self, product):
        self.__products.append(product)
