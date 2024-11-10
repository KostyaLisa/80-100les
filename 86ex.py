import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('loja.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create the products table with specified columns
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        stock INTEGER NOT NULL
    )
''')

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database and table created successfully.")
