import sqlite3

# Connect to the database
conn = sqlite3.connect('loja.db')
cursor = conn.cursor()

# List of fictitious products to insert
products = [
    ("Laptop", 1200.99, 10),
    ("Smartphone", 699.99, 25),
    ("Tablet", 299.99, 30),
    ("Headphones", 59.99, 100),
    ("Smartwatch", 149.99, 50),
    ("Keyboard", 39.99, 75),
    ("Mouse", 25.99, 80),
    ("Monitor", 199.99, 40),
    ("External Hard Drive", 89.99, 60),
    ("USB Flash Drive", 9.99, 200)
]

# Insert multiple products using executemany
cursor.executemany('''
    INSERT INTO products (name, price, stock)
    VALUES (?, ?, ?)
''', products)

# Commit changes and close the connection
conn.commit()
conn.close()

print("Products inserted successfully.")
