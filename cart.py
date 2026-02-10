from product import Product

class Cart:
    def __init__(self, product_list : list[Product] = []):
        self.product_list = product_list
        self.id_set = set()
        self.id_markup() #Inserts the IDs to the set

    def add_product(self, product : Product):
        """#Checks and adds the product to the list, 
        and the ID to the set"""
        if isinstance(product, Product) and product.id not in self.id_set:
            self.product_list.append(product)
            self.id_set.add(product.id)
        elif isinstance(product, Product) and product.id in self.id_set:
            product.quantity += 1 #the same reference in memory
        else:
            print("Something went wrong")
    
    def sum_of_products(self): 
        """#returns the total pay amount"""
        the_sum = 0
        for i in self.product_list:
            the_sum += i.price * i.quantity
        return the_sum

    def show_products(self, pretty_printing = False):
        """#shows the list of products
            pretty_printing makes new lines if it is  True"""
        print()
        if pretty_printing:
            for i in self.product_list:
                print("-" + str(i.quantity) + "X  ", i.name, end = "\n")  
        else:
            for i in self.product_list:
                print(i.quantity , "X ",i.name, end = " | ")
        

    def id_markup(self): 
        """#Inserts the IDs of the products in the list of IDs"""
        for i in self.product_list:
            self.id_set.add(i.id)

#testy = Cart([Product("masian", 100, 10), Product("caruta", 20, 10)])

