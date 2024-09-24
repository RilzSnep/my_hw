class Product:
    name: str
    price: int
    description: str
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    @classmethod
    def new_product(cls, prod_inf: dict):
        return cls(prod_inf['name'], prod_inf['description'], prod_inf['price'], prod_inf['quantity'])


class Category:
    category_count = 0
    product_count = 0
    name: str
    description: str

    def __init__(self, name, description):
        self.description = description
        self.name = name
        self.__products = []
        self.category_count += 1
        self.product_count += len(description)
        Category.category_count += 1

    def add_product(self, product):
        self.__products.append(product)

    @property
    def get_product(self):
        for product in self.__products:
            return f"{product.name}, {product.price} руб. Остаток: {product.quantity}."


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни")

    category1.add_product(product1)
    category1.add_product(product2)
    category1.add_product(product3)

    print(category1.products)

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print(category1.products)
    print(Category.product_count)

    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5})
    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    new_product.__price = 800
    print(new_product.price)
    new_product.__price = -100
    print(new_product.price)
    new_product.__price = 0
    print(new_product.price)