import random

secret_number = random.randint(1, 99)
print("I am thinking of a number between 1 and 99...")
# This is fence post problem! :D before the loop the guess has a value
guess = int(input("Enter a guess: "))
# True if guess is not equal to secret number
while guess != secret_number:
    # True if guess is less than secret number
    if guess < secret_number:
        print("Your guess is to low")
    else:
        print("Your guess is too high")

    print("") # an empty line
    guess = int(input("Enter a new guess: "))

print(f"Congrats! The number was: {secret_number}")