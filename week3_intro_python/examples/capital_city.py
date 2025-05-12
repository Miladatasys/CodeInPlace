from ai import call_gpt
"""
Write a program that will tell the user 
the capital city of a country
"""
def main():
    country = input("Country: ")
    print("Thinking...") # The LLM might takes a few senconds to answer so we print this.
    capital = call_gpt(f"What is the capital city of {country}? ")
    print(capital)

if __name__ == "__main__":
    main()