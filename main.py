from product import Product
from product_manager import ProductManager

manager = ProductManager([])
manager.add_product(Product("Scrisors", 10, 200))
manager.add_product(Product("Rose", 20, 80))
manager.add_product(Product("Lilys", 21, 31))
manager.add_product(Product("Sign with Tokyo", 24, 62))

manager.show_products(pretty_printing=True)
manager.show_price_sum()
