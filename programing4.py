import random

num = random.randint(1, 100)
guess = input("Guess (odd/even): ").lower()

if num % 2 == 0:
    actual = "even"
else:
    actual = "odd"

print("Random Number:", num)

if guess == actual:
    print("Correct Guess")
else:
    print("Wrong Guess. It is", actual)

# Output:
# Guess (odd/even): even
# Random Number: 42
# Correct Guess
