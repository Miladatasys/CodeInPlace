def main():
    go_to_beeper() # uses handled_corner() helper
    return_home()  # uses turn_around() and turn_right() utilities

def go_to_beeper():
    for i in range(3):
        if front_is_clear(): 
            move()
        else:
            handle_corner()
            pick_beeper()

def return_home():
    turn_around()
    move()
    turn_right()
    move()
    turn_left()
    for i in range(3):
        if front_is_clear():
            move()
    turn_around()

# Helper function to handle corner logic
def handle_corner():
    turn_right()
    move()
    turn_left()
    move()

# Utility functions to turn right using left turns
def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    for i in range(2):
        turn_left()

