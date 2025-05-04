from karel.stanfordkarel import *
"""
Karel will start in one dead end, 
and so long as Karel moves forwards through the laberynth,
Karel will eventually end up at the other dead end.
Steps:
1. Move to wall
2. Check if left is open
3. Else if right is open
4. Karel is at the final dead end (stop)
"""

def main():
    """
    The program will allow Karel to solve any labyrinth.
    Karel will always start facing the open direction
    A hint: Solving the problem means moving until you hit a wall, 
    reorienting yourself to turn whichever way is open
    (but not going back) If both directions are blocked, 
    it doesn't matter which way Karel faces
    """
    while front_is_clear():
        move_to_wall()
        find_direction()

def move_to_wall():
    """
    Moves Karel forward until it hits a wall

    Precondition:   Karel is facing an open path
    Postcondition:  Karel is facing a wall directly in front,
                    standing on the last open square of the corridor
    """
    while front_is_clear():
        move()

# Helper functions
def find_direction():
    """
    Determines which side (left or right) is clear, 
    and turns Karel to face that direction
    Precondition: Karel is facing wall
    Postcondition: Karel is now facing the only open direction
    """
    if left_is_clear():
        turn_left()
    if right_is_clear():
        turn_right()

def turn_right():
    for _ in range(3):
        turn_left()

def turn_around():
    turn_left()
    turn_left()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()