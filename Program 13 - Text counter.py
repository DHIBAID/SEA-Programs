with open('input.txt', 'r') as file:
    content = file.read()
    vowels = sum(1 for char in content if char.lower() in 'aeiou')
    consonants = sum(1 for char in content if char.isalpha() and char.lower() not in 'aeiou')
    uppercase = sum(1 for char in content if char.isupper())
    lowercase = sum(1 for char in content if char.islower())

print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
print(f"Uppercase characters: {uppercase}")
print(f"Lowercase characters: {lowercase}")
