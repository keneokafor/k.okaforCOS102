# program to calculate the simple interest

principal_amount = float(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the rate of interest (in percentage): "))
time_period = float(input("Enter the time period (in years): "))

simple_interest = principal_amount * (1 + (rate_of_interest / 100) * time_period)

simple_interest_amount = simple_interest - principal_amount
print("Simple interest:", simple_interest_amount)