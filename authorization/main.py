#This is Lizzy Saldanas Authorized assignment.

authorized = ["eva", "Mr. C", "Mrs. Wanger", "Lizzy", "Catalina", "Marie", "Monica", "Jeff Bezos"]
Banned = ["Mr. M"]
admin = ["Ms. LaRose"]

ask = input("What's your name?: ")

if ask in authorized:
    print("You are an authorized User.")
elif ask in Banned:
    print("You are not an authorized user. You are BANNED")
elif ask in admin:
    print("Welcome Admin!")
else:
    print("You are not an authorized user.")