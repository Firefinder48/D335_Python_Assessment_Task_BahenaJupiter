# Task:
# Create a solution that accepts an integer input representing any number of ounces. Output the converted total number of tons, pounds, and remaining ounces based on the input ounces value. There are 16 ounces in a pound and 2,000 pounds in a ton.
# The solution output should be in the format
# Tons: value_1
# Pounds: value_2
# Ounces: value_3
# Sample Input/Output:
# If the input is
# 32035
# then the expected output is
# Tons: 1
# Pounds: 2
# Ounces: 3

def convert_ounces_to_tons_pounds_ounces(ounces):
    ounces_per_pound = 16
    pounds_per_ton = 2000

    total_pounds = ounces // ounces_per_pound
    tons = total_pounds // pounds_per_ton
    remaining_pounds = total_pounds % pounds_per_ton
    remaining_ounces = ounces % ounces_per_pound

    return tons, remaining_pounds, remaining_ounces

def main():
    # Get user input for the number of ounces
    input_ounces = int(input("Enter the number of ounces: "))

    # Convert the ounces to tons, pounds, and remaining ounces
    tons, pounds, remaining_ounces = convert_ounces_to_tons_pounds_ounces(input_ounces)

    # Display the result
    print(f"Tons: {tons}\nPounds: {pounds}\nOunces: {remaining_ounces}")

if __name__ == "__main__":
    main()
