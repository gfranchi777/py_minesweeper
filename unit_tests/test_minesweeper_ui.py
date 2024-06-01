'''
Module: test_minesweeper_ui

This module initializes a Minesweeper game, prints the game board, and starts the game controller.

Functions:
    main() -> None
'''

from py_minesweeper.controller.controller import MinesweeperController

def main() -> None:
    '''
    Initializes a Minesweeper game, prints the game board, and starts the game controller.

    This function creates an instance of MinesweeperController, prints the initial values 
    of the game board, and starts the game controller.

    Parameters:
        None

    Returns:
        None
    '''
    controller = MinesweeperController()
    controller.board.print_values(controller.board.grid, False)

    for row in range(controller.board.width):
        for col in range(controller.board.length):
            controller.board_frame.buttons[row][col].configure(
                text=f"{controller.board.get_value_at([row, col])}")

    controller.run()

if __name__ == "__main__":
    main()
