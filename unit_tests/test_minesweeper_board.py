"""
Module: test_minesweepe_board
"""
from game_engine.enums import GameModes
from game_engine.minesweeper_board import MinesweeperBoard

class TestMinesweeperBoard:
    def __init__(self) -> None:
        pass
    
    def test_board() -> None:
        """
        Function: test_board
        Parameters: None
        """
        game_mode = GameModes.CLASSIC

        board = MinesweeperBoard(game_mode)

        print('Current Board Status:\n')
        board.print_values(board.grid, False)

        print('Mines : ', end='')
        board.print_values(board.mine_coords)

        print('Blanks: ', end='')
        board.print_values(board.blank_coords)

