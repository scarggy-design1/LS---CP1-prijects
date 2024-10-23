
your_list = []
def add(your_list):
    addend = input("What would you like to add?: ")
    your_list.append(addend)
    print("your list is now: ", your_list)
    return your_list

def remove(your_list):
    take = input("What would you like to remove?: ")
    your_list.remove(take)
    print("your list is now: ", your_list)
    return your_list


while True:

    action = input("""What would you like to do?

        Enter 1 to add item

        Enter 2 to remove item

        Enter 3 to leave the list:\n""")

    if action =="1":

        add(your_list)

    elif action =="2":

        remove(your_list)

    else:

        print("Have a nice day!")

        break