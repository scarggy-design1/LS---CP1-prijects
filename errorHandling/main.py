#This is Lizzy Saldana's Error Handling Calculator
while True:
    num1 = int(input("Pick any whole number (this is your first number): "))
    num2 = int(input("pick another whole number (this is your second number): "))
    try: 
        number = num1+num2
    except:
        print('you did not input numbers. Try again')
        continue

    ask = input("""What operation would you like to preform?:
                a. multiplication
                b. division
                c. addition
                d. subtraction
                e. floor divison
                f. mod
                g. exponents
                h. quit
                """)

    if ask == 'a':
        op = num1*num2
        print(op)
        continue
    if ask == 'b':
        if num2 or num1 == 0:
            print("you cannot divide by zero, sorry!")
            continue
        op = num1/num2
        print(op)
    if ask == 'c':
        op = num1+num2
        print(op)
        continue
    if ask == 'd':
        op = num1-num2
        print(op)
        continue
    if ask == 'e':
        if num2 or num1 == 0:
            print("you cannot divide by zero, sorry!")
            continue
        op = num1//num2
        print(op)
    if ask == 'f':
        if num2 or num1 == 0: 
            print("you cannot divide by zero, sorry!")
            continue
        op = num1%num2
        print(op)
    if ask == 'g':
        op = num1**num2
        print(op)
        continue
    if ask == 'h':
        break