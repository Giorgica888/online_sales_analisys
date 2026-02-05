import itertools

class Product:
    _id_counter = itertools.count()
    def __init__(self, name, price, quantity):
        self.id = "Product:" + str(next(Product._id_counter))
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def show_product_info(self):
        print(f"The product : {self.name} costs {self.price} \
         and we have {self.quantity} pieces in stock")
    
    def update_product_quantity(self, new_quantity):
        if new_quantity >= 0:
            self.quantity = new_quantity