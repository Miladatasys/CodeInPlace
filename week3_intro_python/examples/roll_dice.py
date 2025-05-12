import random

# number of sides on each die to roll
NUM_SIDES = 6

def main():
    # setting seed is useful for debugging and will generate the same sequence of random numbers 
    random.seed(1) # If you're done testing the program you can comment the seed you set before. 
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2
    print("Dice have", NUM_SIDES, "sides each.")
    print("First die: ", die1)
    print("Second dice: ", die2)
    print("Total of two dice: ", total)

if __name__ == '__main__':
    main()