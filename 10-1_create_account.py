# Bryce Fish
# Sep 21
# Lab 10-1

def main():
    full_name = get_full_name()
    password = get_password()
    email_address = get_email()
    phone_number = get_phone_num()
    print()
    
    first_name = get_first_name(full_name)   
    print(f"Hi {first_name}, thanks for creating an account.")
    print(f"We'll text your confirmation code to this number: {phone_number}")
    
def get_full_name():
    while True:
        name = input("Enter full name:       ").strip()
        if " " in name:
            return name
        else:
            print("You must enter your full name.")
    
def get_first_name(full_name):
    index1 = full_name.find(" ")
    first_name = full_name[:index1]
    return first_name
    
def get_password():
    while True:
        digit = False
        cap_letter = False
        password = input("Enter password:        ").strip()
        for char in password:
            if char.isdigit():
                digit = True
            elif char.isupper():
                cap_letter = True
        if digit == False or cap_letter == False or len(password) < 8:
            print(f"Password must be 8 characters or more \n"
                  f"with at least one digit and one uppercase letter.")
        else:
            return password
        
def get_email():
    while True:
        email = input("Enter email address:       ").strip()
        at_index = email.find("@")
        dot_index = email.find(".com", at_index)
        if at_index == -1 or dot_index == -1:
            print("Please enter a valid email address.")
        else:
            return email

def get_phone_num():
    while True:
        phone_num = input("Enter phone number:        ").strip()
        for lightning_mcqueen in " -.()": 
            phone_num = phone_num.replace(lightning_mcqueen, "")
        if len(phone_num) != 10 or phone_num.isdigit() == False:
            print("Please enter a 10-digit phone number.")
        else:
            phone_num = phone_num[0:3] + "." + phone_num [3:6] + "." + phone_num[6:]
            return phone_num
    # its a Cars movie reference

if __name__ == "__main__":
    main()
