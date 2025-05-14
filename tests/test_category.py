import pytest
from category import Category
from product import Product

def test_category_creation():
    category = Category("Test Category", "Test Description", [])
    assert category.name == "Test Category"
    assert category.description == "Test Description"
    assert category.products == []

def test_category_middle_price():
    product1 = Product("Product 1", "Description 1", 100.0, 1)
    product2 = Product("Product 2", "Description 2", 200.0, 1)
    category = Category("Test Category", "Test Description", [product1, product2])
    assert category.middle_price() == 150.0

def test_category_empty_middle_price():
    category = Category("Test Category", "Test Description", [])
    assert category.middle_price() == 0 