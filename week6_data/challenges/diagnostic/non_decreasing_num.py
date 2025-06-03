def main():
    # Intro message and user input
    print("Enter a sequence of non-decreasing numbers.")
    first_input = input("Enter num: ")
    current_num = float(first_input)

    # Counter
    count = 1

    while True:
        next_input = input("Enter num: ")
        next_num = float(next_input)

        if next_num >= current_num:
            count += 1
            current_num = next_num
        else:
            print("Thanks for playing!")
            print("Sequence length:", count)
            break

if __name__ == "__main__":
    main()
