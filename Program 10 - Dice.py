import random

def roll_dice():
    return random.randint(1, 6)

result = roll_dice()
print("The dice rolled:", result)
