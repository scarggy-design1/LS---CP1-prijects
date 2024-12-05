#This is lizzy Saldana's rock paper scissors assignment
import random 



def computer():
    choice = random.randint(1,3)
    if choice == 1:
        print("computer chooses Rock")
        return 1
    elif choice == 2:
        print("computer chooses Paper")
        return 2
    elif choice == 3:
        print("computer chooses scissors")
        return 3
    else:
        print("something went wrong", choice)

        
    
def user():
    ask = input("""Pick:
                    a. ROCK
                    b. PAPER
                    c. SCISSORS
                    d. quit
                    """)
    if ask == 'a':
        print("you chose rock!")
        return 'a'   
    elif ask == 'b':
        print("you chose paper!")
        return 'b'    
    elif ask == 'c':
        print("you chose scissors!")
        return 'c'   
    elif ask == 'd':
        print("You chose to quit.")
        return 'd'
    else:
        print("please pick a valid choice.")
       
score = 0
def outcome(): 
    player = user()
    comp = computer()
    global score
    if player == 'a' and comp == 1 or player == 'b' and comp == 2 or player == 'c' and comp == 3:
        print("tie!")
        print(score)
    elif player == 'a' and comp == 2:
        print("computer wins")
    elif player == 'a' and comp == 3:
        print("user wins")
        score=+1
        print(score)
    elif player == 'b' and comp == 1:
        print("user wins!")
        score=+1
        print(score)
    elif player == 'b' and comp == 3:
        print("Computer wins!")
    elif player == 'c' and comp == 1:
        print("Computer wins")
    elif player == 'c' and comp == 2:
        print("user wins!")
        score=+1
        print(score)
    else:
        print(score)


while True:
    outcome()
    print("outcome finished")