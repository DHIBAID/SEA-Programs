import pymysql
cnx = pymysql.connect(user='yourusername', password='yourpassword', host='localhost', database='yourdatabase')

cursor = cnx.cursor()
cursor.execute("SELECT * FROM tabledat LIMIT 3")
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
cnx.close()
