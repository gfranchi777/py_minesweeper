"""
Module: test_minesweepe_board
"""
from py_minesweeper.resources.enums import GameModes
from py_minesweeper.game_engine.minesweeper_board import MinesweeperBoard
from py_minesweeper.ui.board_frame import BoardFrame
from py_minesweeper.ui.root_window import RootWindow
from py_minesweeper.ui.game_controls_frame import GameControlsFrame

import customtkinter

def main() -> None:
    """Run test cases for the MiesweeperBoard class
    
    Args:
        None

    Returns:
        None
    """
    board = MinesweeperBoard(GameModes.CLASSIC)

    root_window = RootWindow()

    game_controls_frame = GameControlsFrame(master=root_window)

    board_frame = BoardFrame(master=root_window, board=board)

    root_window.mainloop()

if __name__ == '__main__':
    main()

