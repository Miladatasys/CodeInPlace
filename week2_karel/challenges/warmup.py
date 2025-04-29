def main():
    turn_left()
    move()
    turn_right()
    move()

def turn_right():
    for _ in range(3):
        turn_left()

if __name__ == '__main__':
    main()