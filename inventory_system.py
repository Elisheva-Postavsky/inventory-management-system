from product import Product


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
 
    def remove_product(self, product_name):
        for p in self.products:
            if p.name == product_name:
                self.products.remove(p)
                break

    def get_product(self, product_name):
        for p in self.products:
            if p.name == product_name:
                return p
        return None

    def total_inventory_value(self):
        total_value = 0
        for p in self.products:
            total_value += p.price * p.quantity
        return total_value

    def get_products_list(self):
        return self.products


if __name__ == '__main__':
    inventory = Inventory()

    product1 = Product("Product A", 5.99, 50)
    product2 = Product("Product B", 10.99, 30)
    inventory.add_product(product1)
    inventory.add_product(product2)

    products_list = inventory.get_products_list()
    for product in products_list:
        print(product.name, product.price)

    inventory.remove_product("Product B")

    for product in products_list:
        print(product.name, product.price)
