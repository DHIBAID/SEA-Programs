with open('input.txt', 'r') as file:
    for line in file:
        words = line.split()
        print('#'.join(words))
