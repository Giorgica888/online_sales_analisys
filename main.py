from product import Product
from product_manager import ProductManager

manager = ProductManager([])
manager.add_product(Product("L'scrisors", 10, 200))
manager.add_product(Product("Rose", 20, 81))
manager.add_product(Product("Lilys and play", 21, 31))
manager.add_product(Product("Sign with Tokyo", 30, 62))


