from src.category import Category


def test_category_init(test_category):
    assert test_category.name == "Test Category"
    assert test_category.description == "Test Description"
    assert len(test_category.products) == 1
    assert test_category.products[0].name == "Test Product"


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
