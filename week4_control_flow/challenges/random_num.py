import random

N_NUMBERS = 10
MIN_VALUE = 1
MAX_VALUE = 100

def main():
    """
    Print 10 random numbers in the range 1 to 100.
    Each time you run your program you should get different numbers
    Recall that the python random library has a function randint
    which returns an integer in the range set by the parameters (inclusive). 
    """
    for i in range(N_NUMBERS):
        value = random.randint(MIN_VALUE, MAX_VALUE)
        print(value)

if __name__ == '__main__':
    main()