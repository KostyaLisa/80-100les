class Product:
    def __init__(self, name, quantity_in_stock=0):
        self.name = name
        self._quantity_in_stock = max(0, quantity_in_stock)  # Ensure non-negative stock

    # Property for quantity_in_stock with a getter and a setter
    @property
    def quantity_in_stock(self):
        return self._quantity_in_stock

    @quantity_in_stock.setter
    def quantity_in_stock(self, quantity):
        if quantity >= 0:
            self._quantity_in_stock = quantity
        else:
            print("Quantity cannot be negative.")

    # Method to display the current stock
    def show_stock(self):
        print(f"The product '{self.name}' has {self._quantity_in_stock} units in stock.")

    # Method to increase the stock by a given amount
    def add_stock(self, amount):
        if amount > 0:
            self._quantity_in_stock += amount
            print(f"Added {amount} units to '{self.name}'. New stock: {self._quantity_in_stock}")
        else:
            print("Please add a positive amount to the stock.")

# Example usage
product = Product("Widget", 10)

# Display current stock
product.show_stock()

# Add stock
product.add_stock(5)

# Show updated stock
product.show_stock()

# Attempt to set negative stock (should be prevented)
product.quantity_in_stock = -3

# Show final stock
product.show_stock()
