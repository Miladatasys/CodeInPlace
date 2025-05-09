"""
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.
Apply a formula using a multiplier: weight x 0.378
"""

# Constant
MARS_GRAVITY = 0.378
# weight: 147.2

def main():
    # Get input from user and convert to float
    earth_weight = float(input("Enter a weight on Earth: "))
    
    # Calculate Mars weight
    mars_weight = earth_weight * MARS_GRAVITY
    
    # Print the full calculation result
    print(f"The equivalent weight on Mars: {mars_weight}")

if __name__ == "__main__":
    main()