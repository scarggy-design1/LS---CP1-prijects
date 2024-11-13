#This is Lizzy saldanas deciphering assignment
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
text = input("Pick a word: ")

def ciper(x):
    letters = list(x)
    for x in alphabet:
        check = ord(x)
        check=+1
        done = chr(check)
        print(done)
        

ciper(text)


