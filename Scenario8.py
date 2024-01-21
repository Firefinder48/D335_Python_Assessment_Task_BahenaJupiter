# Task:
# Create a solution that accepts an integer input representing water temperature in degrees Fahrenheit. Output a description of the water state based on the following scale:
#    If the temperature is below 33° F, the water is “Frozen”.
#    If the water is between 33° F and 80° F (including 33), the water is “Cold”.
#    If the water is between 80° F and 115° F (including 80), the water is "Warm".
#    If the water is between 115° F and 211° (including 115) F, the water is “Hot".
#    If the water is greater than or equal to 212° F, the water is “Boiling”.
# Additionally, output a safety comment only during the following circumstances:
#    If the water is exactly 212° F, the safety comment is "Caution: Hot!"
#    If the water temperature is less than 33° F, the safety comment is "Watch out for ice!"
# The solution output should be in the format
# water_state
# optional_safety_comment
# Sample Input/Output:
# If the input is
# 118
# then the expected output is
# Hot
# Alternatively, if the input is
# 32
# then the expected output is
# Frozen
# Watch out for ice!

def describe_water_state(temperature):
    if temperature < 33:
        state = "Frozen"
        comment = "Watch out for ice!"
    elif 33 <= temperature < 80:
        state = "Cold"
        comment = ""
    elif 80 <= temperature < 115:
        state = "Warm"
        comment = ""
    elif 115 <= temperature < 212:
        state = "Hot"
        comment = ""
    else:
        state = "Boiling"
        comment = "Caution: Hot!" if temperature == 212 else ""

    output = state
    if comment:
        output += "\n" + comment
    return output

def main():
    # Get user input for the water temperature
    temperature = int(input("Enter the water temperature in degrees Fahrenheit: "))

    # Determine the water state and safety comment
    result = describe_water_state(temperature)

    # Display the result
    print(result)

if __name__ == "__main__":
    main()
