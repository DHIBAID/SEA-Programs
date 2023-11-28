def capitalize_first_last_letters(sentence):
    words = sentence.split()
    modified_words = [
        word[0].upper() + word[1:-1] + word[-1].upper() if len(word) > 1 else word.upper()
        for word in words
    ]
    return ' '.join(modified_words)

user_input = input("Enter a sentence: ")
result = capitalize_first_last_letters(user_input)
print("Modified sentence:", result)
