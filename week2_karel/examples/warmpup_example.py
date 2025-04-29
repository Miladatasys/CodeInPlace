from karel.stanfordkarel import *

"""
A warmup example. Makes karel place a diagonal
beeper line. Recall how while loops work, and
practice stepping up! We are going to use a 
similar sequence of commands a few times today.
"""
def main():
    # keep stepping up until the top
    while front_is_clear():
        # Assume: Karel is facing right (east)
        put_beeper()
        turn_left()
        move()
        turn_right()
        move()
    put_beeper()

# Helper functions
def turn_right():
    for i in range(3):
        turn_left()

# This is "boilerplate" code which launches your code
# when you hit the run button
if __name__ == '__main__':
    main()