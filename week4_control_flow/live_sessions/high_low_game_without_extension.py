"""
1.  Two nums are generated from 1 to 100: one for player, one for a computer (opponent). 
    Player can't sees computer num
2.  Player make a guess saying their number is either higher 
    than or lower than computer's number.
3.  If player guess matches truth, player get's a point. 
4.  Game's over after all rounds have been played.    
"""
import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')
    # Milestone #5: Adding a points system
    score = 0

    # Milestone #4: Play multiple rounds
    for i in range(NUM_ROUNDS):
        print(f"Round {i + 1}")

        # Milestone #1: Generates the random numbers
        computer_number = random.randint(1, 100)
        player_number = random.randint(1, 100)

        """
        Temporarily print computer num for testing
        print(f"Computer number is {computer_number}")
        """
        print(f"Your number is {player_number}")

        # Milestone #2: Get the user choice
        player_guess = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()

        # Milestone #3: Write program logic
        higher_and_correct = player_guess == "higher" and player_number > computer_number
        lower_and_correct = player_guess == "lower" and player_number < computer_number

        if higher_and_correct or lower_and_correct:
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")
        print(f"Your score is now {score}")
        print()

    print("Thanks for playing!")

if __name__ == "__main__":
    main()