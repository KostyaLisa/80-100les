

# Get user input
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))


def calculate_bmi(weight, height):
    # Calculate BMI
    bmi = weight / (height ** 2)
    return bmi

def get_bmi_category(bmi):
    # Determine BMI category based on the calculated BMI
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal weight"
    elif 25.0 <= bmi <= 29.9:
        return "Overweight"
    elif 30.0 <= bmi <= 34.9:
        return "Grade 1 obesity"
    elif 35.0 <= bmi <= 39.9:
        return "Obesity grade 2"
    else:
        return "Grade 3 obesity (morbid obesity)"


# Calculate BMI
bmi = calculate_bmi(weight, height)

# Determine BMI category
category = get_bmi_category(bmi)

# Display the results
print(f"Your BMI is: {bmi:.2f}")
print("BMI Category:", category)