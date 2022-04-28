'''
Tic-Tac-Toe: My solution
Author: Felix Flores
Course: CSE210 
Date: April 27
'''

print("Welcome to tictactoe\n")

def create_board():
    values=[]
    for number in range(9):
        values.append(number + 1)
    return values

#print the game board
def printBoard(values):
    print("\n")
    print("     |     |")
    print("  {}  |  {}  |  {}".format(values[0],values[1], values[2]))
    print("_____|_____|_____")
    print("     |     |")
    print("  {}  |  {}  |  {}".format(values[3],values[4], values[5]))
    print("_____|_____|_____")
    print("     |     |")
    print("  {}  |  {}  |  {}".format(values[6],values[7], values[8]))
    print("     |     |")
    print("\n")

#take player position
def player_input():
    global board
    global current_player
    inp = int(input("Enter a number 1-9: "))
    if inp >= 1 and inp <= 9:
        if board[inp-1] == "X" or board[inp-1] == "O":
            print("\nspot already taken")
        else:
            board[inp-1] = current_player
    
    else:
        print("\nChoose a number between 1-9")

#Check win or tie
def checkhorizontle(board):
    global winner
    if board[0] == board[1] == board[2]:
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5]:
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8]:
        winner = board[6]  
        return True  

def checkvertical(board):
    global winner
    if board[0] == board[3] == board[6]:
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7]:
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8]:
        winner = board[2]
        return True

def checkdiagonal(board):
    global winner
    if board[0]==board[4]==board[8]:
        winner = board[0]
        return True
    elif board[2]==board[4]==board[6]:
        winner = board[2]
        return True

def checktie(board):
    global GameRunning
    for spot in range(9):
        if board[spot] !="X" and board[spot] != "O":
            return False 
    GameRunning=False 
    printBoard(board)
    print(f"It is a TIE!!!! thank you for playing") 
    return True
    
#switch player 
def switchPlayer ():
    global current_player
    if current_player == "X":
        current_player ="O"
    else:
        current_player= "X"

#Check for Win 
def checkWin():
    global GameRunning
    if checkhorizontle(board) or checkdiagonal(board) or checkvertical(board):
        print (f"The winner is {winner}")
        printBoard(board)
        print("Good game. Thanks for playing!")
        GameRunning=False

board = create_board()
current_player = "X"
winner = None
GameRunning = True
def main():
    while GameRunning==True:
        printBoard(board)
        player_input()
        checkWin()
        checktie(board)
        switchPlayer()

if __name__ == "__main__":
    main()
