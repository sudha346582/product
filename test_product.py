#test_product.py
import pytest
from product import get_product_info

def test_get_product_info():
    # sample data
    product_id = "P001"
    name = "Laptop"
    quantity = 5
    price = 1200

    # expected result
    expected_output = (
        "Product ID:P001\n"
        "Product Name:Laptop\n"
        "Quantity:5\n"
        "Price:1200"
    )

    # Assertion
    assert get_product_info(product_id, name, quantity, price) == expected_output