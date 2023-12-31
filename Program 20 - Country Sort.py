import sqlite3

conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS customers (
                    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    customer_name TEXT,
                    country TEXT
                )''')

customers_data = [
    ('Alice', 'USA'),
    ('Bob', 'Canada'),
    ('Charlie', 'USA'),
    ('David', 'India'),
    ('Eva', 'Canada'),
    ('Frank', 'India')
]

cursor.executemany('INSERT INTO customers(customer_name, country) VALUES (?, ?)', customers_data)
conn.commit()

for row in cursor.execute('''SELECT country, COUNT(*) AS total_customers 
                            FROM customers 
                            GROUP BY country'''):
    print(f"Country: {row[0]}, Total Customers: {row[1]}")

conn.close()
