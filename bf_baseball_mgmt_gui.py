#!/usr/bin/env python3
# Bryce Fish
# Project 1
# Server-Side Programming
# Sept 16: parts 1-2

# display a welcome message
print("================================================================")
print("\t\tBaseball Team Manager\n")
print("This program calculates the batting average for a player based \n on the player\'s official number of at bats and hits.")
print("================================================================")
# get user input
player_name_input = (input("Player's Name: "))
num_bats_input = int(input("Official number of at bats: "))
num_hits_input = int(input("Number of hits: "))

#calc avg and round
batting_avg = num_hits_input / num_bats_input
batting_avg = round(batting_avg, 3)

print()
print(f"{player_name_input}'s batting average is {batting_avg}")
