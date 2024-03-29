# If for a cell, the total number of safe neighbours - the number of revealed safe neighbours = the # of hidden neighbours, then every hidden is safe
def safeSweep(board, minesweeper, boardLen):

    boardCopy = board

    for i in range(boardLen):
        for j in range(boardLen):
            if str(board[i,j]).isnumeric() and 1 <= board[i,j] <= 8:

                numberHint = board[i,j]

                if i == 0 and j == 0:

                    boardCopy = topLeft(i,j, boardCopy, minesweeper, numberHint)

                elif i == boardLen-1 and j == 0:

                    boardCopy = botLeft(i,j, boardCopy, minesweeper, numberHint)

                elif i == 0 and j == boardLen-1:

                    boardCopy = topRight(i,j, boardCopy, minesweeper, numberHint)

                elif i == boardLen-1 and j == boardLen-1:

                    boardCopy = botRight(i,j, boardCopy, minesweeper, numberHint)

                elif i == 0 and j != 0 and j != boardLen-1:

                    boardCopy = topEdge(i,j, boardCopy, minesweeper, numberHint)

                elif i != 0 and i != boardLen-1 and j == 0:

                    boardCopy = leftEdge(i,j, boardCopy, minesweeper, numberHint)

                elif i != 0 and i != boardLen-1 and j == boardLen-1:

                    boardCopy = rightEdge(i,j, boardCopy, minesweeper, numberHint)

                elif i == boardLen-1 and j != 0 and j != boardLen-1:

                    boardCopy = botEdge(i,j, boardCopy, minesweeper, numberHint)

                else:   

                    boardCopy = middle(i,j, boardCopy, minesweeper, numberHint)

    return boardCopy

###############################################################

def topLeft(i,j, board, answers, hint):

    hiddenCount = 0
    safeCount = 0
    hiddenTuples = []

    topLeftCoords = [(1,1), (1,0), (0,1)]
                    #  SE,    S,     E
    notHintChars = ['M', 'm', '-']

    for x,y in topLeftCoords:
        a, b = i, j # reset to original i,j
        a += x
        b += y
        if board[a, b] == '-':
            hiddenCount += 1
            hiddenTuples.append((a,b))
        if board[a, b] not in notHintChars:
            safeCount += 1

    if ((len(topLeftCoords) - hint) - safeCount) == hiddenCount:
        for i in range(len(hiddenTuples)):
            x = hiddenTuples[i][0]
            y = hiddenTuples[i][1]
            board[x,y] = answers[x,y]

    return board


def topRight(i,j, board, answers, hint):

    hiddenCount = 0
    safeCount = 0
    hiddenTuples = []

    topRightCoords = [(1,-1), (1,0), (0,-1)]
                    #   SW,     S,      W
    notHintChars = ['M', 'm', '-']

    for x,y in topRightCoords:
        a, b = i, j # reset to original i,j
        a += x
        b += y
        if board[a, b] == '-':
            hiddenCount += 1
            hiddenTuples.append((a,b))
        if board[a, b] not in notHintChars:
            safeCount += 1

    if ((len(topRightCoords) - hint) - safeCount) == hiddenCount:
        for i in range(len(hiddenTuples)):
            x = hiddenTuples[i][0]
            y = hiddenTuples[i][1]
            board[x,y] = answers[x,y]

    return board


def botLeft(i,j, board, answers, hint):

    hiddenCount = 0
    safeCount = 0
    hiddenTuples = []

    botLeftCoords = [(-1,1), (-1,0), (0,1)]
                    #   NE,     N,      E
    notHintChars = ['M', 'm', '-']

    for x,y in botLeftCoords:
        a, b = i, j # reset to original i,j
        a += x
        b += y
        if board[a, b] == '-':
            hiddenCount += 1
            hiddenTuples.append((a,b))
        if board[a, b] not in notHintChars:
            safeCount += 1

    if ((len(botLeftCoords) - hint) - safeCount) == hiddenCount:
        for i in range(len(hiddenTuples)):
            x = hiddenTuples[i][0]
            y = hiddenTuples[i][1]
            board[x,y] = answers[x,y]

    return board


def botRight(i,j, board, answers, hint):

    hiddenCount = 0
    safeCount = 0
    hiddenTuples = []

    botRightCoords = [(-1,-1), (-1,0), (0,-1)]
                    #    NW,      N,      W
    notHintChars = ['M', 'm', '-']

    for x,y in botRightCoords:
        a, b = i, j # reset to original i,j
        a += x
        b += y
        if board[a, b] == '-':
            hiddenCount += 1
            hiddenTuples.append((a,b))
        if board[a, b] not in notHintChars:
            safeCount += 1

    if ((len(botRightCoords) - hint) - safeCount) == hiddenCount:
        for i in range(len(hiddenTuples)):
            x = hiddenTuples[i][0]
            y = hiddenTuples[i][1]
            board[x,y] = answers[x,y]

    return board


