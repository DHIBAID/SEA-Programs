class StudentInformation:
    def __init__(self):
        self.students = {}

    def add_student(self, a, r, n, m):
        self.students[a] = {'Roll Number': r, 'Name': n, 'Marks': m}

    def display_student_info(self, a):
        s = self.students.get(a)
        if s:
            print(f"Student Information:\nAdmission Number: {a}\nRoll Number: {s['Roll Number']}\nName: {s['Name']}\nMarks: {s['Marks']}")
        else:
            print("Student with this admission number doesn't exist.")

s = StudentInformation()
for _ in range(int(input("Enter the number of students: "))):
    a, r, n, m = input("Enter admission, roll, name, marks: ").split()
    s.add_student(a, r, n, m)

s.display_student_info(input("Enter admission number to search: "))