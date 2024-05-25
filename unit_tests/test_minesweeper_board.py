"""
Module: test_minesweepe_board
"""
from py_minesweeper.resources.enums import GameModes
from py_minesweeper.game_engine.minesweeper_board import MinesweeperBoard
from py_minesweeper.ui.board_frame import BoardFrame

import customtkinter

def main() -> None:
    """Run test cases for the MiesweeperBoard class
    
    Args:
        None

    Returns:
        None
    """
    game_mode = GameModes.MEDIUM

    board = MinesweeperBoard(game_mode)

    customtkinter.set_appearance_mode("system")
    customtkinter.set_default_color_theme("dark-blue")

    app = customtkinter.CTk()
    app.geometry("400x400")
    app.title("Minesweeper")

    board_frame = BoardFrame(board=board, master=app)
    board_frame.pack(pady=0, padx=0, fill="both", expand=True)

    app.mainloop()

if __name__ == '__main__':
    main()

