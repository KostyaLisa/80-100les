import sqlite3

# Function to connect to the database
def connect_db():
    return sqlite3.connect('loja.db')

# Function to add a new product
def add_product(name, price, stock):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, price, stock) VALUES (?, ?, ?)", (name, price, stock))
    conn.commit()
    conn.close()
    print("Product added successfully.")

# Function to show all products
def show_all_products():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()
    print("\nAll Products:")
    print("ID | Name | Price | Stock")
    print("-" * 30)
    for product in products:
        print(f"{product[0]:<3} | {product[1]:<15} | ${product[2]:<7.2f} | {product[3]}")

# Function to update an existing product
def update_product(product_id, name=None, price=None, stock=None):
    conn = connect_db()
    cursor = conn.cursor()

    # Update fields only if new values are provided
    if name is not None:
        cursor.execute("UPDATE products SET name = ? WHERE id = ?", (name, product_id))
    if price is not None:
        cursor.execute("UPDATE products SET price = ? WHERE id = ?", (price, product_id))
    if stock is not None:
        cursor.execute("UPDATE products SET stock = ? WHERE id = ?", (stock, product_id))

    conn.commit()
    conn.close()
    print("Product updated successfully.")

# Main menu
def main():
    while True:
        print("\nMenu:")
        print("1. Add a new product")
        print("2. Show all products")
        print("3. Update an existing product")
        print("4. Exit")

        try:
            choice = int(input("Choose an option (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 4.")
            continue

        if choice == 1:
            # Add new product
            name = input("Enter product name: ")
            try:
                price = float(input("Enter product price: "))
                stock = int(input("Enter product stock: "))
            except ValueError:
                print("Invalid input. Price should be a number and stock an integer.")
                continue
            add_product(name, price, stock)

        elif choice == 2:
            # Show all products
            show_all_products()

        elif choice == 3:
            # Update product
            try:
                product_id = int(input("Enter the ID of the product to update: "))
                print("Leave fields blank to keep current values.")
                name = input("Enter new name (or press Enter to skip): ").strip() or None
                price_input = input("Enter new price (or press Enter to skip): ").strip()
                price = float(price_input) if price_input else None
                stock_input = input("Enter new stock (or press Enter to skip): ").strip()
                stock = int(stock_input) if stock_input else None
            except ValueError:
                print("Invalid input. Please make sure IDs and numbers are valid.")
                continue
            update_product(product_id, name, price, stock)

        elif choice == 4:
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose a number from 1 to 4.")

# Run the program
main()
