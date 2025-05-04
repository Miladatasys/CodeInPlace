from karel.stanfordkarel import *

"""
Each row starts with a stack of beepers. Karel should pick them
up, one at a time, and spread them down the row. 
Caution! Karel can't count, and starts with infinite beepers in
her bag. How can you solve this puzzle?
steps:
1. move
2. spread_beeper
3. get_back_to_beeper
4. go_first_column
"""

def main():
    
    spreadbeeper()
    go_to_first()


def spreadbeeper():
    move()
    while beepers_present():
        pick_beeper()
        if beepers_present():
            go_forward()          
            put_beeper()
            restart()
    put_beeper()


def turn_back():
    turn_left()
    turn_left()

def go_to_first():
    turn_back()
    while front_is_clear():
        move()
    turn_back()

def restart():
    turn_back()
    while front_is_clear():
        move()
    turn_back()
    move()

def go_forward():
    while beepers_present():
        move()


if __name__ == '__main__':
    main()
