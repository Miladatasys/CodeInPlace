"""
Karel starts on a trail of beepers and must follow the path,
picking up each beeper until the trail ends.
Karel starts on a beeper and ends at the last one, facing East.
"""

from karel.stanfordkarel import *

def main():
    """
    Follows a trail of beepers by:
    - Collecting beepers in a straight path
    - Stepping back and checking for turns
    - Repeating until the trail ends
    """
    while beepers_present():
        follow_straight_trail()
        step_backwards()
        # Check left
        turn_left()
        move()
        if no_beepers_present():
            # Trail doesn't continue to the left, goes right
            step_backwards()
            turn_around()
            move()

    
# Mid-level helper functions
def follow_straight_trail():
    """
    Picks up beepers in a straight line until Karel hits a gap.
    Pre: Karel is on a beeper and facing the correct trail direction.
    Post: Karel stops on the first non-beeper tile.
    """
    while beepers_present():
        pick_beeper()
        move()


# Low-level helper functions
def turn_around():
    # Turns Karel 180 degrees.
    turn_left()
    turn_left()

def step_backwards():
    # Moves Karel back one step without changing final direction.
    turn_around()
    move()
    turn_around()

def turn_right():
    # Turns Karel right (90°) using three left turns.
    for i in range(3):
        turn_left()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()