import math


def calculate_roots(a, b, c):
    d = b**2 - 4 * a * c
    if d > 0:
        return ((-b + math.sqrt(d)) / (2 * a), (-b - math.sqrt(d)) / (2 * a))
    elif d == 0:
        return (-b / (2 * a), -b / (2 * a))
    else:
        return (
            f"{-b / (2*a)} + {math.sqrt(abs(d)) / (2*a)}i",
            f"{-b / (2*a)} - {math.sqrt(abs(d)) / (2*a)}i",
        )


a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

roots = calculate_roots(a, b, c)
print("The roots are complex:" if isinstance(roots[0], str) else "The roots are:")
for r in roots:
    print(r)
