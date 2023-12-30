'''
SQL 
create database rand ; 
use rand ; 
CREATE TABLE tab 
(
    no	INT,
    marks	INT
);

INSERT INTO tab (no, marks) VALUES
	('1', '55'),
	('2', '65'),
	('3', '3'),
	('4', '79'),
	('5', '54'),
	('6', '37'),
	('7', '87'),
	('8', '32'),
	('9', '78'),
	('10', '90'),
	('11', '85');
update tab  set marks = 22  WHERE no =3 ; 
delete from tab where no = 2 ; 
'''

import mysql.connector as mysc

con = mysc.connect(host='localhost', user='yourusername', password='yourpassword', database='youdatabase')

print(con)
cursor=con.cursor()
cursor.execute("select * from tab ")
display = cursor.fetchall()

for i in display:
    print(i)
    
cursor.execute("update tab  set marks = 22  WHERE no =3")
cursor.execute('delete from tab where no = 2')
