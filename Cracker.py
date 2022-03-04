import hashlib
from passlib.hash import bcrypt
from urllib.request import urlopen
from bcrpytext import bcryptfunc
import random
import string

chars = string.printable
chars_list = list(chars)

options = input("Which attack? (B/D)").upper()
#Brute force attack
if options == 'B':

    password = input("Enter your password: ")

    guess_password = ""

    while(guess_password != password):
        guess_password = random.choices(chars_list, k=len(password))

        print(str(guess_password))

        if (guess_password == list(password)):
            print("Your password is: " +"".join(guess_password))
            break

else:
    hashvalue = input("Enter a string to hash: ")

#Hash for SHA256
    hashobj2 = hashlib.sha256()
    hashobj2.update(hashvalue.encode())
    print('\n SHA-256 Hash: ' + hashobj2.hexdigest())

#hash for MD5
    hashobj1 = hashlib.md5()
    hashobj1.update(hashvalue.encode())
    print('\n MD5 Hash: ' + hashobj1.hexdigest())

#Hash for Bcrypt
    hashobj3 = bcrypt.hash(hashvalue)
    print('\n Bcrypt Hash: ' + hashobj3)

#Dictionary attack for SHA256
    crackhash = input("\nPress 1 to crack SHA-256, 2 for MD5, 3 for Bcrypt: ")

    if crackhash == '1':
        sha256hash = input("\nEnter SHA-256 Hash Value: ")
  
        passlist = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(), 'utf-8')

        for i in passlist.split('\n'):
            hashguess = hashlib.sha256(bytes(i, 'utf-8')).hexdigest()
            if hashguess == sha256hash:
                print("Password Found!\nThe password is: " + str(i))
                quit()
            else:
                print("Searching...")

        print("Unable to find password in list :(")

#Dictionary for MD5
    elif crackhash == '2':
        MD5hash = input("Enter MD5 Hash Value: ")
  
        passlist2 = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(), 'utf-8')

        for i in passlist2.split('\n'):
            hashguess2 = hashlib.md5(bytes(i, 'utf-8')).hexdigest()
            if hashguess2 == MD5hash:
                print("\n\nPassword Found!" + "\nThe password is: " + str(i))
                quit()
            else:
                print("\n Searching...")

        print("Unable to find password in list :(")

#Dictionary for Bcrypt
    elif crackhash == '3':

        wordlist = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(), 'utf-8')

        words = wordlist.splitlines()

        hash = input('Enter Bcrypt Hash Value: ')
        length = len(words)

        correct_word = ""
        found = 0
        for (index, word) in enumerate(words):
            bcryptfunc(index, length)
            correct = bcrypt.verify(word, hash)
            if (correct):
                correct_word = word
                found += 1
                break

        if (found == 1):
            print("\n\nPassword Found!")
            print("The Password is:", correct_word)
        else:
            print("\n\nUnable to find password in list :(")
    else:
        print("invalid number") 
