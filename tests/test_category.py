from src.category import Category
from src.product import Product

def test_category_init(test_category):
    assert test_category.name == "Test Category"
    assert test_category.description == "Test Description"

    assert test_category.products == "Test Product, 100 руб. Остаток: 10 шт."


def test_products_count(test_product):
    Category.product_count = 0
    product = test_product

    category = Category("Test Category", "Test Description", [product])
    assert category.product_count == 1


def test_categories_count():
    Category.category_count = 0
    Category("Test Category 1", "Test Description 1", [])
    Category("Test Category 2", "Test Description 2", [])

    assert Category.category_count == 2


def test_add_product(test_category):
    product = Product(
        "Test Product",
        "Test Description",
        100,
        10)

    test_category.add_product(product)

    assert "Test Product, 100 руб. Остаток: 10 шт." in test_category.products