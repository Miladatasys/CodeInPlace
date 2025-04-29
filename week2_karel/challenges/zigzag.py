from karel.stanfordkarel import *
"""
Karel is at the bottom left corner where
should place a beeper and follow a zig zag pattern of beepers
such as all odd columns have beepers in row 1 and all even columns
have beepers in row 2. The world will always have 2 rows and
an even number of columns. Karel should end up in the bottom of
the right corner of the world. 
"""

def main():
    """
    Places beepers in a zig zag pattern across the world
    Pre:    Karel start at (1,1) facing East with no beepers.
    Post:   Karel ends up at the bottom-right corner, 
            facing East, with beepers in a zig-zag pattern
    """
    

    
def place_beeper_and_move_up():
    """
    Turns North, moves up one row, turns East to continue placing beepers.
    Pre: Karel is facing East at bottom row.
    Post: Karel is facing East at top row.
    """
    pass


def return_to_bottom_row():
    """
    Turns South, moves down one row, and turns East to continue.
    Pre: Karel is facing East at top row.
    Post: Karel is facing East at bottom row.
    """
    pass



# Low-level helper functions
def turn_right():
    for _ in range(3):
        turn_left()

def turn_around():
    turn_left()
    turn_left()

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()