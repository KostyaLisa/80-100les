import math

def add(a, b):
    """Addition of two numbers."""
    return a + b

def subtract(a, b):
    """Subtraction of two numbers."""
    return a - b

def multiply(a, b):
    """Multiplication of two numbers."""
    return a * b

def divide(a, b):
    """Division of two numbers, handling division by zero."""
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None

def multiplication_table(n):
    """Print the multiplication table for a given number."""
    print(f"Multiplication table for {n}:")
    for i in range(1, 11):
        print(f"{n} * {i} = {n * i}")

def is_even_or_odd(n):
    """Check if a number is even or odd."""
    return "Even number" if n % 2 == 0 else "Odd number"

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def factorial(n):
    """Calculate the factorial of a number."""
    try:
        return math.factorial(n)
    except ValueError:
        print("Error: Invalid input. Please enter a non-negative integer.")
        return None

def main():
    while True:
        print("\n/Menu:")
        print("1. Calculator [SUM, SUBTRACT, MULTIPLY, DIVIDE]")
        print("2. Multiplication Table")
        print("3. Check if a number is even or odd")
        print("4. Check if a number is prime")
        print("5. Factorial")
        print("6. Exit")

        try:
            choice = int(input("Select an option (1-6): "))
        except ValueError:
            print("Error: Please enter a number from 1 to 6.")
            continue

        if choice == 1:
            try:
                a = float(input("Enter the first number: "))
                b = float(input("Enter the second number: "))
                operation = input("Enter operation (+, -, *, /): ")

                if operation == '+':
                    print("Result:", add(a, b))
                elif operation == '-':
                    print("Result:", subtract(a, b))
                elif operation == '*':
                    print("Result:", multiply(a, b))
                elif operation == '/':
                    result = divide(a, b)
                    if result is not None:
                        print("Result:", result)
                else:
                    print("Error: Invalid operation.")
            except ValueError:
                print("Error: Please enter valid numbers.")

        elif choice == 2:
            try:
                n = int(input("Enter a number for the multiplication table: "))
                multiplication_table(n)
            except ValueError:
                print("Error: Please enter an integer.")

        elif choice == 3:
            try:
                n = int(input("Enter a number: "))
                print(f"The number {n} is an {is_even_or_odd(n)}.")
            except ValueError:
                print("Error: Please enter an integer.")

        elif choice == 4:
            try:
                n = int(input("Enter a number to check for primality: "))
                if is_prime(n):
                    print(f"The number {n} is prime.")
                else:
                    print(f"The number {n} is not prime.")
            except ValueError:
                print("Error: Please enter an integer.")

        elif choice == 5:
            try:
                n = int(input("Enter a number to calculate the factorial: "))
                result = factorial(n)
                if result is not None:
                    print(f"The factorial of {n} is {result}.")
            except ValueError:
                print("Error: Please enter an integer.")

        elif choice == 6:
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Error: Please select a valid option from 1 to 6.")

# Run the program
main()
