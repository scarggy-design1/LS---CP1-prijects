#This is lizzy Saldana's tic tac toe game
import random
print("welcome to tic tac toe! You will be X's and the computer is the O.")


grid = [[" ", " ", " "], 
        [" ", " ", " "], 
        [" ", " ", " "]]


choice = ["1. top left", "2. top middle", "3. top right", "4. middle left", "5. exact middle", "6. middle right", "7. bottom left", "8. bottom middle", "9. bottom right"]
print("choose 10 to quit.")
def place():
    global choice
    print("Where would you like to go?")
    options = int(input(choice))

    if options == 1:
        if grid[0][0] == 'X':
            return 'taken'
        grid[0][0] = "X"
        choice.remove("1. top left")
        
    elif options == 2:
        if grid[0][1] == 'X':
            return 'taken'
        grid[0][1] = 'X'
        choice.remove("2. top middle")

    elif options == 3:
        if grid[0][2] == 'X':
            return 'taken'
        grid[0][2] = 'X'
        choice.remove("3. top right")

    elif options == 4:
        if grid[1][0] == 'X':
            return 'taken'
        grid[1][0] = 'X'
        choice.remove("4. middle left")


    elif options == 5:
        if grid[1][1] == 'X':
            return 'taken'
        grid[1][1] = 'X'
        choice.remove("5. exact middle")

    elif options == 6:
        if grid[1][2] == 'X':
            return 'taken'
        grid[1][2] = 'X'
        choice.remove("6. middle right")

    elif options == 7:
        if grid[2][0] == 'X':
            return 'taken'
        grid[2][0] = 'X'
        choice.remove("7. bottom left")

    elif options == 8:
        if grid[2][1] == 'X':
            return 'taken'
        grid[2][1] = 'X'
        choice.remove("8. bottom middle")

    elif options == 9:
        if grid[2][2] == 'X':
            return 'taken'
        grid[2][2] = 'X'
        choice.remove("9. bottom right")

    elif options == 10:
        return 10



def computer():
    global choice
    comp_choice = random.randint(1,9)
    if comp_choice == 1:
        if grid[0][0] == 'X' or grid[0][0] == 'O':
            return 'taken'
        grid[0][0] = "O"
        choice.remove("1. top left")

    elif comp_choice == 2:
        if grid[0][1] == 'X' or grid[0][1] == 'O':
            return 'taken'
        grid[0][0] = 'O'
        choice.remove("2. top middle")

    elif choice == 3:
        if grid[0][2] == 'X' or grid[0][2] == 'O':
            return 'taken'
        grid[0][2] = 'O'
        choice.remove("3. top right")

    elif choice == 4:
        if grid[1][0] == 'X' or grid[1][0] == 'O':
            return 'taken'
        grid[1][0] = 'O'
        choice.remove("4. middle left")
        
    elif choice == 5:
        if grid[1][1] == 'X' or grid[1][1] == 'O':
            return 'taken'
        grid[1][1] = 'O'
        choice.remove("5. exact middle")

    elif choice == 6:
        if grid[1][2] == 'X' or grid[1][2] == 'O':
            return 'taken'
        grid[1][2] = 'O'
        choice.remove("6. middle right")

    elif choice == 7:
        if grid[2][0] == 'X' or grid[2][0] == 'O':
            return 'taken'
        grid[2][0] = 'O'
        choice.remove("7. bottom left")

    elif choice == 8:
        if grid[2][1] == 'X' or grid[2][1] == 'O':
            return 'taken'
        grid[2][1] = 'O'
        choice.remove("8. bottom middle")

    elif choice == 9:
        if grid[2][2] == 'X' or grid[2][2] == 'O':
            return 'taken'
        grid[2][2] = 'O'
        choice.remove("9. bottom right")

def outcome():
    player_place = place()
    comp = computer()
    if player_place == 'taken':
        print("Already taken, choose another spot.")
        place()
    elif player_place == 10:
        return 'break'
    computer()
    if comp == 'taken':
        computer()


    if grid[0][0] and grid[0][1] and grid[0][2] == 'X':
        print("X's win!")
        return 'break'
    elif grid[1][0] and grid[1][1] and grid[1][2] == 'X':
        print("X's win!")
        return 'break'
    elif grid[2][0] and grid[2][1] and grid[2][2] == 'X':
        print("X's win!")
        return 'break'
    elif grid[0][0] and grid[1][1] and grid[2][2] == 'X':
        print("X's win!")
        return 'break'
    elif grid[0][2] and grid[1][1] and grid[2][0] == 'X':
        print("X's win!")
        return 'break'
    elif grid[0][0] and grid[1][0] and grid[2][0] == 'X':
        print("X's win!")
        return 'break'
    elif grid[0][2] and grid[0][2] and grid[1][2] == 'X':
        print("X's win!")
        return 'break'
    elif grid[0][1] and grid[1][1] and grid[2][1] == 'X':
        print("X's win!")
        return 'break'
    elif grid[0][0] and grid[0][1] and grid[0][2] == 'O':
        print("O's win!")
        return 'break'
    elif grid[1][0] and grid[1][1] and grid[1][2] == 'O':
        print("O's win!")
        return 'break'
    elif grid[2][0] and grid[2][1] and grid[2][2] == 'O':
        print("O's win!")
        return 'break'
    elif grid[0][0] and grid[1][1] and grid[2][2] == 'O':
        print("O's win!")
        return 'break'
    elif grid[0][2] and grid[1][1] and grid[2][0] == 'O':
        print("O's win!")
        return 'break'
    elif grid[0][0] and grid[1][0] and grid[2][0] == 'O':
        print("O's win!")
        return 'break'
    elif grid[0][2] and grid[0][2] and grid[1][2] == 'O':
        print("O's win!")
        return 'break'
    elif grid[0][1] and grid[1][1] and grid[2][1] == 'O':
        print("O's win!")
        return 'break'
    



while True:
    print(""" 
    """,
            grid[0][0],"""|""", grid[0][1],"""|""", grid[0][2],"""
    """,
            grid[1][0],"""|""", grid[1][1],"""|""", grid[1][2], """
    """,
            grid[2][0],"""|""", grid[2][1],"""|""", grid[2][2])
    if outcome() == 'break':
        break
   
 