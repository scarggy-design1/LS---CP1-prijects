#This is Lizzy saldanas deciphering assignment

def ciper():
    text = input("Pick a word: ")
    string = ''
    for x in text:
        check = (ord(x))+1
        string = string + chr(check)

    print("orginal: ", text)
    print("code: ", string)
        

ciper()


