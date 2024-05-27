from py_minesweeper.resources.enums import UiData
from py_minesweeper.model.minesweeper_model import MinesweeperModel

import customtkinter as ctk

class BoardFrame(ctk.CTkFrame):
    def __init__(self, board: MinesweeperModel, master, **kwargs) -> None:
        super().__init__(master, **kwargs)

        self._button_height = 40
        self._button_width = 40
        
        self._board = board

        self.buttons = [[None for _ in range(self._board.length)] for _ in range(self._board.width)]
        
        self.pack(side="top", pady=0, padx=0, fill="both")

        self.create_board_ui()

    def create_board_ui(self) -> None:
        for row in range(self._board.length):
            for col in range(self._board.width):
                button = ctk.CTkButton(self)
                button.configure(width=self._button_width)
                button.configure(height=self._button_height)
                button.configure(text=f"")
                button.configure(hover=True)
                button.configure(state="enabled")
                button.configure(command=lambda b=button, r=row, c=col: self.reveal_square_value(b,r,c))
                button.grid(row=row, column=col, padx=1, pady=1)
                
                self.buttons[row][col] = button

    def reveal_square_value(self, button : ctk.CTkButton, row : int, col : int) -> None:
        button.configure(text=f"{self._board.get_value_at([row,col])}")
        
        match button.cget("text"):
            case "0":
                button.configure(text="")
            case "9":
                self.game_over()

        button.configure(state="disabled")
        button.configure(fg_color="#424949")
        button.configure(text_color_disabled="#f1c40f")
    
    def activate_board(self) -> None:
        pass

    def game_over(self) -> None:
        mid_row = int(self._board.length / 2) - 1
        mid_col = int(self._board.width / 2)

        for row in range(self._board.width):
            for col in range(self._board.length):
                self.buttons[row][col].configure(state="disabled")
                self.buttons[row][col].configure(fg_color="#424949")
                self.buttons[row][col].configure(text_color_disabled="#f1c40f")

        self.buttons[mid_row][mid_col - 2].configure(text="G")
        self.buttons[mid_row][mid_col - 1].configure(text="A")
        self.buttons[mid_row][mid_col].configure(text="M")
        self.buttons[mid_row][mid_col + 1].configure(text="E")

        self.buttons[mid_row + 1][mid_col - 2].configure(text="O")
        self.buttons[mid_row + 1][mid_col - 1].configure(text="V")
        self.buttons[mid_row + 1][mid_col].configure(text="E")
        self.buttons[mid_row + 1][mid_col + 1].configure(text="R")
