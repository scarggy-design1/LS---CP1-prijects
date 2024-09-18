#this is Lizzy saldanas casting assignment

name = input("What is your name?: ")
age = int(input("how old are you?: "))
h = int(input("what is your height in meters?: "))
fn = int(input("what's your favorite number?: "))

print("converting...")

age2 = int(age) #will now convert age to an integer and age2
fn2 = int(fn) #favorite number is now going to be treated as an integer
h2 = float(h) #Height will be converted to a float 

print("age went from ", age, "to:", age2)
print("favorite number went from ", fn, "to:", fn2)
print("Your height went from ", h, "to:", h2)