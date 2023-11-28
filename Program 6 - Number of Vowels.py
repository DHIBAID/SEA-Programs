def count_vowels(s):
    return sum(1 for char in s if char.lower() in 'aeiou')

def main():
    user_input = input("Enter a string: ")
    vowels_count = count_vowels(user_input)
    print(f"The total number of vowels in the string is: {vowels_count}")

main()
