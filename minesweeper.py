"""
Module: minesweeper

This module contains the entry point for the Minesweeper game. It initializes the 
MinesweeperController and starts the game.
"""

from controller.controller import MinesweeperController

def main() -> None:
    """
    Initialize and run the Minesweeper game.

    This function creates an instance of MinesweeperController and starts the game's main loop.

    Args:
        None

    Returns:
        None
    """
    controller = MinesweeperController()
    controller.run()

if __name__ == '__main__':
    main()
