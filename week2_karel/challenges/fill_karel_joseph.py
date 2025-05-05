from karel.stanfordkarel import *

"""
Your task is simple: no matter the size of the world, Karel should fill it with beepers.
"""


def main():
    """
    Fills the entire world with beepers row by row.
    Karel starts at the bottom-left, facing right, and ends at the top-right, facing right.
    """
    fill_world()


def fill_world():
    fill_row()
    face_east()
    while left_is_clear():
        move_north()
        face_east()
        fill_row()
    move_to_wall()

# Mid-level helper functions
def fill_row():
    put_beepers_until_wall()
    return__to_opposite_wall()
    face_east()

def put_beepers_until_wall():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()

def return__to_opposite_wall():
    turn_around()
    move_to_wall()
 

# Utility functions

# Safety first!
def move_safely():
    if front_is_clear():
        move()

def put_beeper_safely():
    if no_beepers_present():
        put_beeper()

def pick_beeper_safely():
    if beepers_present():
        pick_beeper() 

# Main character motion
def turn_around():
    turn_left()
    turn_left()

def turn_right():
    for _ in range(3):
        turn_left()

# Let's get reoriented
def face_north():
    while not_facing_north():
        turn_left()
"""
Now, to this problem let's define a function 
when we're already facing north and need to move
"""
def move_north():
    face_north()
    move_safely()

def face_south():
    while not_facing_south():
        turn_left()

def face_east():
    while not_facing_east():
        turn_left()

def face_west():
    while not_facing_west():
        turn_left()

# There's no place like home
def move_to_wall():
    while front_is_clear():
        move()

def go_home():
    """Karel returns to the SW corner, facing East."""
    face_west()
    move_to_wall()
    turn_left()
    move_to_wall()
    turn_left()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()