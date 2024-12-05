#This is lizzy Saldana's rock paper scissors assignment

score = 0
def computer():
    import random 
    choice = random.randint(1,3)
    if choice == 1:
        print("computer chooses Rock")
        return 1
    if choice == 2:
        print("computer chooses Paper")
        return 1
    if choice == 3:
        print("computer chooses scissors")
        return 1

        
    

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
        
    if ask == 'b':
        print("you chose paper!")
        return 'b'
            
    if ask == 'c':
        print("you chose scissors!")
        return 'c'
        
    if ask == 'd':
        print(score)
        print("You chose to quit.")
        return 'd'
       

def outcome(): 
    if user() == 'a' and computer() == 1 or user() == 'b' and computer() == 2 or user() == 'c' and computer() == 3:
        print("tie!")
        print(score)
    if user() == 'a' and computer() == 2:
        print("computer wins")
    if user() == 'a' and computer() == 3:
        print("user wins")
        score=+1
        print(score)
    if user() == 'b' and computer() == 1:
        print("user wins!")
        score=+1
        print(score)
    if user() == 'b' and computer() == 3:
        print("Computer wins!")
    if user() == 'c' and computer() == 1:
        print("Computer wins")
    if user() == 'c' and computer() == 2:
        print("user wins!")
        score=+1
        print(score)


while True:
    user()
    computer()
    outcome()