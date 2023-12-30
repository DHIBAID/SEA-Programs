import mysql.connector

cnx = mysql.connector.connect(user='yourusername', password='yourpassword', host='localhost', database='yourdatabase')
cursor = cnx.cursor()
cursor.execute("SELECT * FROM tableName WHERE no < 10")

row = cursor.fetchone()
while row is not None:
    print(row)
    row = cursor.fetchone()

cursor.close()
