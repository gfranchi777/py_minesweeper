from py_minesweeper.resources.enums import UiData
from py_minesweeper.game_engine.minesweeper_board import MinesweeperBoard

import customtkinter as ctk

class BoardFrame(ctk.CTkFrame):
    def __init__(self, board: MinesweeperBoard, master, **kwargs) -> None:
        super().__init__(master, **kwargs)

        self._button_height = 40
        self._button_width = 40
        
        self._board = board

        self.pack(side="top", pady=0, padx=0, fill="both")

        self.create_board_ui()

    def create_board_ui(self) -> None:
        for row in range(self._board.width):
            for col in range(self._board.length):
                button = ctk.CTkButton(self)
                button.configure(width=self._button_width)
                button.configure(height=self._button_height)
                button.configure(text=f"")
                button.configure(hover=True)
                button.configure(command=lambda b=button, r=row, c=col: self.reveal_square_value(b,r,c))
                button.grid(row=row, column=col, padx=1, pady=1)

    def reveal_square_value(self, button : ctk.CTkButton, row : int, col : int) -> None:
        button.configure(text=f"{self._board.get_value_at([row,col])}")
        button.configure(state="disabled")
