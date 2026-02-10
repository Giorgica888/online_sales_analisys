The following Python Program is usefull for managing the store you own
Why?
because you have here everythign you need for keeping track of the products present in your shop.

Here are the main functionalitys of the Program:


-Product
    This class handles the products as a store insance, not a products itself, as it may look.
    Beacause of the ***quantity*** varaible, that handles the product a type, rather than a instance.
    Like an instance of the store, rather than an individual product.
    you can use this class alongside with the funcionalitys documented inside of it

    main characteristics:the function with that scope
    -Each product instance has an ID (the class instance, not the individual product)
    - You can update the quantity : update_product_quantity
    - you can show information about it inside the console, if you want : show_product_info

-ProductManager
    An util created to handle the products inside the store, kind of like a container,
    that holds all the pieces of the store inside (which are the products)
    
    Main characteristics: the dunction with that scope 
        -You can add products inside of it 
        -You can show the products inside, with they'r quantitys : add_product
        -You can print the total cost amount of the products inside of it : show_price_sum
        -You an remove a products (or update the quantity by -1 to remove one) : remove_product ** or for the -1 Product.product_inside.quantity -= 1

- Cart
    The Cart class is responsible for keeping
    all the customers product inside one box, it is usefull because it allows
    the person to keep track of what they are going to buy from the store.

    Main characteristics : the function with that scope
        - You can add a product : add_products, it keeps track od the pre-existing products, if you decide, just use the product inside the list
        -You can see the total sum of the products : sum_of_products
        -You can show all the products inside of it : show_products

- Main 
    Here we use them all togather
    Its our playground.
    We import and start using all those nice functionalitys.



