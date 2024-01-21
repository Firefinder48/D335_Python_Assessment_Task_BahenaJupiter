# Task:
# Create a solution that accepts any three integer inputs representing the base (b1, b2) and height (h) measurements of a trapezoid in meters. Output the exact area of the trapezoid in square meters as a float value. The exact area of a trapezoid can be calculated by finding the average of the two base measurements, then multiplying by the height measurement.
# Trapezoid Area Formula:
# A = [(b1 + b2) / 2] * h
# The solution output should be in the format
# Trapezoid area: area_value square meters
# Sample Input/Output:
# If the input is
# 3
# 4
# 5
# then the expected output is
# Trapezoid area: 17.5 square meters
# Alternatively, if the input is
# 3
# 5
# 7
# then the expected output is
# Trapezoid area: 28.0 square meters

def calculate_trapezoid_area(b1, b2, h):
    area = ((b1 + b2) / 2) * h
    return area

def main():
    # Get user input for the base and height measurements
    b1 = int(input("Enter the length of the first base (b1) in meters: "))
    b2 = int(input("Enter the length of the second base (b2) in meters: "))
    h = int(input("Enter the height (h) of the trapezoid in meters: "))

    # Calculate the area of the trapezoid
    trapezoid_area = calculate_trapezoid_area(b1, b2, h)

    # Display the result
    print(f"Trapezoid area: {trapezoid_area} square meters")

if __name__ == "__main__":
    main()
