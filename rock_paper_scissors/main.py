#This is lizzy Saldana's rock paper scissors assignment
import random 
score = 0
def computer():
    while True:
        choice = random.randint(1,3)
        if choice == 1:
            print("computer chooses Rock")
            return False
        if choice == 2:
            print("computer chooses Paper")
            return False
        if choice == 3:
            print("computer chooses scissors")
            return False
    

def user():

    ask = input("""Pick:
                    a. ROCK
                    b. PAPER
                    c. SCISSORS
                    d. quit
                    """)
    if ask == 'a':
        print("you chose rock!")
        
    if ask == 'b':
            print("you chose paper!")
            
    if ask == 'c':
            print("you chose scissors!")
        
    if ask == 'd':
        print(score)
       

def outcome(): 
    while True:
        if user() == 'a' and computer() == 1 or user() == 'b' and computer() == 2 or user() == 'c' and computer() == 3:
            print("tie!")
            continue
        if user() == 'a' and computer() == 2:
            print("computer wins")
            continue
        if user() == 'a' and computer() == 3:
            print("user wins")
            score=+1
            print(score)
            continue
        if user() == 'b' and computer() == 1:
            print("user wins!")
            score=+1
            print(score)
            continue
        if user() == 'b' and computer() == 3:
            print("Computer wins!")
            continue
        if user() == 'c' and computer == 1:
            print("Computer wins")
            continue
        if user() == 'c' and computer == 2:
            print("user wins!")
            score=+1
            print(score)
            continue 

while True:
    user()
    computer()
    outcome()