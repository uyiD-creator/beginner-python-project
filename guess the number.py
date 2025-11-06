# Guess the Number Game

import random

print("Welcome to Guess the Number Game!")
print("I am thinking of a number between 1 and 10")

secret_number = random.randint(1, 10)
guess = None

while guess != secret_number:
    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Correct! You guessed the number!")
        
print("Thanks for playing!")
