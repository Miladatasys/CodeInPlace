"""
This program prompts the user to type an affirmation of coder choice,
until they type it incorrectly. 
"""

AFFIRMATION = "I am capable of doing anything I put my mind to."

def main():
    print(f"Please type the following affirmation: {AFFIRMATION}") 
    
    # Get's user input
    user_feedback = input()

    """
    While the user's input isn't the affirmation we tell the user that they did not type the affirmation correctly
    """
    while user_feedback != AFFIRMATION:
        print("That was not the affirmation.")
        
        # Aks the user to type the affirmation again!
        print(f"Please type the following affirmation:{AFFIRMATION} ")
        user_feedback = input()

    # Print confirmation
    print("That's right! :)")


if __name__ == '__main__':
    main()