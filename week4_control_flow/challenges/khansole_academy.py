"""
This program generates random simple addition problems
that involve adding two 2-digit intergers (i.e., the numbers
10 through 99). The user is asked for an answer to the generated 
problem and the program should determine if the answer is correct or not 
and give the user an appropriate message to let them know.
"""

import random

def main():
    print("Khansole Academy")
    # Generates 2 digits integers
    num1 = random.randint(10, 99)
    num2 = random.randint(10, 99)
    # Addition
    total = num1 + num2
    
    # User answer
    print(f"What is {num1} + {num2}?")
    user_input = int(input("Your answer: "))

    # Checks if it's correct
    if user_input != total:
        print(f"Incorrect.\nThe expected answer is {total}")
    else:
        print("Correct!")

    
if __name__ == '__main__':
    main()