from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""


def main():
    """
    Get Karel to create a checkerboard pattern of beepers inside an empty rectangular world, 
    As you think about how you will solve the problem, you should make sure that your solution 
    works with checkerboards that are different in size from the standard 6x6 checkerboard shown in the example above. 
    Some examples of such cases are discussed below. Odd-sized checkerboards are tricky, 
    and you should make sure that your program generates the following pattern in a 5x3 world:
    """
    checker_world()


# Mid-level helper functions
def checker_world():
    """
    I want to keep doing these two rows so long as my left is clear. 'Cause that ,eams I have more rows to do.
    If I'm facing East and left is clear, there's a row above me that I should try to look at.
    """
    """
    Here  I only check if left is clear once. Then I moved north. 
    So this is a safe move north because I know my left is clear. 
    """
    # Row 1, 2, ... , n-1
    while left_is_clear(): 
        checker_even_index_row()
        move_north()
        face_east()
        """
        But if I move north again, and I haven't check left is clear, then I'm going to be in trouble. 
        I might run into a wall, THAT'S WHY I CHECK THAT LEFT IS CLEAR BEFORE MOVE NORTH a second time. 
        """
        if left_is_clear(): 
            checker_odd_index_row()
            move_north()
            face_east()
        
    # Last row? Check if beepers present in the row below
    move_south()
    if beepers_present(): # Last row should be an odd index row
        move_north()
        face_east()
        checker_odd_index_row()
    else:
        move_north()
        face_east()
        checker_even_index_row()
        
    go_home()


def checker_even_index_row():
    """
    It's a matter of putting a beeper down. And then
    moving two steps and putting another beeper down.
    """
    put_beeper()
    move_safely()
    while front_is_clear():
        move()
        put_beeper()
        move_safely()
    return_to_opposite_wall()
    face_east()

def return_to_opposite_wall():
    turn_around()
    move_to_wall()

def checker_odd_index_row():
    if front_is_clear():
        move()
        checker_even_index_row()
    



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


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()