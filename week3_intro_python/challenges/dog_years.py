"""
Asks a user to input an age in human years,
and converts it to the equivalent age in dog years
On average a year is equal to 7.18 dog years.
To convert 3 years to dog years, you multiply 3 * 7.18 to 
get 21.54
"""
# Each year for a human is like 7.18 years for a dog
DOG_YEARS_MULTIPLIER = 7.18  # A constant is written in caps. 

def main():
    """
    This program will take in an age in calendar years, multiply that age by 7.18 
    and report the resulting dog years.
    """
    calendar_year = input("Enter an age in calendar years: ") # input always return a str

    conversion = DOG_YEARS_MULTIPLIER * float(calendar_year)

    print(f"That's {conversion} in dog years! ")

if __name__ == '__main__':
    main()