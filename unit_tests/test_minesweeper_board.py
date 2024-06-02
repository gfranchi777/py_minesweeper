'''
Module: test_minesweeper_board

This module initializes a Minesweeper game with the classic game mode and prints the game board.

Functions:
    main() -> None
'''

from py_minesweeper.model.minesweeper_model import MinesweeperModel
from py_minesweeper.model.enums import GameModes


def main() -> None:
    '''
    Initializes a Minesweeper game with the classic game mode and prints the game board.

    This function creates an instance of MinesweeperModel with the classic game mode and 
    prints the initial values of the game board.

    Parameters:
        None

    Returns:
        None
    '''
    board = MinesweeperModel(GameModes.CLASSIC)

    board.print_values(board.grid, False)

if __name__ == "__main__":
    main()
