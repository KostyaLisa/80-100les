class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe(self):
        print(f"The book titled '{self.title}' was written by author {self.author}.")

# Create three instances of the Book class
book1 = Book("To Kill a Mockingbird", "Harper Lee")
book2 = Book("1984", "George Orwell")
book3 = Book("Pride and Prejudice", "Jane Austen")

# Call the describe method for each book
book1.describe()
book2.describe()
book3.describe()
