import sqlite3

with sqlite3.connect('students.db') as conn:
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Students (
                        Reg_No TEXT PRIMARY KEY,
                        Sname TEXT,
                        Age INTEGER,
                        Dept TEXT,
                        Class TEXT
                    )''')

    students_data = [
        ('M1001', 'Harish', 19, 'ME', 'ME1'),
        ('M1002', 'Akash', 20, 'ME', 'ME2'),
        ('C1001', 'Sneha', 20, 'CSE', 'CS1'),
        ('C1002', 'Lithya', 19, 'CSE', 'CS2'),
        ('E1001', 'Ravi', 20, 'ECE', 'EC1'),
        ('E1002', 'Leena', 21, 'EEE', 'EE1'),
        ('E1003', 'Rose', 20, 'ECE', 'EC2')
    ]

    cursor.executemany('INSERT INTO Students VALUES (?, ?, ?, ?, ?)', students_data)

    queries = [
        '''SELECT * FROM Students WHERE Dept = 'CSE' ''',
        '''SELECT * FROM Students WHERE Dept = 'ME' AND Age >= 20 ''',
        '''SELECT Dept, COUNT(*) AS Total_Students FROM Students GROUP BY Dept ''',
        '''UPDATE Students SET Class = 'ME1' WHERE Class = 'ME2' ''',
        '''SELECT Reg_No, COUNT(*) AS Count_Reg_No FROM Students GROUP BY Reg_No HAVING COUNT_Reg_No > 1 '''
    ]

    [print(cursor.fetchall()) for query in queries for _ in cursor.execute(query)]
