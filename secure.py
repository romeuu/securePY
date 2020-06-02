import os
import errno
from passlib.hash import pbkdf2_sha256

def menu():
    print("What do you want to do?\n1. Add new password.\n2. Modify existent password.\n3. Delete password.\n4. List current passwords.\n5. Exit")
    select = int(input("Enter your choice: "))
    return select

def checkOption(selection):
    if(selection == 1):
        print("option 1")
    elif(selection == 2):
        print("option 2")
    elif(selection == 3):
        print("option 3")
    elif(selection == 4):
        print("option 4")
    elif(selection == 5):
        quit()



try:
    file = open(".masterpass", 'r+')
    masterpass = input("Please enter your masterpass: ")
    with open('.masterpass') as f:
        correctpassword = f.readline()
        if(pbkdf2_sha256.verify(masterpass, correctpassword)):
            #continue
            print("Correct password!\nEntering the vault...")

            while True:
                checkOption(menu())
        else:
            #exit
            print("Incorrect password!")
    
except FileNotFoundError:
    file = open(".masterpass", 'w')
    masterpass = input("Please enter the masterpass you want to use. Remember it, it will be asked every time you execute the script.")
    hash = pbkdf2_sha256.hash(masterpass)
    file.write(hash)
    file.close()

