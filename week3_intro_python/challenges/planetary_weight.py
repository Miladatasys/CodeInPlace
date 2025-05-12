"""
Prompts the user for a weight on Earth
and a planet (in separate inputs). Then 
prints the equivalent weight on that planet.

Note that the user should type in a planet with 
the first letter as uppercase, and you do not need
to handle the case where a user types in something 
other than one of the planets (that is not Earth). 
"""
# Planets gravitational constants relative to earth
MERCURY_GRAVITY = 0.376
VENUS_GRAVITY   = 0.889
MARS_GRAVITY    = 0.378
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY  = 1.081
URANUS_GRAVITY  = 0.815
NEPTUNE_GRAVITY = 1.14

def main():
    """
    Precondition:   User inputs a valid num value for weight  
                    and inputs a valid planet name (starting with uppercase letter)
    Postcondition:  Displays the weight on the selected planet, rounded by two decimals
    """
    earth_weight = float(input("Enter a weight on Earth: "))
    planet = input("Enter a planet: ")

    # Determine the gravitational constant based on the selected planet
    if planet == 'Mercury':
        gravity_constant = MERCURY_GRAVITY
    elif planet == 'Venus':
        gravity_constant = VENUS_GRAVITY
    elif planet == 'Mars':
        gravity_constant = MARS_GRAVITY
    elif planet == 'Jupiter':
        gravity_constant = JUPITER_GRAVITY
    elif planet == 'Saturn':
        gravity_constant = SATURN_GRAVITY
    elif planet == 'Uranus':
        gravity_constant = URANUS_GRAVITY
    else:
        # Can assume user types in one of these planets, so this can be an else instead of elif
        gravity_constant = NEPTUNE_GRAVITY

    # Compute the equivalent weight on the selected planet
    planetary_weight = earth_weight * gravity_constant
    rounded_planetary_weight = round(planetary_weight, 2)

    # Output the result to the user
    print(f"The equivalent weight on {planet}: {rounded_planetary_weight} ")

if __name__ == "__main__":
    main()