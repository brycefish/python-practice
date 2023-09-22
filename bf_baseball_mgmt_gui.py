#!/usr/bin/env python3
# Bryce Fish
# Project 1
# Server-Side Programming

# display a welcome message
print("================================================================")
print("\t\tBaseball Team Manager\n")
print("This program calculates the batting average for a player based \n on the player\'s official number of at bats and hits.")
print()
print("1 – Calculate batting average")
print("2 - Exit program")
print("================================================================")


exitChar = True
while exitChar == True:
    print()
    option = input("Menu option: ")

    if option == '1':
        print("-- Calculate batting average --")
        num_bats_input = int(input("Official number of at bats: "))
        num_hits_input = int(input("Number of hits: "))

        #calc avg and round
        batting_avg = num_hits_input / num_bats_input
        batting_avg = round(batting_avg, 3)
        print(f"Batting average: {batting_avg}")

    elif option == '2':
        print("Bye!")
        exitChar = False

    else:
        print("Not a valid option. Please try again")