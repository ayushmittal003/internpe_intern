# function for print a board
def printBoard(xState, zState):
    zero  = 'X' if xState[0] else ('O' if zState[0] else '')
    one   = 'X' if xState[1] else ('O' if zState[1] else '')
    two   = 'X' if xState[2] else ('O' if zState[2] else '')
    three = 'X' if xState[3] else ('0' if zState[3] else '')
    four  = 'X' if xState[4] else ('O' if zState[4] else '')
    five  = 'X' if xState[5] else ('O' if zState[5] else '')
    six   = 'X' if xState[6] else ('O' if zState[6] else '')
    seven = 'X' if xState[7] else ('O' if zState[7] else '')
    eight = 'X' if xState[8] else ('O' if zState[8] else '')
    print("Here,start the Game--->")
    print(f" {zero}  | {one}  | {two}")
    print("---|---|---")
    print(f" {three}  | {four}  | {five}")
    print("---|---|---")
    print(f" {six}  | {seven}  | {eight}")


# condition check for win
def checkWin(xState, zState):
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if ((xState[win[0]] + xState[win[1]] + xState[win[2]]) == 3):
            print("Ayush Won the match")
            return 1
        if ((zState[win[0]] + zState[win[1]] + zState[win[2]]) == 3):
            print("Python Won the match")
            return 0
    return -1


xState = [0,0,0,0,0,0,0,0,0]
zState = [0,0,0,0,0,0,0,0,0]
turn = 1  # 1 for ayush and 0 for computer
print("Welcome to Tic Tac Toe")
print("Position of number--->")
print(" 0 | 1 | 2")
print("-- |---|---")
print(" 3 | 4 | 5")
print("-- |---|---")
print(" 6 | 7 | 8")
while (True):
    printBoard(xState, zState)

    if (turn == 1):
        print("Ayush's Chance")
        value = int(input("Please enter a number: "))
        xState[value] = 1
    else:
        print("Python's Chance")
        value = int(input("Please enter a value: "))
        zState[value] = 1

    cwin = checkWin(xState, zState)
    if (cwin != -1):
        print("Match over")
        break

    turn = 1 - turn

