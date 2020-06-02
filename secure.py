import os
import errno
from passlib.hash import pbkdf2_sha256

try:
    file = open(".masterpass", 'r+')
    masterpass = input("Please enter your masterpass: ")
    with open('.masterpass') as f:
        correctpassword = f.readline()
        if(pbkdf2_sha256.verify(masterpass, correctpassword)):
            #continue
        else:
            #exit
    
except FileNotFoundError:
    file = open(".masterpass", 'w')
    masterpass = input("Please enter the masterpass you want to use. Remember it, it will be asked every time you execute the script.")
    hash = pbkdf2_sha256.hash(masterpass)
    file.write(hash)
    file.close()