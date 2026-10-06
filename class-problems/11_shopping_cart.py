# Problem Statement:
# Create a class ShoppingCart with customer name and cart ID.
# Initialize these values using a constructor.
# Implement methods to add products, remove products, and calculate the total bill.
# Use a destructor to display a message when the shopping cart object is destroyed.

class ShoppingCart:
    def __init__(self, customer_name, cart_id):
        self.customer_name = customer_name
        self.cart_id = cart_id
        self.products = []

    def add_product(self, product, price):
        self.products.append([product, price])
        print("Product added.")

    def remove_product(self, product):
        for item in self.products:
            if item[0] == product:
                self.products.remove(item)
                print("Product removed.")
                return
        print("Product not found.")

    def total_bill(self):
        return sum(item[1] for item in self.products)

    def display_cart(self):
        print("\nCustomer:", self.customer_name)
        print("Cart ID:", self.cart_id)

        for product, price in self.products:
            print(product, "-", price)

        print("Total Bill: Rs.", self.total_bill())

    def __del__(self):
        print("Shopping cart object destroyed.")


cart = ShoppingCart("Rahul", "C101")
cart.add_product("Laptop", 50000)
cart.add_product("Mouse", 800)
cart.add_product("Keyboard", 1500)
cart.remove_product("Mouse")
cart.display_cart()
