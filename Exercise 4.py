def get_tax_bracket(income):
    # Invalid income
    if income < 0:
        return "Invalid income.", 0.0

    # Find bracket based on 2024 single filer brackets
    if income <= 11600:
        bracket = "Low (10%)"
        rate = 0.10
    elif income <= 47150:
        bracket = "Lower Middle (12%)"
        rate = 0.12
    elif income <= 100525:
        bracket = "Middle (22%)"
        rate = 0.22
    elif income <= 191950:
        bracket = "Upper Middle (24%)"
        rate = 0.24
    elif income <= 243725:
        bracket = "Upper (32%)"
        rate = 0.32
    elif income <= 609350:
        bracket = "Very High (35%)"
        rate = 0.35
    else:
        bracket = "Highest (37%)"
        rate = 0.37

    
    
    # Bonus: ternary expression for deduction eligibility
    bracket = bracket + " (Deduction Eligible)" if income % 2 == 0 else bracket

    return bracket, rate


# 
def main():
    income = float(input("Enter employee annual income: "))

    bracket, rate = get_tax_bracket(income)

    if bracket == "Invalid income.":
        print(bracket)
    else:
        estimated_tax = income * rate
        print(f"Your bracket: {bracket}")
        print(f"Estimated tax: ${estimated_tax:,.2f}")


