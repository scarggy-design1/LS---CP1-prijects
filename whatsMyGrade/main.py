#This is Lizzy Saldanas Whats my grade? Assignment


grade = float(input("What percentage do you have in your class?: "))
if grade < 60:
    print("You have an F")
elif grade < 64 and grade >= 60:
    print("You have a D-")
elif grade < 67 and grade >= 64:
    print("You have a D")
elif grade < 70 and grade >= 67:
    print("You have a D+")
elif grade < 74 and grade >= 70:
    print("You have a C-")
elif grade < 77 and grade >= 74:
    print("You have a C")
elif grade < 80 and grade >= 77:
    print('You have a C+')
elif grade < 84 and grade >= 80:
    print("You have a B-")
elif grade < 87 and grade >= 84:
    print("You have a B")
elif grade < 90 and grade >= 87:
    print("You have a B+")
elif grade < 94 and grade >= 90:
    print("You have an A-")
elif grade < 100 and grade >= 94:
    print("You have an A")
else:
    print("Choose a valid option.")