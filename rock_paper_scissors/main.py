#This is lizzy Saldana's rock paper scissors assignment
game = True
score = 0
def computer():
    import random
    num = random.randint(1,3)
    if num == 1:
        print("ROCK")
        
    if num == 2:
        print("PAPER")
        
    if num == 3:
        print("SCISSORS")
        

def user():
    ask= input("""Pick:
               1. Rock
               2. Paper
               3. Scissors
               """)
    if ask == '1':
        print("You choose rock!")
    if ask == '2':
        print("You choose paper!")
    if ask == '3':
        print("You choose scissors!")

def outcome():
    if computer() == 3 and user() == '1':
        print("User wins!")
        score+=1
    if computer() == 1 and user() == '3':
        print("Computer wins!")
    if computer() == 2 and user() == '1':
        print("Computer wins!")
    if computer() == 1 and user() == '2':
        print("User wins!")
        score+=1
    if computer() == 3 and user() == '3':
        print("Tie!")
    if computer() == 2 and user() == '2':
        print("Tie!")
    if computer() == 1 and user() == '1':
        print("Tie!")
    if computer() == 2 and user() == '3':
        print("User wins!")
        score+=1
    if computer() == 3 and user() == '2':
        print("Computer Wins!")


while game == True:
    user()
    computer()
    outcome()
