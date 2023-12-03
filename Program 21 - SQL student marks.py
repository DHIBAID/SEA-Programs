import sqlite3

conn = sqlite3.connect('student_database.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS student_marks (
                    student_id INTEGER PRIMARY KEY,
                    student_name TEXT,
                    marks INTEGER
                )''')

sample_data = [
    (1, 'Alice', 85),
    (2, 'Bob', 72),
    (3, 'Charlie', 90),
    (4, 'David', 68),
    (5, 'Eva', 78)
]

cursor.executemany('INSERT INTO student_marks VALUES (?, ?, ?)', sample_data)
conn.commit()

cursor.execute('''SELECT MIN(marks) AS min_marks, MAX(marks) AS max_marks, SUM(marks) AS total_marks, AVG(marks) AS avg_marks 
                FROM student_marks''')

result = cursor.fetchone()
if result:
    min_marks, max_marks, total_marks, avg_marks = result
    print(f"Minimum Marks: {min_marks}\nMaximum Marks: {max_marks}\nTotal Marks: {total_marks}\nAverage Marks: {avg_marks}")
else:
    print("No data found in the table.")

conn.close()
