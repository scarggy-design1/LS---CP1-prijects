#This is Lizzy Saldanas attempt at a palindrome

x = input("Pick a word and I'll check if its a palindrome or not!: ") 

check = x [::-1]

print(check)

if check == x:
    print("Yes its a palidrome!")
else:
    print("Nope, this isn't one.")


