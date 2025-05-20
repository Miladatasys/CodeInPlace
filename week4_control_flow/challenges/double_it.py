import math

def main():
    """
    This program will ask a user to enter a number and then
    will double that number and print out the result. 
    It will repeat that process until the value is 100 or greater. 
    """
    curr_value = int(input("Enter a number: "))
    """
    1. Print the current value
    2. Double the current value
    3. The loop continues
    """
    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value)

        

if __name__ == '__main__':
    main()