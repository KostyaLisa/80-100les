class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades  # List of grades

    # Method to calculate the average of the grades
    def calculate_average(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        else:
            return 0

    # Method to check the student's status
    def check_status(self):
        average = self.calculate_average()
        if average >= 10:
            return "Approved"
        else:
            return "Failed"

# Create an instance of the Student class
student1 = Student("Alice", [12, 15, 10, 9, 14])

# Calculate the average and check the status
average = student1.calculate_average()
status = student1.check_status()

# Display the results
print(f"Student: {student1.name}")
print(f"Average Grade: {average:.2f}")
print(f"Status: {status}")
