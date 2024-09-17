#This is lizzy saldanas Quiz!!
print("5 question Quiz!")
score_keeping = 0
q1 = int(input("What is 5-3?: "))

if q1 == 2:
    print("Good Job!")
    score_keeping +=1
else:
    print('Nope.')
    
q2 = str(input("what is the hypen notation for Carbon 14?: "))


if q2 == "carbon-14":
    print("correectt!")
    score_keeping +=1
else:
    print("sorry not sorry! Its supposed to be carbon-14.")
    
q3 = str(input("What is Lizzys favorite pokemon?: "))

if q3 == "scraggy":
    print("good job! :)")
    score_keeping +=1
else:
    ("Incorrect!")

q4 = str(input("What is THE BEST drink ever?: "))

if q4 == "black tea with lemon":
    print("true")
    score_keeping +=1
else:
    print("wrong.")

q5 = str(input("Eva Kibbie is a lil slow: "))

if q5 == "duhh":
    print("Thats right-eo miss/mister!")
    score_keeping +=1
else:
    print("I mean its obvious but yes we love her <33")

print("your finall score! ", score_keeping)




