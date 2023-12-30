import mysql.connector

cnx = mysql.connector.connect(user='yourusername', password='yourpassword', host='localhost', database='yourdatabase')
cursor = cnx.cursor()

cursor.execute("""
CREATE TABLE People (
    name VARCHAR(255),
    age INT
)
""")

names_ages = [
    ('John', 23), ('Amy', 21), ('Mike', 25),
    ('Emma', 22), ('Brad', 24), ('Sophia', 26),
    ('Daniel', 27), ('Olivia', 28), ('Max', 29),
    ('Isabella', 30)]
stmt = "INSERT INTO People (name, age) VALUES (%s, %s)"
cursor.executemany(stmt, names_ages)

cnx.commit()
cursor.execute("SELECT * FROM People ORDER BY age DESC")

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
cnx.close()
