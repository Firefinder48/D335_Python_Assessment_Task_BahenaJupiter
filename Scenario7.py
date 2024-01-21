# Task:
# Create a solution that accepts an integer input to compare against the following list:
# predef_list = [4, -27, 15, 33, -10]
# Output a Boolean value indicating whether the input value is greater than the maximum value from predef_list
# The solution output should be in the format
# Greater Than Max? Boolean_value
# Sample Input/Output:
# If the input is
# 20
# then the expected output is
# Greater Than Max? False

def is_greater_than_max(input_value, predef_list):
    max_value = max(predef_list)
    return input_value > max_value

def main():
    # Predefined list
    predef_list = [4, -27, 15, 33, -10]

    # Get user input for the integer to compare
    input_value = int(input("Enter an integer to compare: "))

    # Check if the input is greater than the maximum value in the list
    result = is_greater_than_max(input_value, predef_list)

    # Display the result
    print(f"Greater Than Max? {result}")

if __name__ == "__main__":
    main()
