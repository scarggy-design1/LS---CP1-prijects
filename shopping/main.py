



while True:

    action = int(input("""What would you like to do?
                   
    Enter 1 to add item
                   
    Enter 2 to remove item
                   
    Enter 3 to leave the list:\n"""))

    additem=+1
    remove= additem-1

    if action == 1:

        print(additem)
        additem=+1

    elif action == 2:

        print(remove)

    elif action ==3 :

        print("you currently have ", additem, " items!")
    else:
        print("have a wonderful day")
        break
   