# Prompt user for revenue and cost
def main():
    revenue = float(input("Enter your company's revenue: "))
    cost = float(input("Enter your company's cost: "))
    profit = revenue - cost
    margin = profit/revenue 
    if revenue == 0:
        print("Invalid Revenue")
    else:
        print(f"Profit: ${profit:.2f}")
        print(f"Margin: {margin:.2%}")


main()