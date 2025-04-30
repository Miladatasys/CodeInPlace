"""
Karel starts in the bottom left corner 
of a world with 2 empty flower stems, facing East.
Karel should bloom both flowers with beepers 
and end in the bottom right corner of the world facing East.
"""
from karel.stanfordkarel import *

def main():
        # bloom_flower()
    pass

def bloom_flower():
    """
    Moves Karel to the base of the first flower,
    Moves Karel up the flower, blooms the flower, moves Karel back
    down and turns her to face East
    """
    pass

def move_to_wall():
    # Moves Karel forward until she is block
    pass

def climb_stem():
    """
    Moves Karel up the stem util top
    Precondition:   Karel starts facing East at the base
    Postcondition:  Karel's at the top, in the bottom left corner
                    of the bloom facing North
    """
    pass

# Mid-level helper functions
def bloom():
    """
    Places 4 beepers in a square.
    Precondition:   Karel starts off at the bottom left corner 
                    of the square
    Postcondition:  End up at the bottom right corner of the square,
                    facing South
    """
    pass


# Low-level helper functions
def turn_around():
    # Turns 180°
    turn_left()
    turn_left()

def turn_right():
    # Turns 90°
    for i in range(3):
        turn_left()
   

if __name__ == '__main__':
    main()