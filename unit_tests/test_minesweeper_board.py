from utils.MinesweeperBoard import MinesweeperBoard

game_mode = "CLASSIC"

board = MinesweeperBoard(game_mode)

if board.isGridInitialized():
    board.printGrid()
    board.printBoard()
    board.printMineCoordinates()
