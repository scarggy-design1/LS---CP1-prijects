#This is Lizzy Saldana's simple quiz assignment
score = 0
question = True
correct = 'correct! Next question. '
incorrect= 'Wrong. Next question. '
print("Welcome to a fairly easy 5 question quiz!")



q1 = input('''What is the name of the best math teacher of all time?:
        a. Mr. C
        b. Mr. M
        c. Mrs. Cannon!
        d. Mr. L
            ''')
if q1:
    if q1 == 'c':
        score+=1
        print(correct, score, "pts so far")
        q2 = input('''What is the square root of 225?:
        a. 5
        b. 7
        c. 14
        d. 15
            ''')
    if q1 != 'c':
        print(incorrect)
        qv2 = input(''' what is 5x5?:
        a. 50
        b. 25
        c. 20
        d. 55
            ''')
    if q2 == 'd' or qv2 == 'b':
        score+=1
        print(correct, score, "pts so far")
        q3 = input('''If you make 40$ an hour and work 40 hour weeks, how much money will you make by the end of 4 weeks?:
        a. $1120
        b. $600
        c. $11120
        d. $1201
            ''')
        if q3 != 'a':
            print(incorrect)
            qv3 = input(''' what is 20-10?:
        a. 30
        b. 5
        c. 20
        d. 10
            ''')
    if q3 == 'a' or qv3 == 'd':
        score+=1
        print(correct, score, "pts so far")
        q4 = input('''what is the square root of -1?:
        a. error
        b. i
        c. squareroot of 1
        d. none of the above.
            ''')
        if q4 != 'b':
            print(incorrect)
            qv4 = input("""What is 7x2?:
        a. 20
        b. 9
        c. 14
        d. 12
            """)
    if q4 == 'b' or qv4 == 'c':
        score+=1
        print(correct, score, "pts so far")
        q5 = input('''What is the average of 37 and 3?:
        a. 20.0
        b. 21
        c. 20.1
        d. 19.9
            ''')
        if q5 != 'a':
            print(incorrect)
            qv5 = input("""What is the average of 4 and 10?:
        a. 14
        b. 7
        c. 10
        d. 4
            """)
    if q5 == 'a' or qv5 == 'b':
        score+=1
        print("Correct and congratulations! You finished with:", score, "out of 5 points.")
    

                    


