from createboard import *
from agent import *
from advAgent import *

def main():

    boardDimension = int(input("Enter the dimension of the board: "))

    if boardDimension <= 5:
        print("Board too small")
        exit()

    initial = board(boardDimension)

    mines = int(input("Enter the number of mines: "))

    
    if mines >= boardDimension * boardDimension:
        print("Mine limit exceeded")
        exit()

    minesweeper = minePlacer(mines, initial)

    # printBoard(minesweeper)

    minesweeperHints = hintsCalculator(minesweeper)

    printBoard(minesweeperHints)
    #printAdvBoard(minesweeperHints)

    result, mineHits = search(minesweeperHints, boardDimension)
    #result, mineHits = advSearch(minesweeperHints, boardDimension)

    print('result: ')
    printBoard(result)
    #printAdvBoard(result)

    print()

    # M,m = mineScan(result, boardDimension)

    percent = (mines-mineHits) / mines
    percent *= 100

    print("Found", percent, "percent of mines without hitting a mine")

    # Need to calculate the final score represented by the total number of mines - the mines exploded by the player
    finalscore = mines - mineHits
    print("Final Score:", finalscore, " out of ", mines)

    print('End of program.')

if __name__ == "__main__":
    main()