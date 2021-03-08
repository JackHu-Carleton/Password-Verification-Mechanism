# Writen by: Zijun Hu
# Copyright © 2021 Zijun Hu. All rights reserved.
# The purpose of this program is to check for weak password
import hashlib
import os


def checkPassword():
    # Password length must between 8~12 characters
    if not 8 < len(password) < 12:
        return False
    # Password must include at least:
    if not any(x.isupper() for x in password):  # – one upper-case letter;
        return False
    if not any(x.islower() for x in password):  # – one lower-case letter;
        return False
    if not any(x in ['!', '@', '#', '$', '%', '?', '∗'] for x in password):  # – one numerical digit, and
        return False
    if not any(x.isdigit() for x in password):  # – one special character from the set: {!, @, #, $, %, ?, ∗}
        return False

    # Passwords found on a list of common weak passwords (e.g., Password1, Qwerty123, or Qaz123wsx)
    # must be prohibited
    weakPasswordFile = open("weakPasswd.txt", "r")
    weakPasswordSet = weakPasswordFile.read().splitlines()
    for x in weakPasswordSet:
        if x in password:
            return False

    # Passwords matching the format of calendar dates, license plate numbers, telephone numbers, or other
    # common numbers must be prohibited
    B_month = birthday.split("/")[0]
    B_date = birthday.split("/")[1]
    B_year = birthday.split("/")[2]
    birthdayCombine = B_month + B_date + B_year
    if telephone_numbers in password or birthdayCombine in password or username in password:
        return False
    if plateNumber:
        if plateNumber in password:
            return False
    return True


def enrolUser():
    salt = os.urandom(32)
    dk = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    # Record the set of password data into the passwd.txt
    passwordFile = open("passwd.txt", "a")
    passwordFile.write(username + " ")
    passwordFile.write(salt.hex() + " ")  # Change made to store the Salt value in hex format instead bytes.
    passwordFile.write(dk.hex() + "\n")
    passwordFile.close()

    passwordFile = open("UserInfo.txt", "a")
    passwordFile.write(username + " ")
    passwordFile.write(birthday + " ")
    if plateNumber:
        passwordFile.write(plateNumber + " ")
    else:
        passwordFile.write("NoPlateInfo" + " ")
    passwordFile.write(telephone_numbers + " ")
    passwordFile.write(role + "\n")
    passwordFile.close()


username = input("Please enter the User ID: \n")
birthday = input("Please enter your birthday in the following format (MM/DD/YY) \n")
plateNumber = input("Please enter the plate number, leave blank if not apply\n")
telephone_numbers = input("Please enter your telephone number\n")

print("0.   Clients")
print("1.	Premium Clients")
print("2.	Tellers")
print("3.	Technical Support")
print("4.	Financial Advisors")
print("5.	Financial Planners")
print("6.	Investment Analysts")
print("7.	Compliance Officers")
print("8.	Others(All employees)")
role = input("Please select your position title from above:\n")

while True:
    print("Please notice the following password rules:")
    print("Password must include at least:")
    print("-    one upper-case letter.")
    print("-    one lower-case letter.")
    print("-    one numerical digit.")
    print("-    one special character from the set: {!, @, #, $, %, ?, ∗}.")
    print("Password shall not be a weak password.")
    print("Password shall not contain any personal information or User ID")
    password = input("Enter the password: \n")
    if checkPassword():
        break
    else:
        print("Password illegal,")

print("Password pass the check, enrolling user...\n")
enrolUser()
print("Congratulation, you have been enrolled successfully!")
