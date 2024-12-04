"""#This is Lizzy Saldana's simple quiz assignment
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
    right = 'c'
    if q1 == right:
        print(correct)
        score=+1
        q2 = input('''What is the square root of 225?:
        a. 5
        b. 7
        c. 14
        d. 15
            ''')
    if q1 != right:
        print(incorrect)
        qv2 = input(''' what is 5x5?:
        a. 50
        b. 25
        c. 20
        d. 55
            ''')
if q2 or qv2:
    right = 'c'
    rightv2 = 'b'
    if q2 == right or qv2 == rightv2:
        print(correct)
        score=+1
        q3 = input('''What is the square root of 225?:
        a. 5
        b. 7
        c. 14
        d. 15
            ''')
    if q1 != right:
        print(incorrect)
        qv3 = input(''' what is 5x5?:
        a. 50
        b. 25
        c. 20
        d. 55
            ''')
if q3:
    right = 'c'
    if q1 == right:
        print(correct)
        score=+1
        q2 = input('''What is the square root of 225?:
        a. 5
        b. 7
        c. 14
        d. 15
            ''')
    if q1 != right:
        print(incorrect)
        qv2 = input(''' what is 5x5?:
        a. 50
        b. 25
        c. 20
        d. 55
            ''')
if q4:
    right = 'c'
    if q1 == right:
        print(correct)
        score=+1
        q2 = input('''What is the square root of 225?:
        a. 5
        b. 7
        c. 14
        d. 15
            ''')
    if q1 != right:
        print(incorrect)
        qv2 = input(''' what is 5x5?:
        a. 50
        b. 25
        c. 20
        d. 55
            ''')
if q5:
    
      """