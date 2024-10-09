from abc import ABC, abstractmethod


class BaseProduct(ABC):

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def price(self, other):
        pass


class MixinProduct:
    def __init__(self, *args, **kwargs):
        super.__init__(*args, **kwargs)
        print(f"{self.__class__.__name__} с параметрами:{args} {kwargs}")


class Product(BaseProduct, MixinProduct):
    name: str
    price: int
    quantity: int
    description: str

    def __init__(self, name, description, price, quantity):
        super().__init__(name, description, price, quantity)
        self.name = name
        self.__price = price
        self.description = description
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) is type(other):
            return self.__price * self.quantity + other.__price * other.quantity
        else:
            raise TypeError("Объекты должны быть экземплярами одного класса")

    def price(self, value: float):
        if value <= 0:
            return "Цена не должна быть нулевая или отрицательная"
        else:
            self.__price = value

    @classmethod
    def new_product(cls, prod_inf: dict):
        return cls(
            prod_inf["name"],
            prod_inf["description"],
            prod_inf["price"],
            prod_inf["quantity"],
        )

    @property
    def price(self):
        return self.__price

    def return_quantity(self):
        return self.quantity


class Smartphone(Product):
    def __init__(
            self, name, description, price, quantity, efficiency, model, memory, color
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(
            self, name, description, price, quantity, country, germination_period, color
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


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
    def products(self):
        return [
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            for product in self.__products
        ]

    def add_product(self, product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Такой продукт нам не подходит")


# if __name__ == '__main__':
#     product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
#     product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
#     product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#
#     print(product1.name)
#     print(product1.description)
#     print(product1.price)
#     print(product1.quantity)
#
#     print(product2.name)
#     print(product2.description)
#     print(product2.price)
#     print(product2.quantity)
#
#     print(product3.name)
#     print(product3.description)
#     print(product3.price)
#     print(product3.quantity)
#
#     category1 = Category("Смартфоны",
#                          "Смартфоны, как средство не только коммуникации, но и получения дополнительных"
#                          " функций для удобства жизни",
#                          [product1, product2, product3])
#
#     print(category1.name == "Смартфоны")
#     print(category1.description)
#     print(len(category1.products))
#     print(category1.category_count)
#     print(category1.product_count)
#
#     product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
#     category2 = Category("Телевизоры",
#                          "Современный телевизор, который позволяет наслаждаться"
#                          " просмотром, станет вашим другом и помощником",
#                          [product4])
#
#     print(category2.name)
#     print(category2.description)
#     print(len(category2.products))
#     print(category2.products)
#
#     print(Category.category_count)
#     print(Category.product_count)
