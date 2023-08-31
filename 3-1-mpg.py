# Bryce Fish Lab 3-1
#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon program")
print()

exitChar = "y"
while exitChar =="y":

    # get input from the user
    miles_driven = float(input("Enter miles driven:         "))
    gallons_used = float(input("Enter gallons of gas used:  "))
    cost_per_gallon = float(input("Enter cost per gallon:      "))

    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    elif cost_per_gallon <= 0:
        print("Cost per gallon must be greater than zero. Please try again.")
    else:
        # calculations
        mpg = round(miles_driven / gallons_used, 2)
        total_cost = round(cost_per_gallon * gallons_used, 1)
        cost_per_mile = round(total_cost / miles_driven, 1)
        # display results
        print()
        print("Miles Per Gallon:          ", mpg)
        print("Total Gas Cost:            ", total_cost)
        print("Cost Per Mile:             ", cost_per_mile)
        print()
    
    print()
    exitChar = input("Get entries for another trip (y/n)?").lower()
    print()

print()
print("Bye!")



