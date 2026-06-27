import pytest

from src.product import Product, Smartphone, LawnGrass


def test_product_init(test_product):
    assert test_product.name == "Test Product"
    assert test_product.description == "Test Description"
    assert test_product.price == 100
    assert test_product.quantity == 10


def test_new_product():
    data = {
        "name": "Samsung_TEST",
        "description": "Test",
        "price": 100,
        "quantity": 5,
    }

    product = Product.new_product(data)

    assert isinstance(product, Product)
    assert product.name == "Samsung_TEST"
    assert product.description == "Test"
    assert product.price == 100
    assert product.quantity == 5


def test_price(capsys, test_product_price_lower):
    default_price = test_product_price_lower.price
    test_product_price_lower.price = -100
    captured = capsys.readouterr()
    assert captured.out == "Цена не должна быть нулевая или отрицательная\n"
    assert test_product_price_lower.price == default_price


def test_price_setter(test_product):
    test_product.price = 500

    assert test_product.price == 500


def test_magic_add():
    product1 = Smartphone(
        "Test 1",
        "Desc",
        100,
        10,
        95,
        "Test model",
        256,
        "Black",
    )

    product2 = Smartphone(
        "Test 2",
        "Desc",
        200,
        2,
        98,
        "Test model",
        128,
        "Gray",
    )

    assert product1 + product2 == 100 * 10 + 200 * 2


def test_magic_str():
    product = Product("Test Product", "Test desc", 100, 10)

    assert str(product) == "Test Product, 100 руб. Остаток: 10 шт."


def test_add_product(test_category):
    product = Product("Test Product", "Test desc", 100, 10)

    products_before = len(test_category.products)

    test_category.add_product(product)

    assert product in test_category.products
    assert len(test_category.products) == products_before + 1


def test_add_subclass_product(test_category):
    smartphone = Smartphone(
        "Test product",
        "Test desc",
        100000,
        5,
        95.5,
        "test model",
        256,
        "Black",
    )

    test_category.add_product(smartphone)

    assert smartphone in test_category.products


def test_add_subclass_product_lawngrass(test_category):
    grass = LawnGrass(
        "test grass",
        "test desc",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )
    test_category.add_product(grass)
    assert grass in test_category.products


def test_add_product_type_error(test_category):
    with pytest.raises(TypeError):
        test_category.add_product("Not a product")
