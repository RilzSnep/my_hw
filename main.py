class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, product_data):
        return cls(product_data["name"], product_data["description"], product_data["price"], product_data["quantity"])


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.__products = []
        Category.category_count += 1
        Category.product_count += len(description)

    def add_product(self, product):
        self.__products.append(product)

    def get_products(self):
        product_strings = []
        for product in self.__products:
            product_strings.append(f"{product.name}, {product.get_price()} руб. Остаток: {product.quantity} шт.")
        return product_strings


if __name__ == "main":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
    )

    category1.add_product(product1)
    category1.add_product(product2)
    category1.add_product(product3)

    print(category1.get_products())
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print(category1.get_products())
    print(category1.product_count)

    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5})
    print(new_product.name)
    print(new_product.description)
    print(new_product.get_price())
    print(new_product.quantity)

    new_product.set_price(800)
    print(new_product.get_price())

    new_product.set_price(-100)
    print(new_product.get_price())

    new_product.set_price(0)
    print(new_product.get_price())