from py_minesweeper.resources.enums import UiData
from py_minesweeper.resources.enums import CoordinateModifiers
from py_minesweeper.model.minesweeper_model import MinesweeperModel

import customtkinter as ctk
import time

class BoardFrame(ctk.CTkFrame):
    def __init__(self, board: MinesweeperModel, master, **kwargs) -> None:
        super().__init__(master, **kwargs)

        self._button_length = 40
        self._button_width = 40
        
        self._board = board
        
        self._coord_mods = CoordinateModifiers.COORD_MODS.value

        self.buttons = [[None for _ in range(self._board.length)] for _ in range(self._board.width)]
        
        self.pack(side="top", pady=0, padx=0, fill="both")

        self.create_board_ui()

    def create_board_ui(self) -> None:
        for row in range(self._board.width):
            for col in range(self._board.length):
                button = ctk.CTkButton(self)
                button.configure(width=self._button_width)
                button.configure(height=self._button_length)
                button.configure(text=f"")
                button.configure(hover=True)
                button.configure(state="enabled")
                button.configure(command=lambda r=row, c=col: self.reveal_square_value(r,c))
                button.grid(row=row, column=col, padx=1, pady=1)
                
                self.buttons[row][col] = button

    def reveal_adjacent_blanks(self, coords: list[list[int]]) -> None:
        if not self._board.is_valid_position(coords):
            return

        if self.buttons[coords[0]][coords[1]].cget("state") == 'disabled':
            return
        
        if self._board.get_value_at([coords[0], coords[1]]) != 0:
            return

        self.disable_button(coords[0], coords[1], True)

        for cmod_x, cmod_y in self._coord_mods:
            self.reveal_adjacent_blanks([coords[0] + cmod_x, coords[1] + cmod_y])

    def reveal_square_value(self, row: int, col: int) -> None:        
        match self._board.get_value_at([row, col]):
            case 0:
                self.reveal_adjacent_blanks([row, col])
            case 9:
                self.game_over()
            case _:
                self.buttons[row][col].configure(text=f"{self._board.get_value_at([row,col])}")
                self.disable_button(row, col)
    
    def activate_board(self) -> None:
        pass

    def disable_button(self, row: int, col: int, clear_text: bool = False) -> None:
        if clear_text:
            self.buttons[row][col].configure(text="")

        self.buttons[row][col].configure(state="disabled")
        self.buttons[row][col].configure(fg_color="#424949")
        self.buttons[row][col].configure(text_color_disabled="#f1c40f")

    def game_over(self) -> None:
        mid_row = int(self._board.width / 2) - 1
        mid_col = int(self._board.length / 2)

        for row in range(self._board.width):
            for col in range(self._board.length):
                self.disable_button(row, col, True)

        self.buttons[mid_row][mid_col - 2].configure(text="G")
        self.buttons[mid_row][mid_col - 1].configure(text="A")
        self.buttons[mid_row][mid_col].configure(text="M")
        self.buttons[mid_row][mid_col + 1].configure(text="E")

        self.buttons[mid_row + 1][mid_col - 2].configure(text="O")
        self.buttons[mid_row + 1][mid_col - 1].configure(text="V")
        self.buttons[mid_row + 1][mid_col].configure(text="E")
        self.buttons[mid_row + 1][mid_col + 1].configure(text="R")
