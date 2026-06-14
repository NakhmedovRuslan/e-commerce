from src.product import Product

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

