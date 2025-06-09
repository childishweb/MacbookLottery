import random
def get_guess(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Not a number. Try again!")

# Use 1-45 inclusive as the valid lottery number range.
secret_numbers = random.sample(range(1, 46), 6)
print("Welcome to James's Macbook lottery! Guess 6 numbers (1-45).")

guesses = [get_guess(f"Number {i+1}: ") for i in range(6)]

if guesses == secret_numbers:
    print("Holy shit...i'm ruined")
else:
    print("HAHAHAH you FUCKING loser!!!! The numbers were:", secret_numbers)
