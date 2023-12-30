'''
SQL
CREATE DATABASE SHOP ; 
USE SHOP ; 
CREATE TABLE PRODUCT 
(
    p_ID	VARCHAR(512),
    product	VARCHAR(512),
    Manufacture	VARCHAR(512),
    PRICE	INT,
    DISCOUNT	VARCHAR(512)
);

INSERT INTO PRODUCT (p_ID, product, Manufacture, PRICE, DISCOUNT) VALUES
	('TP01', 'Talcum powder', 'LAK', '40', ''),
	('FW05', 'Face wash', 'ABC', '45', '5'),
	('BS01', 'bath soap', 'ABC', '55', ''),
	('SH06', 'Shampoo', 'XYZ', '120', '10'),
	('FW12', 'Face wash', 'XYZ', '95', '');

CREATE TABLE CLIENT 
(
    C_ID	INT,
    CLIENTNAME	VARCHAR(512),
    CITY	VARCHAR(512),
    P_ID	VARCHAR(512)
);

INSERT INTO CLIENT (C_ID, CLIENTNAME, CITY, P_ID) VALUES
	('1', 'COSMETIC SHOP', 'DELHI', 'TP01'),
	('2', 'TOTAL HEALTH', 'MUMBAI', 'FW05'),
	('3', 'LIVE LIFE', 'DELHI', 'BS01'),
	('4', 'PRETTY WOMAN', 'DELHI', 'SH06'),
	('5', 'DREAMS', 'DELHI', 'FW12');

    
SELECT Product, PRICE
FROM PRODUCT
WHERE Price BETWEEN 50 AND 150;


SELECT *
FROM product
WHERE Manufacture IN ('XYZ', 'ABC');


SELECT Product, Manufacture , Price
FROM product
WHERE Discount IS NULL OR Discount = 0;

SELECT Product, Price
FROM product
WHERE Product LIKE '%h';

Select CLIENTNAME , City , P_ID and Product form where City = “Delhi” ;

SELECT P_ID FROM CLIENT ; 
'''

import mysql.connector

cnx = mysql.connector.connect(
    host='your_host',
    user='your_user',
    password='your_password',
    database='your_database'
)

cursor = cnx.cursor()

query1 = "SELECT ProductName, Price FROM products WHERE Price BETWEEN 50 AND 150"
cursor.execute(query1)
print("Products with price between 50 and 150:")
for row in cursor:
    print(row)

query2 = "SELECT * FROM products WHERE Manufacturer IN ('XYZ', 'ABC')"
cursor.execute(query2)
print("\nProducts manufactured by XYZ or ABC:")
for row in cursor:
    print(row)
