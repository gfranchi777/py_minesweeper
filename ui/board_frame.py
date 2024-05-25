from py_minesweeper.resources.enums import UiData
from py_minesweeper.game_engine.minesweeper_board import MinesweeperBoard

import customtkinter as ctk

class BoardFrame(ctk.CTkFrame):
    def __init__(self, board: MinesweeperBoard, master, **kwargs) -> None:
        super().__init__(master, **kwargs)

        self._button_height = 40
        self._button_width = 40

        self.create_board_ui(board)

    def create_board_ui(self, board: MinesweeperBoard) -> None:
        for row in range(board.width):
            for col in range(board.length):
                button = ctk.CTkButton(self)
                button.configure(width=self._button_width)
                button.configure(height=self._button_height)
                button.configure(text=f"{board.get_value_at([row,col])}")
                button.configure(hover=True)
                button.grid(row=row, column=col, padx=1, pady=1)

