import itertools

class Product:
    _id_counter = itertools.count()
    def __init__(self, name : str, price : float, quantity : int):
        self.id = "Product:" + str(next(Product._id_counter))
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def show_product_info(self, show_id : bool = False):
        """ #Prints the inforamtions of the products"""
        if not show_id:
            print(f"The product : {self.name} costs {self.price} \
            and we have {self.quantity} pieces in stock")
        else:
            print(f"The product : {self.name}/ID : {self.id} costs {self.price} \
            and we have {self.quantity} pieces in stock")

        
    def update_product_quantity(self, new_quantity): 
        """#changes the quantity of the products"""
        if new_quantity >= 0:
            self.quantity = new_quantity