def topEdge(i,j, board, answers, hint):

    hiddenCount = 0
    safeCount = 0
    hiddenTuples = []

    topEdgeCoords = [(0,-1), (0,1), (1,0), (1,-1), (1,1)]
                    #   W,     E,     S,     SW,    SE
    notHintChars = ['M', 'm', '-']

    for x,y in topEdgeCoords:
        a, b = i, j # reset to original i,j
        a += x
        b += y
        if board[a, b] == '-':
            hiddenCount += 1
            hiddenTuples.append((a,b))
        if board[a, b] not in notHintChars:
            safeCount += 1

    if ((len(topEdgeCoords) - hint) - safeCount) == hiddenCount:
        for i in range(len(hiddenTuples)):
            x = hiddenTuples[i][0]
            y = hiddenTuples[i][1]
            board[x,y] = answers[x,y]

    return board
    

def leftEdge(i,j, board, answers, hint):

    hiddenCount = 0
    safeCount = 0
    hiddenTuples = []

    leftEdgeCoords = [(0,1), (1,0), (1,1), (-1,0), (-1,1)]
                    #   E,     S,    SE,      N      NE
    notHintChars = ['M', 'm', '-']

    for x,y in leftEdgeCoords:
        a, b = i, j # reset to original i,j
        a += x
        b += y
        if board[a, b] == '-':
            hiddenCount += 1
            hiddenTuples.append((a,b))
        if board[a, b] not in notHintChars:
            safeCount += 1

    if ((len(leftEdgeCoords) - hint) - safeCount) == hiddenCount:
        for i in range(len(hiddenTuples)):
            x = hiddenTuples[i][0]
            y = hiddenTuples[i][1]
            board[x,y] = answers[x,y]

    return board


def rightEdge(i,j, board, answers, hint):

    hiddenCount = 0
    safeCount = 0
    hiddenTuples = []

    rightEdgeCoords = [(0,-1), (1,0), (1,-1), (-1,0), (-1,-1)]
                    #   W,      S,     SW,      N,      NW
    notHintChars = ['M', 'm', '-']

    for x,y in rightEdgeCoords:
        a, b = i, j # reset to original i,j
        a += x
        b += y
        if board[a, b] == '-':
            hiddenCount += 1
            hiddenTuples.append((a,b))
        if board[a, b] not in notHintChars:
            safeCount += 1

    if ((len(rightEdgeCoords) - hint) - safeCount) == hiddenCount:
        for i in range(len(hiddenTuples)):
            x = hiddenTuples[i][0]
            y = hiddenTuples[i][1]
            board[x,y] = answers[x,y]

    return board


def botEdge(i,j, board, answers, hint):

    hiddenCount = 0
    safeCount = 0
    hiddenTuples = []

    botEdgeCoords = [(0,-1), (-1,1), (0,1), (-1,0), (-1,-1)]
                    #   W,     NE,     E,     N,      NW
    notHintChars = ['M', 'm', '-']

    for x,y in botEdgeCoords:
        a, b = i, j # reset to original i,j
        a += x
        b += y
        if board[a, b] == '-':
            hiddenCount += 1
            hiddenTuples.append((a,b))
        if board[a, b] not in notHintChars:
            safeCount += 1

    if ((len(botEdgeCoords) - hint) - safeCount) == hiddenCount:
        for i in range(len(hiddenTuples)):
            x = hiddenTuples[i][0]
            y = hiddenTuples[i][1]
            board[x,y] = answers[x,y]

    return board


def middle(i,j, board, answers, hint):

    hiddenCount = 0
    safeCount = 0
    hiddenTuples = []

    midCoords = [(0,-1), (-1,1), (0,1), (-1,0), (-1,-1), (1,0), (1,-1), (1,1)]
                #   W,     NE,     E,     N,      NW      S,     SW,     SE
    notHintChars = ['M', 'm', '-']

    for x,y in midCoords:
        a, b = i, j # reset to original i,j
        a += x
        b += y
        if board[a, b] == '-':
            hiddenCount += 1
            hiddenTuples.append((a,b))
        if board[a, b] not in notHintChars:
            safeCount += 1

    if ((len(midCoords) - hint) - safeCount) == hiddenCount:
        for i in range(len(hiddenTuples)):
            x = hiddenTuples[i][0]
            y = hiddenTuples[i][1]
            board[x,y] = answers[x,y]

    return board
