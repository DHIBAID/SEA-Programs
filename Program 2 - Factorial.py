n = int(input("Enter number: "))
factorial = 1

if n < 0:
    print("n > 0 only")
    quit(0)

while n > 0:
    factorial *= n
    n -= 1

print(f"Factorial is {factorial}")