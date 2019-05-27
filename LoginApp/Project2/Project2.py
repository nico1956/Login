#This program will let the user log in, create a new user or reset a password.
#It will read from and write to a file all the users credentials.
#
#Nico Busatto 05/09/2019

import os
import time

def main():

    idList = []             
    pswList = []

    #Move passwords and usernames to separate lists
    with open('password.dat', 'r') as f:
        for count, line in enumerate(f, start=1):
            if count % 2 == 0:
                pswList.append((line).replace('\n',''))
    with open('password.dat', 'r') as f:
        for count, line in enumerate(f, start=0):
            if count % 2 == 0:
                idList.append((line).replace('\n',''))
                                     
    menu(idList, pswList)

def menu(idl, pswl):
    
    menuOk = True

    while menuOk:
        print("Choose an option:")
        print("")
        print("1 - Sign In")
        print("2 - Create New User")
        print("3 - Reset Password")
        print("4 - Exit")
        print("")
        choice = str(input("Your selection: "))
        if choice == "1" or choice == "2": 
            if choice == "1":  
                signIn(idl, pswl)
                print("")
                menu(idl, pswl)
            else:
                createNew(idl, pswl)
                print("")
                menu(idl, pswl)
        elif choice == "3":
            resetPassword(idl, pswl)
            print("")
            menu(idl, pswl)
        elif choice == "4":
            exit()
            menu(idl, pswl)
        else:
            print("")
            print("Invalid option!")
            print("")
            continue

def signIn(idl, pswl):

    ok = False

    #Ask for username to login.
    id = str(input("Enter your username: "))
    #If username not found, print message and go back to main menu.
    if id not in idl:
        print("")
        print("Username not found!")
        print("")
        menu(idl, pswl)
    #Else obtain usename index and compare it with password index if password is found,
    #if indexes match, user is logged in.
    else:
        idIndex = idl.index(id)
        password = str(input("Enter your password: "))
        pswIndex = pswl.index(password)
        if idIndex != pswIndex:
            print("")
            print("Wrong password!")
            print("")
            menu(idl, pswl)
        else:
            print("")
            print("You are now logged in!")
            print("")
            while ok:
                text = input("Press enter to return to the menu.")
                if text == "":
                    ok = True
                    menu(idl, pswl)
                else:
                    ok = False

def createNew(idl, pswl):

    IDok = True
    pswOk = True
    ok1 = True

    #Ask for new username
    while IDok:
        newID = str(input("Enter a username: "))
        count = 0
        #Validate for characters amount.
        for c in newID:
            count += 1
        if count >= 6 and count <= 10:
            IDok = True
        else:
            print("Username must be between 6 to 10 characters.")
            createNew(idl, pswl)
        #Validate for digits amount.
        totDigits = sum(char.isdigit() for char in newID)
        if totDigits >= 2:
            IDok = True
        else:
            print("Username must contain two number!")
            createNew(idl, pswl)
        #Check for spaces in username.
        if " " in newID:
            print("Username cannot contain spaces!")
            createNew(idl, pswl)
        else:
            IDok = True
        #Check if username already exists.
        if newID in idl:
            print("Username already exists!")
            createNew(idl, pswl)
        #If all validations are passed, write new user to next line in the file, otherwise loop
        #until good.
        else:
            with open("password.dat", "a") as f:
                f.write("\n" + newID)
                f.close()
                idl.append((newID).replace('\n',''))
                IDok = False
    #Ask for new user password.
    while pswOk:
        newPsw = str(input("Enter a Password: "))
        count = 0
        #Validate for characters amount.
        for c in newPsw:
            count += 1
        if count >= 6 and count <= 12:
            pswOk = True
        else:
            print("Password must be between 6 to 12 characters.")
            continue
        #Check if at least one char is a digit.
        if any(char.isdigit() for char in newPsw):
            pswOk = True
        else:
            print("Password must contain a number!")
            continue
        #Check if at least one char is uppercase
        if any(x.isupper() for x in newPsw):
            pswOk = True
        else:
            print("Password must contain an uppercase letter!")
            continue
        #Check if at least one char is lowercase
        if any(x.islower() for x in newPsw):
            pswOk = True
        else:
            print("Password must contain a lowercase letter!")
            continue
        #Check if there is any space in new password.
        if " " in newPsw:
            print("Password cannot contain spaces!")
            continue
        else:
            pswOk = True
        #Check if password contains username.     
        if newPsw in idl:
            print("Word already used as username!")
            continue
        else:
            pswOk = True
        #Check if password is already used.
        if newPsw in pswl:
            print("Password already exist!")
            continue
        #If all validations are passed, write new user password to next line in the file, otherwise loop
        #until good.
        else:
            with open("password.dat", "a") as f:
                f.write("\n" + newPsw)
                f.close()
                pswl.append((newPsw).replace('\n',''))
                print("New user created!")
                #Ask user to press enter to return to menu and check if user does so.
                while ok1:
                    text = input("Press enter to return to the menu.")
                    if text == "":
                        ok1 = False
                        menu(idl, pswl)
                    else:
                        ok1 = True
                                 
def resetPassword(idl, pswl):

    ok = True
    ok1 = False

    #Enter password that need to be resetted.
    validatePsw = str(input("Enter your password: "))
    if validatePsw in pswl:
        while ok:
            #Ask user to enter new password and go thru option 2' password validation.
            newPsw = str(input("Enter new Password: "))
            count = 0
            for c in newPsw:
                count += 1
            if count >= 6 and count <= 12:
                ok = True
            else:
                print("Password must be between 6 to 12 characters.")
                continue
            if any(char.isdigit() for char in newPsw):
                ok = True
            else:
                print("Password must contain a number!")
                continue
            if any(x.isupper() for x in newPsw):
                ok = True
            else:
                print("Password must contain an uppercase letter!")
                continue
            if any(x.islower() for x in newPsw):
                ok = True
            else:
                print("Password must contain a lowercase letter!")
                continue
            if " " in newPsw:
                print("Password cannot contain spaces!")
                continue
            else:
                ok = True
            if newPsw in idl:
                print("Password cannot contain username!")
                continue
            else:
                ok = True
            if newPsw in pswl:
                print("Password already exist!")
                continue
            #!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!
            #The following code should detect the line that contains the password to replace 
            #and replace it with the new one. It goes in the if statement if strings match,
            # but for some reason it doesn't replace the word...!
            else:     
                with open("password.dat", 'r+') as f:
                    for line in f:
                        line = line.strip("\n")
                        if validatePsw == line:
                            line.replace(line, newPsw)
                print("Password reset successfully!")
                ok = False
                #Ask user to press enter to return to menu and check if user does so.
                while ok1:
                    text = input("Press enter to return to the menu.")
                    if text == "":
                        menu(idl, pswl)
                    else:
                        ok1 = False
    #If password to replace is not found, print a message and return to menu.
    else:
        print("")
        print("Password not found!")
        print("")
        menu(idl, pswl)

def exit():

    #Print a message that user is logged out, sleep and terminate.
    print("User signed out, program terminating.")
    time.sleep(4)
    os._exit(1)

main()