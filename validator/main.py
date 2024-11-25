#This is Lizzy Saldana's password validator assignment
password = True
x = ["@", "#", "$", "%", "*", "&"]
num = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

while password:
    word = input("What is your password?: ")
    convert = list(word)
    if convert in x and num:
        length = len(convert)
        if length >= 8:
            print("Your password is secure enough.")
            break