class Product:

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity


class Category:
    def __init__(self, products, name, description):
        self.description = description
        self.name = name
        self.products = products
