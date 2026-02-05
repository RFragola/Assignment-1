# Prompt for credit score
def main():
    score = int(input("Enter your credit score: "))
    if score < 300 or score > 850:
        print("Invalid score.")
    elif score >= 750 and score <= 850:
        print ("Excellent - Loan Approved")
        print ("Interest rate: Low")
    elif score >= 700:
        print ("Good - Loan Approved with Review")
        print ("Interest rate: Low")
    elif score >= 600:
        print ("Fair - Loan Conditional")
        print ("Seek credit improvement")
    elif 300 <= score < 600:
        print ("Poor - Loan Denied")
        print ("Seek credit improvement")
    else:
        print ("Invalid Score")

main()