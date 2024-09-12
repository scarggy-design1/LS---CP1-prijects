#this is lizzy saldanas basic calculator

v1 = int(input("Choose a number: "))
v2 = int(input("Choose another number: "))

print(v1, "divided by", v2, "=", v1/v2)
print(v2, "divided by", v1, "=", v2/v1)
print(v1, "times", v2, "=", v1*v2)
print(v2, "plus", v1, "=", v2+v1)
print(v1, "minus", v2, "=", v1-v2)
print(v2, "minus", v1, "=", v2-v1)
print(v1, "modules", v2, "=", v1%v2)
print(v2, "modules", v1, "=", v2%v1)
print(v1, "raised to", v2, "=", v1**v2)
print(v2, "raised to", v1, "=", v2**v1)
print(v1, "divided by", v2, "=", v1//v2, "(rounded)")
print(v2, "divided by", v1, "=", v2//v1, "(rounded)")
