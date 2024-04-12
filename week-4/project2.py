# program to calculate the annual tax revenue based on age and years of experience

# taking inputs from the user
age = int(input("Enter your age: "))
years_of_experience = int(input("Enter the number of years of experience: "))

if years_of_experience > 25 and age >=  55:
    print("Annual Tax Revenue = 5,600,00")

elif years_of_experience > 20 and age >= 45:
    print("Annual Tax Revenue = 4,480,000")

elif years_of_experience > 10 and age >= 35:
    print("Annual Tax Revenue = 1,500,000")

else:
    print("Annual Tax Revenue = 550,000")