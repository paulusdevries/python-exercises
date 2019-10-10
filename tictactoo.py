import random, copy, os

board = {
    "1a": " ",
    "2a": " ",
    "3a": " ",
    "1b": " ",
    "2b": " ",
    "3b": " ",
    "1c": " ",
    "2c": " ",
    "3c": " "
}


def isEmpty(turn):
    global board
    if board[turn] != " ":
        return False
    else:
        return True


def clearscreen():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def playerTurn(turn, board):
    if turn in board:
        if isEmpty(turn):
            board[turn] = "X"
            return True
        else:
            print("Your choice is occupied! choose another spot!")
            return False
    else:
        print("Your choice " + turn + " isn\'t valid!")
        return False


# choice is meant for the computer turn to determine whether the computer should use artificial intelligence
# to make a move or if it should only use randomness


def computerTurn(choice, board):
    if not boardDone(board):
        if not isThreeinaRow(board):
            if choice:
                chosen = False
                # having a randomly chosen move
                turn = random.choice(list(board))

                # iterate through possible moves and see if there might be a winning move
                for key in board:
                    if isEmpty(key) and not chosen:
                        for hc in ["O", "X"]:
                            copyboard = copy.deepcopy(board)
                            copyboard[key] = hc
                            if isThreeinaRow(copyboard):
                                board[key] = "O"
                                chosen = True
                                break

                # in case previous operation did not work out:
                # see if the random move might be a winning move for either me or my opponent
                if isEmpty(turn) and not chosen:
                    for move in ["O", "X"]:
                        copyboard = copy.deepcopy(board)
                        copyboard[turn] = move
                        if isThreeinaRow(copyboard):
                            board[turn] = "O"
                            chosen = True
                            break

                # in case previous operation did not work out:
                # if not occupied chose the center spot
                if not chosen and isEmpty("2b"):
                        board["2b"] = "O"
                        chosen = True

                # in case previous operation did not work out:
                # if not occupied chose one of the edges
                if not chosen:
                    for edges in ["1a", "3a", "1c", "3c"]:
                        if isEmpty(edges):
                            copyboard = copy.deepcopy(board)
                            copyboard[edges] = "O"
                            if isThreeinaRow(copyboard):
                                board[edges] = "O"
                                chosen = True
                                break
                            board[edges] = "O"
                            chosen = True
                            break

                    # in case previous operation did not work out:
                    # iterate through random spots and occupy the first possibility only based on availability

                    if not chosen:
                        while True:
                            turn = random.choice(list(board))
                            if isEmpty(turn):
                                board[turn] = "O"
                                break
            else:
                while True:
                    turn = random.choice(list(board))
                    if isEmpty(turn):
                        board[turn] = "O"
                        break
    return board


# check if the game is done i.e. the board is done or full


def boardDone(board):
    if not isThreeinaRow(board):
        fullSpots = 0
        for key in board:
            if board[key] != " ":
                fullSpots += 1

        if fullSpots == 9:
            print("Baord Full, even game")
            return True
        else:
            return False
    else:
        # no need for checking since there is already three in a row returning boolean value
        return False


def drawBoard(board):
    print(" 1   2   3")
    print("")
    print(board["1a"] + " | " + board["2a"] + " | " + board["3a"] + "  A")
    print("-----------")
    print(board["1b"] + " | " + board["2b"] + " | " + board["3b"] + "  B")
    print("-----------")
    print(board["1c"] + " | " + board["2c"] + " | " + board["3c"] + "  C")


def isThreeinaRow(board):
    threeinaRow = False
    if board["1a"] == board["1b"] and board["1a"] == board["1c"] and board["1a"] != " ":
        print("Yeah three in line 1a 1b 1c, " + board["1a"] + " wins")
        threeinaRow = True
    elif board["1a"] == board["2b"] and board["1a"] == board["3c"] and board["1a"] != " ":
        print("Yeah three in line 1a 2b 3c, " + board["1a"] + " wins")
        threeinaRow = True
    elif board["2a"] == board["2b"] and board["2a"] == board["2c"] and board["2a"] != " ":
        print("Yeah three in line 2a 2b 2c, " + board["2a"] + " wins")
        threeinaRow = True
    elif board["3a"] == board["3b"] and board["3a"] == board["3c"] and board["3a"] != " ":
        print("Yeah three in line 3a 3b 3c, " + board["3a"] + " wins")
        threeinaRow = True
    elif board["1a"] == board["2a"] and board["1a"] == board["3a"] and board["1a"] != " ":
        print("Yeah three in line 1a 2a 3a, " + board["1a"] + " wins")
        threeinaRow = True
    elif board["1b"] == board["2b"] and board["1b"] == board["3b"] and board["1b"] != " ":
        print("Yeah three in line 1b 2b 3b, " + board["1b"] + " wins")
        threeinaRow = True
    elif board["1c"] == board["2c"] and board["1c"] == board["3c"] and board["1c"] != " ":
        print("Yeah three in line 1c 2c 3c, " + board["1c"] + " wins")
        threeinaRow = True
    elif board["1c"] == board["2b"] and board["1c"] == board["3a"] and board["1c"] != " ":
        print("Yeah three in line 1c 2b 3a, " + board["1c"] + " wins")
        threeinaRow = True

    return threeinaRow


def main():
    global board
    drawBoard(board)
    print("Coinflip to determine if either computer or player may start...")
    coinflip = random.choice([0, 1, 0, 1, 0, 1, 0, 1, 0, 1])
    if coinflip == 0:
        print("Player may start...")
        while not isThreeinaRow(board) and not boardDone(board):

            if playerTurn(input("Input your choice i.e: 1a or 1b: "), board):
                clearscreen()
                drawBoard(board)
                computerTurn(True, board)
                drawBoard(board)
            else:
                continue

    else:
        print("Computer may start...")
        counterc = 0
        counterp = 0
        while not isThreeinaRow(board) and not boardDone(board):
            if counterc == counterp:
                computerTurn(True, board)
                drawBoard(board)
                counterc += 1
            if not boardDone(board) and playerTurn(input("Input your choice i.e: 1a or 1b: "), board):
                drawBoard(board)
                clearscreen()
                counterp += 1
            else:
                continue


pass


if __name__ == '__main__':
    main()

