class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

# Create three instances of the Book class
book1 = Book("To Kill a Mockingbird", "Harper Lee")
book2 = Book("1984", "George Orwell")
book3 = Book("Pride and Prejudice", "Jane Austen")

# Print the attributes of each book
print(f"Book 1 - Title: {book1.title}, Author: {book1.author}")
print(f"Book 2 - Title: {book2.title}, Author: {book2.author}")
print(f"Book 3 - Title: {book3.title}, Author: {book3.author}")
