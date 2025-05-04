from karel.stanfordkarel import *

"""
Karel climbs a mountain of any size and
plants a beeper at the top
"""

def main():
    climb_up_mountain()
    plant_flag()
    climb_down()

def climb_up_mountain():
    # post: karel is at the top of the mountain
    # facing east
    while front_is_blocked():
        step_up()


def plant_flag():
    # pre: karel is on the valid cell (mp wall or pit below)
    # post: a beeper is placed at karel's current position
    put_beeper()

def climb_down():
    # pre: karel is at the top of the mountain, facing east, with stairs to descend
    # post: karels is at the base of the mountain, still facing east
    while front_is_clear():
        step_down

# Helper functions
def step_up():
    # Karel takes one step up the mountain
    # pre: karel is facing the mountain
    # post: karel is facing the mountain one step up
    turn_left()
    move()
    turn_right()
    move()

def step_down():
    # pre: karel is on a step, facing right (East)
    # post: karel is on the next step, facing right
    move()
    turn_right()
    move()
    turn_left()


def turn_right():
    # pre: karel's facing any direction
    # post: karel's turned 90 degrees right from it's original orientation
    for i in range(3):
        turn_left()

if __name__ == '__main__':
    main()