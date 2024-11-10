class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

    def show_stock(self):
        print(f"Product '{self.name}' has {self.stock} units in stock.")

    def increase_stock(self, amount):
        if amount > 0:
            self.stock += amount
            print(f"Stock of '{self.name}' increased by {amount} units.")
        else:
            print("Please enter a positive amount to increase the stock.")

# Create an instance of the Product class
product1 = Product("Laptop", 10)

# Display current stock
product1.show_stock()

# Increase the stock by a given amount and display updated stock
product1.increase_stock(5)
product1.show_stock()
