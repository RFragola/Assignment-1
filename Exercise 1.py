# Prompt user for revenue and cost
def main():
    revenue = float(input("Enter your company's revenue: "))
    cost = float(input("Enter your company's cost: "))
    profit = revenue - cost  # Calculate profit
    margin = profit/revenue  # Calculate margin
    if revenue == 0:
        print("Invalid Revenue") # Guard against DIV/0 error
    else:
        print(f"Profit: ${profit:.2f}") # Print profit in $
        print(f"Margin: {margin:.2%}")  # Print margin as %


main()