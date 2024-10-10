from typing import Any

import pytest

from src.main import Category, LawnGrass, Product, Smartphone


@pytest.fixture()
def product_1():
    p1 = Product(
        name="Samsung Galaxy S22 Snapdragon 8 gen 1",
        price=35000.0,
        description="amaled display, 8/256Gb , 50,24,12MP ,Color-Black",
        quantity=3,
    )
    return p1


def test_product_1(product_1):
    assert product_1.price == 35000.0
    assert product_1.name == "Samsung Galaxy S22 Snapdragon 8 gen 1"
    assert product_1.description == "amaled display, 8/256Gb , 50,24,12MP ,Color-Black"
    assert product_1.quantity == 3


@pytest.fixture()
def product_2():
    return Product(
        name="Honor 200 lite",
        price=30000.0,
        description="amaled display, 8/256Gb , 200MP ,Color-white",
        quantity=6,
    )


def test_product_zero_quantity():
    try:
        product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 0)
        print("Тест не пройден: исключение не выброшено")
    except ValueError as e:
        assert str(e) == "Товар с нулевым количеством не может быть добавлен", "Неверное сообщение об ошибке"
        print("Тест пройден: выброшено исключение ValueError")


def test_product_2(product_2):
    assert product_2.price == 30000.0
    assert product_2.name == "Honor 200 lite"
    assert product_2.description == "amaled display, 8/256Gb , 200MP ,Color-white"
    assert product_2.quantity == 6


@pytest.fixture()
def product_3():
    p3 = Product(
        name="Iphone 14 pro max",
        price=35000.0,
        description="amaled display, 8/512Gb , 50Mp ,Color-Purple",
        quantity=5,
    )
    return p3


def test_product_3(product_3):
    assert product_3.price == 35000.0
    assert product_3.name == "Iphone 14 pro max"
    assert product_3.description == "amaled display, 8/512Gb , 50Mp ,Color-Purple"
    assert product_3.quantity == 5


@pytest.fixture()
def test_category() -> Any:
    category1 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
    )
    return category1


def test_category_init(test_category: Any) -> Any:
    assert (
            test_category.description
            == "Современный телевизор, который позволяет наслаждаться просмотром, "
               "станет вашим другом и помощником"
    )
    assert test_category.name == "Телевизоры"


def test_category_str():
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )
    assert str(category1.products) == (
        "['Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.', 'Iphone 15, 210000.0 руб."
        " Остаток: 8 шт.', 'Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.']"
    )
    assert product1 + product2 == 2580000.0
    assert product1 + product3 == 1334000.0
    assert product2 + product3 == 2114000.0


smartphone = Smartphone(
    "Samsung Galaxy S23 Ultra",
    "256GB, Серый цвет, 200MP камера",
    180000.0,
    5,
    95.5,
    "S23 Ultra",
    256,
    "Серый",
)


def test_init_smarthone() -> Any:
    assert smartphone.name == "Samsung Galaxy S23 Ultra"
    assert smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone.efficiency == 95.5
    assert smartphone.model == "S23 Ultra"


lawn_grass = LawnGrass(
    "трава", "трава для газона", 500.0, 20, "Россия", "1 месяц", "Зеленый"
)


def test_init_lawngrass() -> Any:
    assert lawn_grass.name == "трава"
    assert lawn_grass.description == "трава для газона"
    assert lawn_grass.price == 500.0
    assert lawn_grass.quantity == 20
    assert lawn_grass.country == "Россия"
    assert lawn_grass.germination_period == "1 месяц"
