"""
Karel will be in a single row world with beepers in some positions.
Karel should invert the pattern of the row
"""
def main():
    invert_corner():
    while front_is_clear():
        move()
        invert_corner()



def invert_corner():
    if beepers_present():
        pick_beeper()
    else:
        put_beeper()

if __name__ == '__main':
    main()