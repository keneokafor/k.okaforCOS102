# program to calculate the compound interest

principal_amount = float(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the rate of interest (in percentage): "))
time_period = float(input("Enter the time period (in years): "))
compounding_frequency = int(input("Enter the compounding frequency per year: "))
 
amount = principal_amount * (1 + rate_of_interest / compounding_frequency) ** (compounding_frequency * time_period)
interest = amount - principal_amount

print("Compound interest:", interest)