import pytest

from inventory_system import Inventory
from product import Product


@pytest.fixture
def inventory():
    return Inventory()

@pytest.fixture
def sample_product():
    return Product("Test Product", 9.99, 20)

def test_add_product(inventory):
    product = Product("New Product", 15.99, 10)
    inventory.add_product(product)
    assert len(inventory.products) == 1

def test_remove_product(inventory):
    product = Product("Remove Product", 12.99, 5)
    inventory.add_product(product)
    inventory.remove_product("Remove Product")
    assert len(inventory.products) == 0

def test_remove_product_not_in_inventory(inventory, sample_product):
    inventory.add_product(sample_product)
    removed_product = inventory.remove_product("Non-existent Product")
    assert removed_product is None

def test_remove_last_product(inventory):
    product = Product("Product A", 10.0, 1)
    inventory.add_product(product)
    inventory.remove_product("Product A")
    assert len(inventory.products) == 0

def test_get_product(inventory, sample_product):
    inventory.add_product(sample_product)
    retrieved_product = inventory.get_product("Test Product")
    assert retrieved_product == sample_product

def test_get_product_empty_inventory(inventory):
    retrieved_product = inventory.get_product("Non-existent Product")
    assert retrieved_product is None

def test_get_product_product_not_found(inventory, sample_product):
    inventory.add_product(sample_product)
    product_name = "Non-existent Product"
    retrieved_product = inventory.get_product(product_name)
    assert retrieved_product is None, f"Expected product with name {product_name} not found in inventory"

def test_total_inventory_value(inventory, sample_product):
    inventory.add_product(sample_product)
    total_value = inventory.total_inventory_value()
    assert total_value == sample_product.price * sample_product.quantity
