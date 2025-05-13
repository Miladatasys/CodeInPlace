"""
This program asks the user how tall they are 
and prints whether or not they're taller 
than a pre-specified minimum height.
"""
MINIMUM_HEIGHT = 50 # constant

def main():
    # Ask the user for their height
    user_height = input("How tall are you? ")

    # Loop until the user enters an empty string
    while user_height != "":
        height = float(user_height) 

        # Check if height meets requirement
        if height >= MINIMUM_HEIGHT:
            print("You're tall enough to ride!")
        else:
            print("You're not tall enough to ride, but maybe next year!")

        # Ask again, and update the same variable used in the condition
        user_height = input("How tall are you? ")

if __name__ == '__main__':
    main()