loan_amnt=int(input("Enter the loan amount (in Rs) : "))
duration=int(input("Enter the duration (in years) : "))
rate=int(input("Enter the rate (in %) : "))

interest_amount=int(loan_amnt*duration*rate*0.01)

print("Interest Payable is Rs : ",interest_amount)