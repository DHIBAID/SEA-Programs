integers = list(map(int, input("Enter integers separated by spaces: ").split()))
with open('integers.bin', 'wb') as file:
    file.write(b''.join(num.to_bytes(4, 'big') for num in integers))

with open('integers.bin', 'rb') as file:
    read_integers = [int.from_bytes(file.read(4), 'big') for _ in range(len(integers))]

print("Integers read from file:", read_integers)
