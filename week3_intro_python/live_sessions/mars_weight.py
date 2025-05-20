"""
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.
Apply a formula using a mitplier: weight x 0.378
"""
# Constant for Mars gravity relative to Earth gravity
MARS_GRAVITY = 0.378

def main():
    """
    Precondition: User inputs a valid numeric value representing their Earth weight.
    Postcondition: Print the equivalent Mars weight rounded and float type to two decimal places.
    """
    earth_weight = float(input("Enter a weight on Earth: "))

    """
    Precondition: `earth_weight` is a positive float.
    Postcondition: `mars_weight` is a float with Mars equivalent weight.
    """
    mars_weight = earth_weight * MARS_GRAVITY

    # Round the result to two decimal places for cleaner output
    rounded_mars_weight = round(mars_weight, 2)

    # Display the result to the user. 
    print(f"The equivalent weight on Mars: {rounded_mars_weight}")
    
if __name__ == "__main__":
    main()