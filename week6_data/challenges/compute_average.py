def main():
    number_list = load_numbers_from_file("numbers.txt")
    # Intermediate step to get the length of elem in the list
    length_list = (len(number_list))
    # built in function "sum" to get the total and divide
    avg = sum(number_list) / length_list
    print("Average: ", avg)

def load_numbers_from_file(filepath):
    """
    Loads numbers from a file into a list and returns it.
    We assume the file to have one number per line.
    Returns a list of numbers. You should not modify this
    function.
    """
    numbers = []
    with open(filepath, 'r') as file_reader:
        for line in file_reader.readlines():
            cleaned_line = line.strip()
            if cleaned_line != '':
                numbers.append(float(cleaned_line))
    
    return numbers


if __name__ == '__main__':
    main()
