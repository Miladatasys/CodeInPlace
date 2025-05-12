"""
This prompts the user for a temperature in Fahrenheit 
(this can be a number with decimal places) and outputs 
the temperature converted to celsius. 
"""

def main():
    # Get the fahrenheit temperature from the user
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))

    # Use the formula to calculate temperature in Celsius
    celsius = (fahrenheit - 32) * 5.0/9.0

    # Output with appropriate units
    print("Temperature: " + str(fahrenheit) + "F = " + str(celsius) + "C")

if __name__ == '__main__':
    main()