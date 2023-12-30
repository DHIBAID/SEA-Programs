import pickle

class Student:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

def insert_record(file_name, student):
    with open(file_name, "ab") as file:
        pickle.dump(student, file)
        print("Record inserted/appended successfully.")

new_student = Student(101, "Alice", 20)
insert_record("student.dat", new_student)
