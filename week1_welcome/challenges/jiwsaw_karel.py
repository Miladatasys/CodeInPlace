def main():
    go_to_beeper()
    place_beeper()
    return_place()

# Go pick up the puzzle piece
def go_to_beeper():
    move()
    move()
    pick_beeper()

# Go to place the beeper
def place_beeper():
    move()
    turn_left()
    move()
    move()
    put_beeper()

# Return to origin
def return_place():
    turn_around()
    move()
    move()
    turn_right()
    move()
    move()
    move()
    turn_around()

# utility functions
def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    for i in range(2):
        turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()