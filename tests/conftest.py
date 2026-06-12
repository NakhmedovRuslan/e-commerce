import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def test_product():
    return Product(
        name="Test Product", description="Test Description", price=100, quantity=10)


@pytest.fixture
def test_category(test_product):
    return Category("Test Category", "Test Description", products=[test_product])

@pytest.fixture
def test_product_price_lower():
    return Product(
        name="Test Product", description="Test Description", price=100, quantity=10)