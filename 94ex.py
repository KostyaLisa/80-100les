import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius  # Private attribute to store the radius

    # Getter method for radius
    def get_radius(self):
        return self.__radius

    # Setter method for radius
    def set_radius(self, radius):
        if radius > 0:
            self.__radius = radius
        else:
            print("Radius must be a positive number.")

    # Method to calculate the area of the circle
    def area(self):
        return math.pi * (self.__radius ** 2)

    # Method to calculate the perimeter (circumference) of the circle
    def perimeter(self):
        return 2 * math.pi * self.__radius

# Create an instance of the Circle class
circle = Circle(5)

# Get the radius using the getter method
print(f"Radius of the circle: {circle.get_radius()}")

# Calculate the area and perimeter
print(f"Area of the circle: {circle.area():.2f}")
print(f"Perimeter (Circumference) of the circle: {circle.perimeter():.2f}")

# Set a new radius using the setter method
circle.set_radius(7)

# Get the updated radius
print(f"Updated radius of the circle: {circle.get_radius()}")

# Recalculate area and perimeter with the new radius
print(f"Updated area of the circle: {circle.area():.2f}")
print(f"Updated perimeter (Circumference) of the circle: {circle.perimeter():.2f}")
