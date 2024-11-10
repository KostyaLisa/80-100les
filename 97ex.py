class Book:
    def __init__(self, title, year, author, availability=True):
        # Private attributes
        self.__title = title
        self.__year = year
        self.__author = author
        self.__availability = availability

    # Getter and Setter for Title
    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    # Getter and Setter for Year
    def get_year(self):
        return self.__year

    def set_year(self, year):
        if isinstance(year, int) and year > 0:
            self.__year = year
        else:
            print("Please enter a valid year.")

    # Getter and Setter for Author
    def get_author(self):
        return self.__author

    def set_author(self, author):
        self.__author = author

    # Getter and Setter for Availability
    def is_available(self):
        return self.__availability

    def set_availability(self, availability):
        if isinstance(availability, bool):
            self.__availability = availability
        else:
            print("Availability should be a boolean value.")


# Create an instance of the Book class
book = Book("1984", 1949, "George Orwell")

# Access attributes using getter methods
print(f"Title: {book.get_title()}")
print(f"Year: {book.get_year()}")
print(f"Author: {book.get_author()}")
print(f"Availability: {'Available' if book.is_available() else 'Not Available'}")

# Modify attributes using setter methods
book.set_year(1950)
book.set_availability(False)

# Display updated information
print("\nUpdated Information:")
print(f"Year: {book.get_year()}")
print(f"Availability: {'Available' if book.is_available() else 'Not Available'}")
