"""
Places exactly 10 beepers on the current tile.
"""
from karel.stanfordkarel import *

def main():
    """
    Places 10 beepers in each square of the bottom row.
    Karel ends at the far right.    
    """
    while front_is_clear():
        place_10_beepers()
        move()
    place_10_beepers()

def place_10_beepers():
    """Places exactly 10 beepers on the current tile."""
    for i in range(10):
        put_beeper()

if __name__ == '__main__':
    main()