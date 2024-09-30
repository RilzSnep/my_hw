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

    def return_quantity(self):
        return self.quantity


class Category:
    category_count = 0
    product_count = 0
    description: str
    name: str

    def __init__(self, name, description, products=[]):
        self.description = description
        self.__products = products if products else []
        self.name = name
        self.category_count += 1
        self.product_count = len(self.__products)
        Category.category_count += 1

    def __str__(self):

        return f"{self.name}, количество продуктов: {self.product_count} шт."

    @property
    def products(self):
        return [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self.__products]

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise ValueError("Что-то не ворк")


if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(str(category1))

    print(category1.products)

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)
