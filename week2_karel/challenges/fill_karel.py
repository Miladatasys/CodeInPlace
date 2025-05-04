from karel.stanfordkarel import *

"""
Your task is simple: no matter the size of the world, Karel should fill it with beepers.
"""


def main():
    """
    Fills the entire world with beepers row by row.
    Karel starts at the bottom-left, facing right, and ends at the top-right, facing right.
    """
    while left_is_clear():
        fill_row()
        turn_right()
    fill_row()
    # Move Karel to top-right
    turn_right()
    while front_is_clear():
        move()

def fill_row():
    """
    Fills the current row with beepers in the current direction.
    Pre:    Karel is at the beginning of a row.
    Post:   Karel is at the end of the row
    """
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()
    move_up_to_next_row()
    if front_is_clear():
        move()
    


def move_up_to_next_row():
    """
    Moves Karel to the start of the next row and turns to it's face to next row
    Pre: Karel is at the end of a filled row
    Post: Karel is at the beginning of the next row, facing right
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