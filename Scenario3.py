# Task:
# Create a solution that accepts an integer input representing the index value for any any of the five elements in the following list:
# various_data_types = [516, 112.49, True, "meow", ("Western", "Governors", "University"), {"apple": 1, "pear": 5}]
# Using the built-in function type() and getting its name by using the .name attribute, output data type (e.g., int”, “float”, “bool”, “str”) based on the input index value of the list element.
# The solution output should be in the format
# Element index_value: data_type
# Sample Input/Output:
# If the input is
# 4
# then the expected output is
# Element 4: tuple

def get_data_type_of_element(index):
    various_data_types = [516, 112.49, True, "meow", ("Western", "Governors", "University"), {"apple": 1, "pear": 5}]

    if 0 <= index < len(various_data_types):
        element_type = type(various_data_types[index]).__name__
        return f"Element {index}: {element_type}"
    else:
        return "Invalid index"

def main():
    # Get user input for the index value
    input_index = int(input("Enter the index value: "))

    # Get the data type of the element at the given index
    result = get_data_type_of_element(input_index)

    # Display the result
    print(result)

if __name__ == "__main__":
    main()
