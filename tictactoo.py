import random

board = {
    "1a" : "   ",
    "2a" : "   ",
    "3a" : "   ",
    "1b" : "   ",
    "2b" : "   ",
    "3b" : "   ",
    "1c" : "   ",
    "2c" : "   ",
    "3c" : "   "
}
def isEmpty(turn):
    global board
    if board[turn] != "   ":
        return False
    else:
        return True


def playerTurn(turn, board):
    if isEmpty(turn):
        board[turn] = " X "
        return board
    else:
        print("Your choice isn\'t valid!")
        return board


def computerTurn(choice, board):
    if choice:
        while True:
            turn = random.choice(list(board))
            if isEmpty(turn):
                board[turn] = " O "
                break
    else:
        while True:
            turn = random.choice(list(board))
            if isEmpty(turn):
                board[turn] = " O "
                break
    return board


def boardDone(board):
    pass


def drawBoard(board):
    print(" 1   2   3")
    print("")
    print(board["1a"] + "|" + board["2a"] + "|" + board["3a"] + "  A")
    print("-----------")
    print(board["1b"] + "|" + board["2b"] + "|" + board["3b"] + "  B")
    print("-----------")
    print(board["1c"] + "|" + board["2c"] + "|" + board["3c"] + "  C")


def isThreeinaRow(board):
    threeinaRow = False
    if board["1a"] == board["1b"] and board["1a"] == board["1c"] and board["1a"] != "   ":
        print("Yeah three in line 1a 1b 1c, " + board["1a"] + " wins")
        threeinaRow = True
    elif board["1a"] == board["2b"] and board["1a"] == board["3c"] and board["1a"] != "   ":
        print("Yeah three in line 1a 2b 3c, " + board["1a"] + " wins")
        threeinaRow = True
    elif board["2a"] == board["2b"] and board["2a"] == board["2c"] and board["2a"] != "   ":
        print("Yeah three in line 2a 2b 2c, " + board["2a"] + " wins")
        threeinaRow = True
    elif board["3a"] == board["3b"] and board["3a"] == board["3c"] and board["3a"] != "   ":
        print("Yeah three in line 3a 3b 3c, " + board["3a"] + " wins")
        threeinaRow = True
    elif board["1a"] == board["2a"] and board["1a"] == board["3a"] and board["1a"] != "   ":
        print("Yeah three in line 1a 2a 3a, " + board["1a"] + " wins")
        threeinaRow = True
    elif board["1b"] == board["2b"] and board["1b"] == board["3b"] and board["1b"] != "   ":
        print("Yeah three in line 1b 2b 3b, " + board["1b"] + " wins")
        threeinaRow = True
    elif board["1c"] == board["2c"] and board["1c"] == board["3c"] and board["1c"] != "   ":
        print("Yeah three in line 1c 2c 3c, " + board["1c"] + " wins")
        threeinaRow = True
    elif board["1c"] == board["2b"] and board["1c"] == board["3a"] and board["1c"] != "   ":
        print("Yeah three in line 1c 2b 3a, " + board["1c"] + " wins")
        threeinaRow = True

    return threeinaRow


def main():
    global board
    drawBoard(board)
    while not isThreeinaRow(board):
        playerTurn(input("Input your choice i.e: 1a or 1b: "), board)
        drawBoard(board)
        computerTurn(True, board)
        drawBoard(board)

    pass

if __name__ == '__main__':
    main()

