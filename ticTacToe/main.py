#This is lizzy Saldana's tic tac toe game
import random
print("welcome to tic tac toe! You will be X's and the computer is the O.")


grid = [1, 2, 3, 4, 5, 6, 7, 8, 9]


choice = ["1. top left", "2. top middle", "3. top right", "4. middle left", "5. exact middle", "6. middle right", "7. bottom left", "8. bottom middle", "9. bottom right"]

def place():
    global choice
    print("Where would you like to go?")
    options = int(input(choice))
    if options == 1:
        if grid[0] == 'X':
            return 'taken'
        grid[0] = "X"
        choice.pop[0]
    elif options == 2:
        if grid[0] == 'X':
            return 'taken'
        grid[1] = 'X'
        choice.pop[1]
    elif options == 3:
        if grid[0] == 'X':
            return 'taken'
        grid[2] = 'X'
        choice.pop[2]
    elif options == 4:
        if grid[0] == 'X':
            return 'taken'
        grid[3] = 'X'
        choice.pop[3]
    elif options == 5:
        if grid[0] == 'X':
            return 'taken'
        grid[4] = 'X'
        choice.pop[4]
    elif options == 6:
        if grid[0] == 'X':
            return 'taken'
        grid[5] = 'X'
        choice.pop[5]
    elif options == 7:
        if grid[0] == 'X':
            return 'taken'
        grid[6] = 'X'
        choice.pop[6]
    elif options == 8:
        if grid[0] == 'X':
            return 'taken'
        grid[7] = 'X'
        choice.pop[7]
    elif options == 9:
        if grid[0] == 'X':
            return 'taken'
        grid[8] = 'X'
        choice.pop[8]


def computer():
    global choice
    comp_choice = random.randint(1,9)
    if comp_choice == 1:
        if grid[0] == 'X' or grid[0] == 'O':
            return 'taken'
        grid[0] = "O"
        choice.pop[0]

    elif comp_choice == 2:
        if grid[1] == 'X' or grid[1] == 'O':
            return 'taken'
        grid[1] = "O"
        choice.pop[1]

    elif choice == 3:
        if grid[2] == 'X' or grid[2] == 'O':
            return 'taken'
        grid[2] = "O"
        choice.pop[2]

    elif choice == 4:
        if grid[3] == 'X' or grid[3] == 'O':
            return 'taken'
        grid[3] = "O"
        choice.pop[3]
        
    elif choice == 5:
        if grid[4] == 'X' or grid[4] == 'O':
            return 'taken'
        grid[4] = "O"
        choice.pop[4]

    elif choice == 6:
        if grid[5] == 'X' or grid[5] == 'O':
            return 'taken'
        grid[5] = "O"
        choice.pop[5]

    elif choice == 7:
        if grid[6] == 'X' or grid[6] == 'O':
            return 'taken'
        grid[6] = "O"
        choice.pop[6]

    elif choice == 8:
        if grid[7] == 'X' or grid[7] == 'O':
            return 'taken'
        grid[7] = "O"
        choice.pop[7]

    elif choice == 9:
        if grid[8] == 'X' or grid[8] == 'O':
            return 'taken'
        grid[8] = "O"
        choice.pop[8]


        

while True:
    player_place = place()
    comp = computer()
    if player_place == 'taken':
        print("Already taken, choose another spot.")
        place()
    elif player_place == 'quit':
        break
    if comp == 'taken':
        computer()
    print(grid[0], """|""", grid[1], """|""", grid[2],
          grid[3], """|""", grid[4], """|""", grid[5],
          grid[6], """|""", grid[7], """|""", grid[8])

 