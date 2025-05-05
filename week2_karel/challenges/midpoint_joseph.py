from karel.stanfordkarel import *

"""
Find  the midpoint of 1st Street
The final state of the world should have
only a single beeper at the midpoint of the first row

Karel is allowed to place additional beepers
wherever it wants to, but must pick them all up again before it finishes.
Similarly, if Karel paints any of the corners in the world
they must all be uncolored before Karel finishes.
"""

def main():
    """
    Main idea: Make a row line of beepers and
    pull beepers off each end until we reach the midpoint
    """
    row_midpoint()

def row_midpoint():
    fill_row()
    pick_beeper_from_opposite_wall()
    pick_beeper_from_opposite_wall()    
    move_safely()

    while beepers_present():
        pick_beeper_from_opposite_end()
    
    # Mark midpoint with a beeper
    turn_around()
    move_safely()
    put_beeper()
    face_east()

def fill_row():
    put_beepers_until_wall()
    return_to_opposite_wall()
    face_east()

def pick_beeper_from_opposite_wall():
    move_to_wall()
    pick_beeper()
    turn_around()

def pick_beeper_from_opposite_end():
    """
    There is an empty space next to the beeper that we want to pick up
    """
    while beepers_present():
        move()
    
    # We've overshot! the beeper is behind us, maybe.
    turn_around()
    move_safely()
    pick_beeper_safely() # Because there might not be a beeper there!

    move_safely() # Move onto a beeper, maybe

def put_beepers_until_wall():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()

def return_to_opposite_wall():
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

# We're defining move south
def move_south():
    face_south()
    move()

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


if __name__ == '__main__':
    main()