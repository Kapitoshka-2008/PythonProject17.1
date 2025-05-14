import pytest
from product import Product

def test_product_creation():
    product = Product("Test Product", "Test Description", 100.0, 5)
    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 100.0
    assert product.quantity == 5

def test_product_zero_quantity():
    with pytest.raises(ValueError) as exc_info:
        Product("Test Product", "Test Description", 100.0, 0)
    assert str(exc_info.value) == "Товар с нулевым количеством не может быть добавлен" 