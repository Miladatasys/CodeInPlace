def main():
    user_height = input("Enter your height in meters: ")
    height = float(user_height)

    if height > 1.6 and height < 1.9:
        print("Correct height to be an astronaut")
    elif height <= 1.6:
        print("Below minimum astronaut height")
    else:
        print("Above maximum astronaut height")

if __name__ == "__main__":
    main()
