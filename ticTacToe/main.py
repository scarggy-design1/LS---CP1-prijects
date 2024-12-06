#This is lizzy Saldana's tic tac toe game

print("welcome to tic tac toe! You will be X's and the computer is the O.")


grid = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
choice = ["1. top left", "2. top middle", "3. top right", "4. middle left", "5. exact middle", "6. middle right", "7. bottom left", "8. bottom middle", "9. bottom right"]

def place():
    options = int(input("Where would you like to go?:", choice))
         
    if options == 1:
        grid[0] = "X"
        choice.remove[0]
    elif options == 2:
        grid[1] = 'X'
        choice.remove[1]
    elif options == 3:
        grid[2] = 'X'
        choice.remove[2]
    elif options == 4:
        grid[3] = 'X'
        choice.remove[3]
    elif options == 5:
        grid[4] = 'X'
        choice.remove[4]
    elif options == 6:
        grid[5] = 'X'
        choice.remove[5]
    elif options == 7:
        grid[6] = 'X'
        choice.remove[6]
    elif options == 8:
        grid[7] = 'X'
        choice.remove[7]
    elif options == 9:
        grid[8] = 'X'
        choice.remove[8]



place()
 