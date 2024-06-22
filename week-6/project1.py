# program to calcilate the price based on the weight of the package and the location of the customer

# taking customer inputs
print("Welcome to Simi Services.")
weight = int(input("Enter the weight of your package in kg: "))
location =str(input("Enter your location: "))

# calculating the price based on location and weight
if weight >= 10 and location =="Ibeju-Lekki":
    print("Your price = N10,000")

elif weight < 10 and location == "Ibeju-Lekki":
    print("Your price = N3,500")

elif weight >= 10 and location == "Epe":
    print("Your price = N10,000")

elif weight < 10 and location == "Epe":
    print("Your price = N5,000")