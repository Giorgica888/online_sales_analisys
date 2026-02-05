from product import Product
from product_manager import ProductManager
from cart import Cart

manager = ProductManager()
manager.add_product(Product("Scrisors", 10, 200))
manager.add_product(Product("Rose", 20, 80))
manager.add_product(Product("Lilys", 21, 31))
manager.add_product(Product("Sign with Tokyo", 24, 62))

manager.show_products(pretty_printing=True)
manager.show_price_sum()

print("\n\n\n")
shopping_cart = Cart()
for i in range(3):
    shopping_cart.add_product(manager.product_list[i])
print(f"The total pay amount is {shopping_cart.sum_of_products()}")
shopping_cart.show_products(pretty_printing=True)