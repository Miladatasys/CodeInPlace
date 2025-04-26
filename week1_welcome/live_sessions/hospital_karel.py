from karel.stanfordkarel import *
"""
Karel starts at the left (west) end of a row with beepers representing supply piles.
Karel's job is to build hospitals at these locations. A hospital is built by placing
beepers in a vertical line, starting from the supply pile. Karel should not run
into a wall.
"""
def main():
    # Main flow
    go_to_first_supply_pile()
    build_left_wall()
    build_right_wall()
    move_to_next_hospital()

def go_to_first_supply_pile():
    # Start program by moving until finding beeper
    while no_beepers_present():
        move()

def build_left_wall():
    """
    Builds the left vertical wall of the hospital.
    Karel start facing north after moving to supply pile
    """
    turn_left()
    move_and_put_beeper()
    move_and_put_beeper()
    turn_around()
    return_to_row()

def build_right_wall():
    """
    Builds the right wall of the hospital
    and get ready to move on to the next one.
    """
    turn_left()
    move()
    turn_left()
    put_column()
    turn_around()
    return_to_row()
    turn_left()

def move_to_next_hospital():
    """
    Repeat the building process one last time 
    and ends at the same position.
    """
    while front_is_clear():
        move()
        if beepers_present():
            build_left_wall()
            build_right_wall()

# Helper functions
def move_and_put_beeper():
    move()
    put_beeper()

def put_column():
    put_beeper()
    for i in range(2):
        move_and_put_beeper()
    
def return_to_row():
    while front_is_clear():
        move()

def turn_around():
    turn_left()
    turn_left()
    
def turn_right():
    for i in range(3):
        turn_left()    
    
if __name__ == '__main__':
    main()