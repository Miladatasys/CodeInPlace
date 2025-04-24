from karel.stanfordkarel import *

"""
Place 20 beepers, move then 25 and end facing east to the right of the 25 beepers
"""

def main():
    """
    First we set the main variables with their logic 
    and then use them separated for modularity
    """
    place_20_beepers()
    move()
    place_25_beepers()
    move()

def place_20_beepers():
    for i in range(20):
        put_beeper()

def place_25_beepers():
    for i in range(25):
        put_beeper()
    
if __name__ == '__main__':
    main()