def createBoard(numBlocks):
    """Returns a new board with three pegs. The first peg has numBlocks
    number of blocks (from 1 to numBlocks). View the assignment page
    for examples and further details."""

    boardArray = []
    firstPeg = []
    for i in range(3):
        if i == 0:
            for i in range(1,numBlocks + 1):
                firstPeg.append(i)
            boardArray.append(firstPeg)
        else:
            boardArray.append([])

    return boardArray
    
def getNumBlocks(board):
    """Returns the number of blocks contained within the specified board.
    For instance, if board = createBoard(6), getNumBlocks(board) should
    return 6."""

    blockCount = 0
    for peg in board:
        for block in peg:
            blockCount += 1

    return blockCount
    #print (blockCount)
    
def isTowerComplete(board, pegNo):
    """Returns True if all of the blocks on the board are on the specified
    peg, in proper order."""

    if len(board[pegNo - 1]) == getNumBlocks(board):
        return True
    else:
        return False
    
def isGameComplete(board,pegNo):
    """Returns True if the goal of the game has been satisfied (ie,
    all of the blocks have been moved to their proper destination),
    where pegNo is the proper destination.   
       Hint: you can do this in one line of code!
       Note: pegNo was added as a parameter 10/28"""

    if isTowerComplete(board,pegNo):
        return True
    """gameComplete = isTowerComplete(board,pegNo)
    if gameComplete == True:
        return True"""

def isValidMove(board, fromPeg, toPeg):
    """fromPeg and toPeg are the indices of the respective pegs.
    Returns True if the fromPeg and the toPeg are on the board,
    the fromPeg has a piece to move, and the piece being moved
    is smaller than (less than) the piece (if any) on the toPeg."""

    try:
        fromPegArray = board[fromPeg]
        toPegArray = board[toPeg]
    except IndexError:
        return False

    if len(fromPegArray) == 0:
        return False
    if len(toPegArray) > 0:
        if fromPegArray[0] > toPegArray[0]:
            return False
    return True

def makeMove(board, fromPeg, toPeg):
    """Changes and returns the board after moving the smallest block
    from the top of fromPeg to the top of toPeg. This function will
    only be used on valid moves (ie, isValidMove(board, fromPeg, toPeg)
    returns True), so you do not need to perform additional checks."""

    board[toPeg].insert(0, board[fromPeg][0])
    board[fromPeg].remove(board[fromPeg][0])

    return board
    
def inputInt(prompt):
    """Asks the user to give input with the given prompt until the
    user has entered an integer. Hint: use try and except to
    test if the input can be converted to an integer."""
    validInput = False
    userInput = input(prompt)

    while not validInput:
        try:
            userInput = int(userInput)
            return userInput
            validInput = True
        except ValueError:
            print('Input must be an integer!')
            userInput = input(prompt)
    
def main():
    board = createBoard(3)
    while not isGameComplete(board,3):
        printBoard(board)
        fromPeg = inputInt("From which peg? ")
        toPeg = inputInt("To which peg? ")
        while not isValidMove(board, fromPeg, toPeg):
            print("INVALID MOVE! Try again!")
            fromPeg = inputInt("From which peg? ")
            toPeg = inputInt("To which peg? ")
        board = makeMove(board, fromPeg, toPeg)
    printBoard(board)
    print("CONGRATULATIONS!")

def printBoard(board):
    nb = max([b for p in board for b in p])
    formatStr = "%ds" % nb
    print("+", "=" * ((2 + nb) * len(board) + len(board) - 1), \
          "+", sep="")
    print("|", end="")
    for pegNo in range(len(board)):
        print(" ", format(str(pegNo), formatStr), sep="", end = " |")
    print("\n", end="")
    print("+", "=" * ((2 + nb) * len(board) + len(board) - 1), \
          "+", sep="")
    for rowNo in range(nb):
        print("|", end = '')
        for peg in board:
            if nb - len(peg) <= rowNo:
                print(" ", format(str(peg[rowNo - nb + len(peg)]) * peg[rowNo - nb + len(peg)], formatStr), sep="", end = ' |')
            else:
                print(" ", format("0" * 0, formatStr), sep="", end = ' |')
        print("\n", end = '')
    print("+", "-" * ((2 + nb) * len(board) + len(board) - 1), \
          "+", sep="")
        
main()
