"""
Karel has been asked to make a Zebra crossing. 
In the world of Karel, a Zebra crossing is defined
as a pattern beginning with a 2-square wide column of beepers,
followed by repeating pairs of a 3-square wide gap
and a 2-square wide column of beepers.
steps:
1. Build first column
2. Build second column
3. Cross the gap.
"""

from karel.stanfordkarel import *
def main():
    """
    The objective is to allows Karel to make a Zebra crossing.
    The program should work for any world that meets the criteria below:
    -   The world will be at least 7 squares wide
    -   The world will be precisely wide enough to begin and end with 
        a column of two beepers.
    """
    while front_is_clear():
        build_zebra_crossing()


def build_zebra_crossing():
    """
    Coordinates the full pattern of repeating beeper columns and gaps across the world
    Precondition:   Karels at (1,1) position, facing east
    Postcondition:  Karel is at the bottom right, facing East with the pattern built
    """
    build_column()
    build_second_column()
    if front_is_clear():
        cross_gap()
    
    
# mid-level Helper functions
def build_column():
    """
    Builds one vertical column of beepers (2 rows)
    Precondition:   Karel is on row 1, facing East, at start of column
    Postcondition:  Karel has placed 2 beepers vertically and is on row 1, 
                    one column to the right, facing East
    """
    turn_left()
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()

def build_second_column():    
    turn_right()
    move()
    put_beeper()
    turn_right()
    while front_is_clear():
        move()
        put_beeper()
    turn_left()


def cross_gap():
    """
    Moves Karel across the 3 horizontal gap to the next column
    Precondition:   Karel is in row 1, facing East, just pass a beeper column
    Postcondition:  Karel is now on row 1, facing East, 
                    at the next column's starting point
    """
    for i in range(4):
        move()
    

# low-level Helper functions
def turn_right():
    for _ in range(3):
        turn_left()

def turn_around():
    turn_left()
    turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()