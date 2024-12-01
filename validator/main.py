#This is Lizzy Saldana's password validator assignment
import re

def password_checker():
    while True:
        word = input("What is your password?: ")
        if len(word) < 8:
            print("Please increase the length of your password.")
            continue
        if not re.search(r'[!@#$%^&*(),.?"|<>{}:;]', word):
            print("Please include a symbol: @, #, $, %, *, &")
            continue
        if not re.search(r'\d', word):
            print("Please include a number in your password.")
            continue
        print("Your password is secure!")
        break

password_checker()
    

        









