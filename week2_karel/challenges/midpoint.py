def main():
    """
    This function identifies the midpoint of the first street by 
    strategically placing and removing beepers.
    """
    fill_line_with_beeper() # first line with beepers
    turn_around() # fix the orientation for the first turn
    pick_beeper_advance() # pick beeper at the end the beepers lines 
    
    put_beeper() # put last beeper at midpoint

    # fix the final orientation of karel to face East
    if facing_west():
        turn_around()
    else :
        pass

    

def pick_beeper_advance():
    """this function picks one beeper recursively at the end of the line left 
    or right side until no beeper left
    """
    while beepers_present():
        pick_beeper()
        move()
        while beepers_present() and front_is_clear():
            move()
        turn_around()
        if no_beepers_present():
            move()


def fill_line_with_beeper():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()


def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    for i in range(2):
        turn_left()

if __name__ == '__main__':
    main()