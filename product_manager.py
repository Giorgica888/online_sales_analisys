from product import Product

class ProductManager:
    def __init__(self, product_list : list[Product] = []):
        self.product_list = product_list
        self.id_set = set()
        self.id_markup() #Inserts the IDs to the set
    
    def add_product(self, product : Product):
        """#Checks and adds the product/product instance to the list,
         and the ID to the set"""
        if isinstance(product, Product) and product.id not in self.id_set:
            self.product_list.append(product)
            self.id_set.add(product.id)
        elif isinstance(product, Product) and product.id in self.id_set:
            product.quantity += 1 #the same reference in memory
        else:
            print("Something went wrong")
    
    def show_products(self, pretty_printing = False): 
        """#shows the list of products|
         pretty_printing makes new lines if it is  True"""
        print()
        if pretty_printing:
            for i in self.product_list:
                print("-" + str(i.quantity) + "X  ", i.name, end = "\n")
        else:
            for i in self.product_list:
                print(i.quantity , "X ",i.name, end = " | ")

    def show_price_sum(self):
        """#Prints the total sum of the products inside the manager"""
        the_sum = 0
        for i in self.product_list:
            the_sum += i.price * i.quantity
        print(f"Total price : {the_sum}")

    def remove_product(self, product_name : str):
        """Removes the froducts from the manager"""
        for i in self.product_list:
            if i.name == product_name:
                self.product_list.remove(i)
                self.id_set.remove(i.id)
                return
            
        if self.product_list:
            print("Product does not exist in the list")
        else:
            print("The list is empty")

    def id_markup(self):#Insrts the IDs in the set
        for i in self.product_list:
            self.id_set.add(i.id)

#Direct Test Place  
# maneger = ProductManager([Product("masian", 100, 10), Product("caruta", 20, 10)])
# maneger.add_product(Product("tir", 22, 10))

# maneger.show_products(pretty_printing=True)

# maneger.remove_product("masian")
# maneger.show_products(pretty_printing=True)
