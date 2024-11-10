class Temperature:
    def __init__(self, celsius=0.0):
        self.__celsius = celsius  # Private attribute for temperature in Celsius

    # Property for Celsius with getter and setter
    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, value):
        self.__celsius = value

    # Method to convert Celsius to Fahrenheit
    def to_fahrenheit(self):
        return (self.__celsius * 9/5) + 32

    # Method to convert Celsius to Kelvin
    def to_kelvin(self):
        return self.__celsius + 273.15

# Example usage
temperature = Temperature(25)  # Initialize with 25°C

# Access and modify temperature in Celsius
print(f"Temperature in Celsius: {temperature.celsius}°C")
temperature.celsius = 30
print(f"Updated Temperature in Celsius: {temperature.celsius}°C")

# Convert to Fahrenheit and Kelvin
print(f"Temperature in Fahrenheit: {temperature.to_fahrenheit()}°F")
print(f"Temperature in Kelvin: {temperature.to_kelvin()}K")
