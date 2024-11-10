def divide_numbers():
    try:
        # Get user input for two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Perform division
        result = num1 / num2
    except ValueError:
        # Handle non-numeric input
        print("Invalid input! Please enter valid numbers.")
    except ZeroDivisionError:
        # Handle division by zero
        print("Error! Division by zero is not allowed.")
    else:
        # Print result if no exceptions were raised
        print(f"The result of dividing {num1} by {num2} is: {result:.2f}")


# Run the function
divide_numbers()
