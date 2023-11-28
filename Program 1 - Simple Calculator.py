num1, num2 = float(input("Number 1: ")), float(input("Number 2: "))
res = 0
operation = input("Operation to perform [+, -, *, /]: ")

if operation == "+":
    res = num1 + num2
elif operation == "-":
    res = num1 - num2
elif operation == "*":
    res = num1 * num2
elif operation == "/":
    res = num1 / num2
else: 
    print("Wrong input.")
    quit(0)

print(res)