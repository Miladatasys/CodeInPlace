from karel.stanfordkarel import *

"""
Each row starts with a stack of beepers. Karel should pick them
up, one at a time, and spread them down the row. 
Caution! Karel can't count, and starts with infinite beepers in
her bag. How can you solve this puzzle?
"""

def main():
    """
    Karel starts at (1,1) facing east
    steps:
        -   Move to supplies 
        -   Pick one beeper
        -   Place that beeper on the next cell
        -   Turn around and get back to the supplies pile
        -   Once all beepers are spread, get back to (1,1)
    """
    move()
    while beepers_present():
        pick_beeper()
        if beepers_present():            
            spread_supplies()
            go_back_to_supplies()
    final_turn()


def spread_supplies():
    """
    Precondition:   Karel's at (1,2) and took a beeper from the supplies
    Postcondition:  Karel put a beeper in an empty cell located after the spreaded beepers
    """
    while beepers_present():
        move()
    put_beeper()
    
def final_turn():
    """
    Precondition:   Last beeper in (1,2)
    Postcondition:  Karel go back to (1,1)
    """
    put_beeper()
    turn_around()
    move()
    turn_around()


def go_back_to_supplies():
    """
    Precondition:   Placed a beeper in the cell
    Postcondition:  Positioned back to (1,1)
    """
    turn_around()
    while front_is_clear():
        move()
    turn_around()
    move()


# Low-level helper functions
def turn_around():
    turn_left()
    turn_left()

def turn_right():
    for _ in range(3):
        turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()