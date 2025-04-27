"""
This problem tests your understanding of the fencepost problem from lecture
"""

def main():
    """
    Fills entire bottom row of any sized world with beepers.
    """
    place_beepers()

def place_beepers():
    """ 
    We don't know how large the world is, 
    so we can use a while-loop to move until we reach the last column
    """
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()

if __name__ == '__main__':
    main()