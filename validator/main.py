#This is Lizzy Saldana's password validator assignment
password = True
x = ["@", "#", "$", "%", "*", "&"]
num = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

while password == True:
    word = input("What is your password?: ")
    s = word
    convert = list(s)
    length = len(convert)
    if x in convert:
        if num in convert:
            if length >= 8:
                print("Your password is secure enough.")
                break