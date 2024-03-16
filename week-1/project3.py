# program to calculate the annuity plan

principal_amount = float(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the rate of interest (in percentage): "))
time_period = float(input("Enter the time period (in years): "))
compounding_frequency = int(input("Enter the compounding frequency per year: "))
m_unknown = float(input("Enter the value of m:" ))

amount = principal_amount * m_unknown * time_period * ((1 + rate_of_interest / compounding_frequency) ** (compounding_frequency * time_period) - 1) / (rate_of_interest / compounding_frequency)
interest = amount - principal_amount

print("Annuity Plan:", interest)