class EmployeeStack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return not self.stack

    def push(self, emp_number, emp_name):
        self.stack.append((emp_number, emp_name))

    def pop(self):
        return self.stack.pop() if self.stack else "Stack is empty"

    def display(self):
        if not self.is_empty():
            print("Employee Details:")
            [print(f"Employee Number: {emp_number}, Employee Name: {emp_name}") for emp_number, emp_name in self.stack[::-1]]
        else:
            print("Stack is empty")


emp_stack = EmployeeStack()

[emp_stack.push(num, name) for num, name in [(101, 'Alice'), (102, 'Bob'), (103, 'Charlie')]]

emp_stack.display()

deleted_employee = emp_stack.pop()
print(f"\nDeleted Employee - Employee Number: {deleted_employee[0]}, Employee Name: {deleted_employee[1]}" if deleted_employee != "Stack is empty" else "\nStack is empty, nothing to delete.")
