from karel.stanfordkarel import *

# this program executes in a special function called main
def main():
    move()
    for i in range(5):
        put_beeper()
    move()

# This is "boilerplate" code which launches your code
# when you hit the run button
if __name__ == '__main__':
    main()


from karel.stanfordkarel import *


def main():
    for i in range(4):
        move()
        put_beeper()
        turn_left()

if __name__ == '__main__':
    main()


from karel.stanfordkarel import *

def main():
    """
    Places 10 beepers in the spot that Karel is standing.
    """
    for i in range(10):
        put_beeper()

if __name__ == '__main__':
    main()
