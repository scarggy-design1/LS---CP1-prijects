#This is Lizzy Saldana's password validator assignment
x = ["@", "#", "$", "%", "*", "&"]
num = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
def password_checker():
    while True:
        word = input("What is your password?: ")
        
        if len(word) < 8:
            print("Please increase the length of your password.")
            continue
        if x in word:
            print("Please include a symbol: @, #, $, %, *, &")
            continue
        if num in word:
            print("Please include a number in your password.")
            continue
        print("Your password is secure!")
        break

password_checker()
    

        









