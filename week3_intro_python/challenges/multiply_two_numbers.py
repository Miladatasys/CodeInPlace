"""
Program: multiply two numbers
--------------------
This program asks the user for two
integers and prints the value of the first number
multiplied with the second
Steps:
    1. Prompt the user to enter the first num
    2. Read the input and convert it to an int
    3. Prompt the user to enter the second num
    4. Read the input and convert it to an int
    5. Calculate the value of multiplying the two numbers
    6. Print the value

"""

def main():
    print("This program multiplies two numbers.")
    num1 = input("Enter first number: ")
    num1 = int(num1)
    num2 = input("Enter second number: ")
    num2 = int(num2)
    total = num1 * num2
    print(str(total))


if __name__ == '__main__':
    main()