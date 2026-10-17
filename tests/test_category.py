from src.category import Category
from src.product import Product


def test_products_count(test_product):
    Category.product_count = 0
    product = test_product

    category = Category("Test Category", "Test Description", [product])
    assert category.product_count == 1


def test_category_init(test_category):
    assert test_category.name == "Test Category"
    assert test_category.description == "Test Description"

    assert any(
        elem.name == "Test Product" and elem.price == 100 and elem.quantity == 10
        for elem in test_category._Category__products
    )


def test_add_product(test_category):
    product = Product("Test Product", "Test Description", 100, 10)

    test_category.add_product(product)

    assert product in test_category._Category__products


def test_middle_price(test_category):
    assert test_category.middle_price() == 100


def test_middle_price_empty():
    category = Category(name="Пустая категория", description="Нет товаров", products=[])

    assert category.middle_price() == 0
