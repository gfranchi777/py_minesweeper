'''
Module: test_minesweeper_ui

This module initializes a Minesweeper game with the classic game mode, prints the game board,
and starts the game controller.

Functions:
    main() -> None
'''

from py_minesweeper.controller.controller import MinesweeperController
from py_minesweeper.model.minesweeper_model import MinesweeperModel
from py_minesweeper.resources.enums import GameModes


def main() -> None:
    '''
    Initializes a Minesweeper game with the classic game mode, prints the game board, 
    and starts the game controller.

    This function creates an instance of MinesweeperModel with the classic game mode, 
    prints the initial values of the game board, creates an instance of MinesweeperController, 
    and starts the game controller.

    Parameters:
        None

    Returns:
        None
    '''
    board = MinesweeperModel(GameModes.CLASSIC)
    board.print_values(board.grid, False)

    controller = MinesweeperController()
    controller.run()

if __name__ == "__main__":
    main()
