def main():
    pick_10_beepers()

def pick_10_beepers():
    for i in range(10):
        while beepers_present():
            pick_beeper()
        if front_is_clear():
            move()

if __name__ == '__main':
    main()