from karel.stanfordkarel import *

# Karel builds missing beeper columns in a temple


def main():
    """
    -   Karel starts at bottom left corner, facing East
    -   The columns are exactly four squares apart, on the 1st, 5th, 9th and 13th columns
    -   Karel can assume that columns are always five units high
    """
    while front_is_clear():
        build_column()
    build_column()

# Mid - level helper functions
def build_column():
    """
    Builds a single column of beepers and moves to the next column
    pre:    Karel is at the base of the colum, facing East on the 1st row
    post:   Karel is back on the 1st row, 4 steps east of the original position
            A full column (5 beepers) has been placed vertically
    """
    turn_left()
    for i in range(4):
        put_beeper()
        move()
    put_beeper()
    turn_around()
    for i in range(4):
        move()
    turn_left()
    for i in range(4):
        if front_is_clear():
            move()


def move_to_next_arch():
    """
    Moves Karel from the top of one column  to the base of the next column
    pre: Karel is at the top of a column, facing north
    post: Karel is at the base of the next column, facing north
    """
    turn_right()
    for i in range(4):
        move()

def descend_column():
    """
    Turns Karel 180 degrees to begin descending the column.
    pre:  Karel is at the top of a column, facing North.
    post: Karel is at the same spot, facing South, ready to descend.
    """
    turn_around()


# Low-level helper functions
def turn_around():
    """
    Turns Karel 180 degrees in place
    pre: Karel is facing any direction
    post: Karel is facing the opposite direction
    """
    # Turns 180°
    turn_left()
    turn_left()

def turn_right():
    # Turns 90°
    for i in range(3):
        turn_left()

if __name__ == '__main__':
    main()