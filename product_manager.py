from product import Product

class ProductManager:
    def __init__(self, product_list : list[Product]):
        self.product_list = product_list
        self.id_set = set()
        self.id_markup() #Inserts the IDs to the set
    
    def add_product(self, product : Product):#Checks and adds the product to the list, and the ID to the set
        if isinstance(product, Product) and product.id not in self.id_set:
            self.product_list.append(product)
            self.id_set.add(product.id)
        else:
            print("Something went wrong")

    def show_products(self, pretty_printing = False):
        if pretty_printing:
            for i in self.product_list:
                print("-" + str(i.quantity) + "X  ", i.name, end = "\n")
        else:
            for i in self.product_list:
                print(i.quantity , "X ",i.name, end = " | ")

    def show_price_sum(self):
        the_sum = 0
        for i in self.product_list:
            the_sum += i.price * i.quantity
        print(f"Total price : {the_sum}")

    def id_markup(self):
        for i in self.product_list:
            self.id_set.add(i.id)
    
# maneger = ProductManager([Product("masian", 100, 10), Product("caruta", 20, 10)])
# maneger.add_product(Product("tir", 22, 10))

# maneger.print_products(pretty_printing=True)