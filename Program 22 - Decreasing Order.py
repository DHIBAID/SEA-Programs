import sqlite3

with sqlite3.connect('dec.db') as conn:
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS student_marks (
                        Student_ID INTEGER PRIMARY KEY,
                        marks INTEGER
                    )''')

    sample_data = [(1, 85), (2, 72), (3, 90), (4, 68), (5, 78)]
    cursor.executemany('INSERT INTO student_marks VALUES (?, ?)', sample_data)
    conn.commit()

    [print(f"Student_ID: {row[0]}, Marks: {row[1]}")
    for row in cursor.execute('''SELECT Student_ID, marks FROM student_marks ORDER BY marks DESC''')]
