#Product Class

class Products :
    def __init__(self,Name,Price,Available):
        self.Name = Name
        self.Price = Price
        self.Availability = Available

class E_Commerce_Cart :

    # creating the different products
    laptop = Products("laptop",1000,True)
    headphone = Products("headphone",50,True)

    #List of products
    products_List = [laptop,headphone]

    def __init__(self):
        self.cart = {}
        self.total_bill = 0
        self.show_products_available()

    # return the corresponding object matches the given product name
    def product_object(self,product_name):
        product_obj = None
        for i in self.products_List:
            if product_name == i.Name:
                product_obj = i
        return product_obj

    def add_product(self,product_name):

        # First checking the product name in product List and its Availability
        product_obj = self.product_object(product_name)
        if product_obj == None or not (product_obj.Availability):
            print(f"{product_name} is not Available")

        # check wether the product is already in the cart
        # if it is already in the cart notify the user
        # Ask the user for change of quantity

        elif (product_name in self.cart):

            print("The product is already in the cart")
            value = input("Do you want to update the quantity Y/N:")
            if value == "Y" or value == "y":
                quantity_value = int(input("Enter the Quantity : "))

                # Update the bill and Quantity
                self.update_quantity(product_name,quantity_value)

        # user is adding the product for the First Time
        else:
            self.cart[product_name] = {"Quantity":1}
            self.total_bill +=product_obj.Price
            print(product_name,"added Succesfully")

    # Delete the products from the cart
    def remove_product_from_cart(self,product_name):
        product_obj = self.product_object(product_name)
        if product_name not in self.cart:
            print("The products is not in the Cart")
        else:
            self.total_bill = self.total_bill - (product_obj.Price * self.cart[product_name]["Quantity"])
            del self.cart[product_name]
            print("Product is removed from the cart")

    # Update the Quantity of the product
    def update_quantity(self,product_name,Quantity):
        product_obj = self.product_object(product_name)
        current_product_quantity = self.cart[product_name]["Quantity"]
        self.total_bill += (Quantity - current_product_quantity) * product_obj.Price

        # Update the Quantity
        self.cart[product_name]["Quantity"] = Quantity
        print("product Quantity is updated")

    # Display the user product in the cart
    def show_cart_products(self):
        if self.cart == {}:
            print("Your Cart is empty add some products")
            return

        print("--Products in the Cart--")
        print("You have",end="")
        for key ,value in self.cart.items():
            print(f" {value['Quantity']} {key}" ,end=",")
        print("in the cart")
        print("Total Bill : $", self.total_bill)

    # Display the Available products
    def show_products_available(self):
        print("The Available Products : ")
        item_num = 1
        for product in self.products_List:
            print(f"{item_num}] Name:{product.Name}   Price:{product.Price}   Availability:{product.Availability}")
            item_num +=1



user1 = E_Commerce_Cart()
user1.add_product("laptop")
user1.show_cart_products()
user1.add_product("headphone")
user1.show_cart_products()
user1.update_quantity('headphone',7)
user1.show_cart_products()
