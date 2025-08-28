import random

# Set the secret_number variable here (between 1 and 10)
secret_number = 7  # You can choose any number between 1 and 10

# Initialize the guess variable here with a value of 0
guess = 0

# While loop runs until guess matches the secret_number
while guess != secret_number:
    guess = random.randint(1, 10)
    print("Guessing:", guess)

print("I guessed the right number! It was", secret_number)
