import mysql.connector

try:
    conn = mysql.connector.connect(
        host='your_host',
        user='your_username',
        password='your_password',
        database='your_database'
    )
    
    if conn.is_connected():
        print('Connected to MySQL database')

except mysql.connector.Error as e:
    print(f"Error connecting to MySQL database: {e}")

finally:
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print('Disconnected from MySQL database')
