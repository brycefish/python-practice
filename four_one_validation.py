#!/usr/bin/env python3
#Bryce Fish
#Lab 4-1
        
def get_float (prompt, low, high):
    is_valid = False
    while is_valid == False:
        num = float(input(prompt))
        if num > low and num <= high:
            is_valid = True
            return num
        else:
            print("Entry must be greater than", low, "and less than or equal to", high)   
                
def get_int (prompt, low, high):
    is_valid = False
    while is_valid == False:
        num = int(input(prompt))
        if num > low and num <= high:
            is_valid = True
            return num
        else:
            print("Entry must be greater than", low, "and less than or equal to", high)   


def main():
    choice = "y"
    while choice.lower() == "y":
        
        # get input from the user
        valid_float = get_float("Enter a number: ", 0, 1000)
        print()
        print("Valid float = ", valid_float)
        valid_int = get_int("Enter a number: ", 0, 50)
        print("Valid integer = ", valid_int)
        print()

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")
    
if __name__ == "__main__":
    main()

 