def test_product_init(test_product):
    assert test_product.name == "Test Product"
    assert test_product.description == "Test Description"
    assert test_product.price == 100
    assert test_product.quantity == 10
