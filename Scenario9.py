# Task:
# Create a solution that accepts one integer input representing the index value for any of the string elements in the following list:
# frameworks = ["Django", "Flask", "CherryPy", "Bottle", "Web2Py", "TurboGears"]
# Output the string element of the index value entered. The solution should be placed in a try block and implement an exception of "Error" if an incompatible integer input is provided.
# The solution output should be in the format
# frameworks_element
# Sample Input/Output:
# If the integer input is
# 2
# then the expected output is
# CherryPy
# Alternatively, if the integer input is
# 7
# then the expected output is
# Error

def get_framework_by_index(index, frameworks):
    try:
        return frameworks[index]
    except IndexError:
        return "Error"

def main():
    # Predefined list of frameworks
    frameworks = ["Django", "Flask", "CherryPy", "Bottle", "Web2Py", "TurboGears"]

    # Get user input for the index value
    index = int(input("Enter the index value for a framework: "))

    # Retrieve the framework element or handle the error
    result = get_framework_by_index(index, frameworks)

    # Display the result
    print(result)

if __name__ == "__main__":
    main()
