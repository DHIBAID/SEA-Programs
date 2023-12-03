import pickle

def load_data():
    try:
        with open('students_data.bin', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return {}

def save_data():
    with open('students_data.bin', 'wb') as file:
        pickle.dump(records, file)

def insert_record():
    records[input("Enter student ID: ")] = {'Name': input("Enter student name: "), 'Age': input("Enter student age: ")}
    save_data()

def read_record():
    [print(f"Student ID: {id}, Name: {info['Name']}, Age: {info['Age']}") for id, info in records.items()]

def update_record():
    student_id = input("Enter student ID to update: ")
    if student_id in records:
        records[student_id] = {'Name': input("Enter updated name: "), 'Age': input("Enter updated age: ")}
        save_data()
    else:
        print("Student ID not found.")

def search_record():
    info = records.get(input("Enter student ID to search: "), "Student ID not found.")
    if info != "Student ID not found.":
        print(f"Student ID: {input}, Name: {info['Name']}, Age: {info['Age']}")
    else:
        print("Student ID not found.")

def delete_record():
    student_id = input("Enter student ID to delete: ")
    if student_id in records:
        del records[student_id]
        save_data()
        print("Record deleted successfully.")
    else:
        print("Student ID not found.")

records = load_data()

while True:
    print("\nMenu:\n1. Insert Record\n2. Read Records\n3. Update Record\n4. Search Record\n5. Delete Record\n6. Exit")
    choice = input("Enter your choice (1-6): ")
    
    if choice == '1': insert_record()
    elif choice == '2': read_record()
    elif choice == '3': update_record()
    elif choice == '4': search_record()
    elif choice == '5': delete_record()
    elif choice == '6': break
    else: print("Invalid choice. Please enter a valid option.")
