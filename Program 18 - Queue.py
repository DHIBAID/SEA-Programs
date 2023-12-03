class Member:
    def __init__(self, member_no, member_name, age):
        self.member_no, self.member_name, self.age = member_no, member_name, age

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0) if self.items else "Queue is empty"

member_queue = Queue()

member_queue.enqueue(Member(1, 'Alice', 25))
member_queue.enqueue(Member(2, 'Bob', 30))
member_queue.enqueue(Member(3, 'Charlie', 28))

print("Members before deletion:")
for member in member_queue.items:
    print(f"Member No.: {member.member_no}, Name: {member.member_name}, Age: {member.age}")

deleted_member = member_queue.dequeue()
print(f"\nDeleted Member - Member No.: {deleted_member.member_no}, Name: {deleted_member.member_name}, Age: {deleted_member.age}" if deleted_member != "Queue is empty" else "\nQueue is empty, nothing to delete.")

print("\nMembers after deletion:")
for member in member_queue.items:
    print(f"Member No.: {member.member_no}, Name: {member.member_name}, Age: {member.age}")
