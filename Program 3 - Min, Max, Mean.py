list_input = str(input("Enter Numerical values seperated by ',': "))
list_input = list_input.split(",")
list_input.sort()
list_input = [eval(i) for i in list_input]

mean = sum(list_input) / len(list_input)
min = list_input[0]
max = list_input[len(list_input) - 1]

print(f"Mean = {mean}, Min = {min}, Max = {max}")
