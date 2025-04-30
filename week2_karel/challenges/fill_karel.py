from karel.stanfordkarel import *

"""
Your task is simple: no matter the size of the world, Karel should fill it with beepers.
"""


def main():
    """
    Fills the entire world with beepers row by row.
    Karel starts at the bottom-left, facing right, and ends at the top-right, facing right.
    fill_row()
    """

def fill_row():
    """
    Fills the current row with beepers in the current direction
    Pre: Karel is at the beginning of a row
    Post: Karel is at the end of the row, same row, same direction
    """
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()
    move_up_to_next_row()

def move_up_to_next_row():
    """
    Moves Karel up one row and flips direction to prepare for next row
    Pre: Karel's at the end of a filled row
    Post: Karel is at the start of the row, ready to fill
    """
    turn_around()
    while front_is_clear():
        move()
    turn_around()
    turn_left()
    

def turn_right():
    for _ in range(3):
        turn_left()

def turn_around():
    turn_left()
    turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()