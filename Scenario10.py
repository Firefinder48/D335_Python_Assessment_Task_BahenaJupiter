# Task:
# Create a solution that accepts an integer input identifying how many shares of stock are to be purchased from the Old Town Stock Exchange, followed by an equivalent number of string inputs representing the stock selections. The following dictionary stock lists available stock selections as the key with the cost per selection as the value.
# stocks = {'TSLA': 912.86 , 'BBBY': 24.84, 'AAPL': 174.26, 'SOFI': 6.92, 'KIRK': 8.72, 'AURA': 22.12, 'AMZN': 141.28, 'EMBK': 12.29, 'LVLU': 2.33}
# Output the total cost of the purchased shares of stock to two decimal places.
# The solution output should be in the format
# Total price: $cost_of_stocks
# Sample Input/Output:
# If the input is
# 3
# SOFI
# AMZN
# LVLU
# then the expected output is
# Total price: $150.53

def calculate_total_stock_price(shares, stock_selections, stocks):
    total_price = 0.0
    for selection in stock_selections:
        if selection in stocks:
            total_price += stocks[selection]
    return round(total_price, 2)

def main():
    # Predefined list of stocks
    stocks = {'TSLA': 912.86, 'BBBY': 24.84, 'AAPL': 174.26, 'SOFI': 6.92, 'KIRK': 8.72, 'AURA': 22.12, 'AMZN': 141.28, 'EMBK': 12.29, 'LVLU': 2.33}

    # Get user input for the number of shares to be purchased
    shares = int(input("Enter the number of shares to be purchased: "))

    # Get user input for the stock selections
    stock_selections = []
    for _ in range(shares):
        stock_selection = input("Enter the stock selection: ").upper()
        stock_selections.append(stock_selection)

    # Calculate the total cost of the purchased shares of stock
    total_price = calculate_total_stock_price(shares, stock_selections, stocks)

    # Display the total price
    print(f"Total price: ${total_price}")

if __name__ == "__main__":
    main()

