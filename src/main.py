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

# if __name__ == "__main__":
#     product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
#     product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
#     product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#
#     category1 = Category("Смартфоны",
#                          "Смартфоны, как средство не только коммуникации,
#                          но и получения дополнительных функций для удобства жизни")
#
#     category1.add_product(product1)
#     category1.add_product(product2)
#     category1.add_product(product3)
#
#     print(category1.get_product)
#
#     product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
#     category1.add_product(product4)
#     print(category1.get_product)
#     print(Category.product_count)
#
#     new_product = Product.new_product(
#         {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
#          "quantity": 5})
#     print(new_product.name)
#     print(new_product.description)
#     print(new_product.price)
#     print(new_product.quantity)
#
#     new_product.__price = 800
#     print(new_product.price)
#     new_product.__price = -100
#     print(new_product.price)
#     new_product.__price = 0
#     print(new_product.price)
