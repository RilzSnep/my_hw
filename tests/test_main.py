import pytest
from typing import Any
from src.main import Category, Product


@pytest.fixture()
def product_1():
    return Product(
        name="Samsung Galaxy S22 Snapdragon 8 gen 1",
        price=35000.0,
        description="amaled display, 8/256Gb , 50,24,12MP ,Color-Black",
        quantity=3,
    )


def test_product_1(product_1):
    assert product_1.name == "Samsung Galaxy S22 Snapdragon 8 gen 1"
    assert product_1.price == 35000.0
    assert product_1.description == "amaled display, 8/256Gb , 50,24,12MP ,Color-Black"
    assert product_1.quantity == 3


@pytest.fixture()
def product_2():
    category52 = Product(
        name="Honor 200 lite",
        price=30000.0,
        description="amaled display, 8/256Gb , 200MP ,Color-white",
        quantity=6,
    )
    return category52


def test_product_2(product_2):
    assert product_2.name == "Honor 200 lite"
    assert product_2.price == 30000.0
    assert product_2.description == "amaled display, 8/256Gb , 200MP ,Color-white"
    assert product_2.quantity == 6


@pytest.fixture()
def product_3():
    return Product(
        name="Iphone 14 pro max",
        price=35000.0,
        description="amaled display, 8/512Gb , 50Mp ,Color-Purple",
        quantity=5,
    )


def test_product_3(product_3):
    assert product_3.name == "Iphone 14 pro max"
    assert product_3.price == 35000.0
    assert product_3.description == "amaled display, 8/512Gb , 50Mp ,Color-Purple"
    assert product_3.quantity == 5


@pytest.fixture()
def test_category() -> Any:
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры ",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
    )
    return category2


def test_category_init(test_category: Any) -> Any:
    assert test_category.name == "Телевизоры "
    assert (
        test_category.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
