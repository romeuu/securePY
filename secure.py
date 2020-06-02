import os
import errno
from passlib.hash import pbkdf2_sha256

def menu():
    print("What do you want to do?\n1. Add new password.\n2. Modify existent password.\n3. Delete password.\n4. List current passwords.\n5. Exit")
    select = int(input("Enter your choice: "))
    return select

def addPassword(web, password):
    try:
        file = open('.passwords', "a+")
        file.write(web+":"+password+"\n")
        file.close()
    except FileNotFoundError:
        file = open('.passwords', 'w')
        file.write(web+":"+password+"\n")
        file.close()

def modifyPassword(web, password):
    try:
        a_file = open(".passwords", "r")
        list_of_lines = a_file.readlines()
        for n, i in enumerate(list_of_lines):
            if web in i:
                list_of_lines[n] = web+":"+password+"\n"
                
        a_file = open(".passwords", "w")
        a_file.writelines(list_of_lines)
        a_file.close()

    except FileNotFoundError:
        print("There are no passwords stored for you.")

def deletePassword(web):
    try:
        a_file = open(".passwords", "r")
        list_of_lines = a_file.readlines()
        for n, i in enumerate(list_of_lines):
            if web in i:
                list_of_lines[n] = ""
                
        a_file = open(".passwords", "w")
        a_file.writelines(list_of_lines)
        a_file.close()

    except FileNotFoundError:
        print("There are no passwords stored for you.")

def checkOption(selection):
    if(selection == 1):
        website = input("Enter the website you want to save a password for: ")
        password = input("Password that you want to save: ")
        addPassword(website, password)
    elif(selection == 2):
        website = input("Enter the website you want to edit the password for: ")
        password = input("Password that you want to edit: ")
        modifyPassword(website, password)
    elif(selection == 3):
        website = input("Enter the website you want to delete the password for: ")
        deletePassword(website)
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

