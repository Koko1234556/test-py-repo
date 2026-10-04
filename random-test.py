import random

# Simple random test code
values = [10, 20, 30, 40, 50]
roll = random.choice(values)
print(f"Random value: {roll}")

if roll >= 30:
    print("You rolled a high number!")
else:
    print("You rolled a low number!")