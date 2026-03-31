import sqlite3

def setup_database():
    # Connect to (or create) the database file
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    
    # Create a table
    cursor.execute('''CREATE TABLE IF NOT EXISTS products 
                     (id INTEGER PRIMARY KEY, name TEXT, price REAL)''')
    
    # Insert data safely using tuples to prevent SQL injection
    sample_data = [('Laptop', 999.99), ('Mouse', 25.50), ('Monitor', 150.00)]
    cursor.executemany('INSERT INTO products (name, price) VALUES (?, ?)', sample_data)
    
    conn.commit()
    
    # Fetch and display
    cursor.execute('SELECT * FROM products WHERE price > 50')
    print("Expensive Items:")
    for row in cursor.fetchall():
        print(f"ID: {row} | Product: {row} | Price: ${row}")
    
    conn.close()

# setup_database()