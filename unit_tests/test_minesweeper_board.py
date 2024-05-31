'''
Module: test_minesweeper_board

This module contains a test script for the Minesweeper game. It sets up the game board,
root window, game controls frame, and board frame to test the functionality of the 
MinesweeperModel class.

Functions:
    main: Runs the test cases for the MinesweeperModel class.
'''

from py_minesweeper.resources.enums import GameModes
from py_minesweeper.model.minesweeper_model import MinesweeperModel
from py_minesweeper.view.board_frame import BoardFrame
from py_minesweeper.view.root_window import RootWindow
from py_minesweeper.view.game_controls_frame import GameControlsFrame

def main() -> None:
    '''
    Run test cases for the MinesweeperModel class.

    This function sets up a medium game mode Minesweeper board, initializes the root window,
    game controls frame, and board frame, and starts the Tkinter main loop.

    Args:
        None

    Returns:
        None
    '''
    board = MinesweeperModel(GameModes.MEDIUM)

    root_window = RootWindow()

    _ = GameControlsFrame(master=root_window)

    _ = BoardFrame(master=root_window, board=board)

    root_window.mainloop()

if __name__ == '__main__':
    main()
