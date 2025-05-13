"""
This program asks the user for their age
and let's them know if they can or can't vote
"""
# Constants of fictional countries
PETURKSBOUIPO_AGE = 16
STANLAU_AGE = 25
MAYENGUA_AGE = 48

def main():
    # Asks user their age and convert it to integer
    age = int(input("How old are you? "))

    # Validate if they can vote in PETURKSBOUIPO
    if age >= PETURKSBOUIPO_AGE:
        print("You can vote in Peturksbouipo where the voting age is " + str(PETURKSBOUIPO_AGE) + ".")
    else:
        print("You cannot vote in Peturksbouipo where the voting age is " + str(PETURKSBOUIPO_AGE) + ".")
    
    # Validate if they can vote in STANLAU
    if age >= STANLAU_AGE:
        print("You can vote in Stanlau where the voting age is " + str(STANLAU_AGE) + ".")
    else:
        print("You cannot vote in Stanlau where the voting age is " + str(STANLAU_AGE) + ".")

    # Validate if they can vote in MAYENGUA
    if age >= MAYENGUA_AGE:
        print("You can vote in Mayengua where the voting age is " + str(MAYENGUA_AGE) + ".")
    else:
        print("You cannot vote in Mayengua where the voting age is " + str(MAYENGUA_AGE) + ".")


if __name__ == '__main__':
    main()