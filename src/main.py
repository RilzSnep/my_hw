from abc import ABC, abstractmethod


class BaseProduct(ABC):

    def __init__(self, name, description, price, quantity):
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @abstractmethod
    def __str__(self):
        pass


class MixinProduct:
    def __init__(self, *args, **kwargs):
        super.__init__(*args, **kwargs)
        print(f"{self.__class__.__name__} с параметрами:{args} {kwargs}")


class Product(BaseProduct, MixinProduct):
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

    def price_(self, value: float):
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

    def middle_price(self):
        try:
            return sum(product.price for product in self.__products) / len(self.__products)
        except ZeroDivisionError:
            return "Нет продуктов в категории"

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
#     try:
#         product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
#     except ValueError as e:
#         print(
#             "Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт с
#             нулевым количеством")
#     else:
#         print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")
#
#     product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
#     product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
#     product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#
#     category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])
#
#     print(category1.middle_price())
#
#     category_empty = Category("Пустая категория", "Категория без продуктов", [])
#     print(category_empty.middle_price())
