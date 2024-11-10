import sqlite3

# Connect to the database
conn = sqlite3.connect('loja.db')
cursor = conn.cursor()

# Update the prices of products with ids 5, 6, and 7
cursor.execute("UPDATE products SET price = 159.99 WHERE id = 5")  # Change price for Smartwatch
cursor.execute("UPDATE products SET price = 44.99 WHERE id = 6")    # Change price for Keyboard
cursor.execute("UPDATE products SET price = 29.99 WHERE id = 7")    # Change price for Mouse

# Commit changes and close the connection
conn.commit()
conn.close()

print("Prices updated successfully.")
