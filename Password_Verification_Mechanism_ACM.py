# Writen by: Zijun Hu
# Copyright © 2021 Zijun Hu. All rights reserved.
# The purpose of this program is to verify the password
import hashlib


# Define function generateACM() to generate the Access Control Matrix,
# ObjectMap, subjectMap and actionMap
def initialAC():
    global acm
    global objectMap
    global subjectMap
    global actionMap
    acm = (['V', 'N', 'N', 'V', 'N', 'V', 'N', 'N', 'N', 'N'],
           ['V', 'N', 'N', 'N', 'V', 'M', 'N', 'N', 'N', 'N'],
           ['V', 'N', 'N', 'N', 'N', 'V', 'N', 'N', 'N', 'N'],
           ['N', 'V', 'R', 'N', 'N', 'N', 'N', 'N', 'N', 'N'],
           ['V', 'N', 'N', 'N', 'N', 'V', 'V', 'N', 'N', 'N'],
           ['V', 'N', 'N', 'N', 'N', 'M', 'V', 'V', 'N', 'N'],
           ['V', 'N', 'N', 'N', 'N', 'M', 'V', 'V', 'V', 'V'],
           ['V', 'N', 'N', 'N', 'N', 'C', 'N', 'N', 'N', 'N'],
           ['V', 'N', 'N', 'N', 'N', 'V', 'N', 'N', 'N', 'N'])
    objectMap = {0: "Client’s Account Balance",
                 1: "Client’s Information",
                 2: "Client’s Account",
                 3: "Contact details of Client’s Financial Advisor",
                 4: "Contact details of Client’s Financial Planner and Investment Analyst",
                 5: "Investments Portfolio",
                 6: "Private Consumer Instruments",
                 7: "Money Market Instruments",
                 8: "Derivatives Trading",
                 9: "Interest Instruments"}
    subjectMap = {0: "Clients",
                  1: "Premium Clients",
                  2: "Tellers",
                  3: "Technical Support",
                  4: "Financial Advisors",
                  5: "Financial Planners",
                  6: "Investment Analysts",
                  7: "Compliance Officers",
                  8: "Others(All employees)"}
    actionMap = {'V': 'View',
                 'M': 'Modify',
                 'R': 'Request Access',
                 'C': 'Validate'}


# Find the user in the passwd file
def findUser():
    passwordFile = open("passwd.txt", "r")
    passwordSet = passwordFile.read().splitlines()
    for pSet in passwordSet:
        userID = pSet.split(" ")[0]
        if userID == inputUsername:
            return [pSet.split(" ")[1], pSet.split(" ")[2]]
    return False


# Checks the role for the input User ID
def checkRole():
    UserInfoFile = open("UserInfo.txt", "r")
    UserInfoSet = UserInfoFile.read().splitlines()
    for uSet in UserInfoSet:
        userID = uSet.split(" ")[0]
        if userID == inputUsername:
            return uSet.split(" ")[len(uSet.split(" ")) - 1]
    return False


# Output allow actions
def outputAccess():
    role = checkRole()
    if not role:
        print("System error, Can't find your profile...")
        return
    i = 0
    print("You are login as: " + inputUsername)
    print("Hello, " + subjectMap[int(role)])
    print("-------------------------------------")
    for r in acm[int(role)]:
        if not r == 'N':
            print(actionMap[r] + " " + objectMap[i])
        i += 1


initialAC()  # initial Access control item

# Ask user to input their User ID and Password
inputUsername = input("Enter User ID: \n")
inputPassword = input("Enter the password: \n")

userPWInfo = findUser()
if not userPWInfo:
    print("User not find, please check the UserID")
else:
    salt = bytes.fromhex(userPWInfo[0])
    dk = hashlib.pbkdf2_hmac('sha256', inputPassword.encode('utf-8'), salt, 100000).hex()
    if str(dk) == userPWInfo[1]:
        print("Access Granted!")
        outputAccess()
    else:
        print("Wrong Password, Access Failed!")
