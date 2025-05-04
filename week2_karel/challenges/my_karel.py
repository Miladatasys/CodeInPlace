from karel.stanfordkarel import *

def main():
    
    hair()
    neck()
    shoulders()
    arms()
    torso()
    legs()
    eyes()
    face()


# Mid-level helper functions

def hair():

    while front_is_clear():
        paint_hair()
        move()
    paint_hair()
    if front_is_blocked():
        descend()
        move()
    turn_left()
    move()
    paint_hair()
    turn_around()
    while front_is_clear():
        paint_hair()
        move()
        paint_hair()
    turn_around()
    descend()
    move()
    paint_hair()
    turn_around()
    turn_right()
    turn_around()
    move()
    paint_hair()
    turn_around()
    while front_is_clear():
        paint_hair()
        move()
    paint_hair()
    while front_is_clear():
        paint_hair()
        move()
    paint_hair()
    if front_is_blocked():
        descend()
        move()
        turn_right()
    while front_is_clear():
        paint_hair()
        move()
    paint_hair()
    turn_left()
    while front_is_clear():
        paint_hair()
        move()
    paint_hair()
    turn_left()
    while front_is_clear():
        move()
    paint_hair()
    turn_left()
    move()
    turn_around()
    turn_left()
    move()
    paint_hair()
    turn_left()
    for i in range(2):
        move()
        paint_hair()
    turn_left()
    move()
    paint_hair()
    move()
    paint_hair()
    turn_left()
    for i in range(2):
        move()
        paint_hair()
    move()
    move()
    paint_hair()
    turn_around()
    turn_left()
    while front_is_clear():
        move()
    paint_hair()

def neck():
    turn_around()
    move()
    descend()
    move()
    turn_left()
    while front_is_clear():
        paint_neck()
        move()
    paint_neck()
    
def shoulders():
    descend()
    move()
    turn_left()
    move()
    paint_shoulders()
    turn_around()
    for i in range(9):
        move()
        paint_shoulders()
    paint_corner("black")
    turn_around()
    for i in range(9):
        move()
    paint_corner("black")

def arms():
    turn_right()
    turn_left()
    descend()
    move()
    for i in range(2):
        paint_arms()
        move()
    paint_hands()
    move()
    paint_corner("black")
    turn_around()
    move()
    turn_right()
    move()
    turn_left()
    for i in range(2):
        paint_corner("black")
        move()
    paint_corner("black")
    turn_left()
    move()
    move()
    while front_is_clear():
        paint_arms()
        move()
    paint_corner("black")
    turn_left()
    paint_corner("black")
    move()
    paint_corner("black")    
    move()
    paint_corner("black")
    turn_left()
    move()
    paint_hands()
    turn_right()
    move()
    paint_corner("black")
    turn_around()
    move()
    move()
    paint_arms()
    move()
    descend()
    move()
    turn_right()
    paint_corner("black")
    for i in range(3):
        paint_corner("black")
        move()
    turn_left()
    paint_corner("black")
    for i in range(7):
        move()
    turn_left()
    paint_corner("black")
    for i in range(3):
        move()
        paint_corner("black")    

def torso():
    turn_around()
    move()
    turn_right()
    move()
    paint_torso()
    move()
    paint_tool()
    turn_left()
    move()
    paint_tool()
    turn_left()
    move()
    paint_torso()
    turn_around()
    move()
    move()
    for i in range(4):
        paint_torso()
        move()
    turn_right()
    move()
    turn_right()
    for i in range(4):
        move()
        paint_torso()
    for i in range(3):
        move()
    turn_around()
    turn_left()
    for i in range(2):
        move()
    turn_around()
    turn_left()
    for i in range(6):
        paint_torso()
        move()
        paint_torso()

def legs():
    move()
    turn_left()
    move()
    for i in range(2):
        paint_legs()
        move()
    paint_legs()
    turn_left()
    for i in range(2):
        paint_legs()
        move()
    paint_legs()
    turn_around()
    move()
    turn_right()
    for i in range(2):
        paint_legs()
        move()    
    paint_legs()
    turn_right()
    for i in range(6):
        paint_legs()
        move()        
    paint_legs()
    turn_around()
    turn_left()
    move()
    paint_legs()
    turn_around()
    turn_left()
    for i in range(5):
        paint_legs()
        move()          
    paint_legs()
    turn_around()
    for i in range(5):
        move()   
    turn_around()
    turn_left()
    move()
    paint_legs()
    turn_around()
    turn_left()
    move()
    paint_legs()
    move() 
    turn_left()   
    paint_legs()

def eyes():
    turn_around()
    for i in range(12):
        move()
    turn_left()
    move()
    paint_eyes()
    move()
    move()
    move()
    paint_eyes()

def face():
    for _ in range(2):
        move()
    turn_around()
    turn_left()
    move()
    turn_right()
    for i in range(8):
        paint_face()
        move()
    paint_face()
    turn_around()
    turn_left()
    for i in range(4):
        paint_face()
        move()    
    paint_face()
    turn_around()
    turn_left()
    for i in range(7):
        paint_face()
        move()    
    paint_face()
    turn_right()
    move()
    for i in range(3):
        paint_face()
        move()       
    turn_around()
    turn_right()
    move()
    turn_left()
    for i in range(3):
        paint_face()
        move()       
    paint_face()
    turn_left()
    for i in range(9):
        paint_face()
        move()    
    paint_face()
    turn_left()
    move()
    turn_right()
    move()
    turn_left()
    for i in range(2):
        paint_face()
        move()    
    turn_around()
    move()
    turn_around()
    turn_left()
    for i in range(2):
        move()        
    for i in range(2):
        paint_face()
        move()    
    paint_face()
    move()
    move()
    for i in range(2):
        paint_face()
        move()       
    turn_left()
    move()
    turn_left()
    paint_face()
    for i in range(5):
        paint_face()
        move()      
    paint_face()     

# Low-level helper functions
def turn_around():
    turn_left()
    turn_left()
    

def turn_right():
    for i in range(3):
        turn_left()

def descend():
    turn_around()
    turn_left()

# Color helpers
"""
Hair
"""
def paint_hair():
    paint_corner("black")

def paint_neck():
    paint_corner("black")

def paint_shoulders():
    paint_corner("royalblue")

def paint_arms():
    paint_corner("royalblue")

def paint_hands():
    paint_corner("khaki")

def paint_torso():
    paint_corner("royalblue")

def paint_legs():
    paint_corner("black")

def paint_eyes():
    paint_corner("saddlebrown")    

def paint_tool():
    paint_corner("gold")

def paint_face():
    paint_corner("khaki") 

if __name__ == '__main__':
    main()