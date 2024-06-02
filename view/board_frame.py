'''
Module: board_frame

This module contains the BoardFrame class, which is responsible for creating and managing the
user interface for the Minesweeper game board using customtkinter.
'''

import customtkinter as ctk
from py_minesweeper.model.enums import CoordinateModifiers
from py_minesweeper.model.minesweeper_model import MinesweeperModel

class BoardFrame(ctk.CTkFrame):
    '''
    BoardFrame class creates and manages the Minesweeper game board UI.

    This class handles the creation of the game board UI, activating and deactivating buttons,
    revealing squares, and managing the game over state.
    '''
    def __init__(self, board: MinesweeperModel, master, **kwargs) -> None:
        '''
        Initialize the BoardFrame.

        Args:
            board (MinesweeperModel): The MinesweeperModel instance representing the game board.
            master: The parent widget.
            **kwargs: Additional keyword arguments for the CTkFrame.
        '''
        super().__init__(master, **kwargs)

        self._button_length = 40
        self._button_width = 40

        self._board = board

        self._coord_mods = CoordinateModifiers.COORD_MODS.value

        self.buttons = [[None for _ in range(self._board.length)] for _ in range(self._board.width)]

        self.pack(side="top", pady=0, padx=0, fill="both")

        self.create_board_ui()

    def activate_button(self, button: ctk.CTkButton, row: int, col: int) -> None:
        '''
        Activate a button on the game board.

        Args:
            button (ctk.CTkButton): The button to activate.
            row (int): The row position of the button.
            col (int): The column position of the button.
        '''
        button.configure(width=self._button_width)
        button.configure(height=self._button_length)
        button.configure(text="")
        button.configure(hover=True)
        button.configure(state="enabled")
        button.configure(command=lambda r=row, c=col: self.reveal_square_value(r,c))
        button.grid(row=row, column=col, padx=1, pady=1)

        self.buttons[row][col] = button

    def create_board_ui(self) -> None:
        '''
        Create the game board user interface.

        This method initializes the game board by creating and activating buttons for each cell.
        '''
        for row in range(self._board.width):
            for col in range(self._board.length):
                button = ctk.CTkButton(self)
                self.activate_button(button, row, col)

    def disable_button(self, row: int, col: int, clear_text: bool = False) -> None:
        '''
        Disable a button on the game board.

        Args:
            row (int): The row position of the button.
            col (int): The column position of the button.
            clear_text (bool): Whether to clear the button's text. Defaults to False.
        '''
        if clear_text:
            self.buttons[row][col].configure(text="")

        self.buttons[row][col].configure(state="disabled")
        self.buttons[row][col].configure(fg_color="#424949")
        self.buttons[row][col].configure(text_color_disabled="#f1c40f")

    def game_over(self) -> None:
        '''
        Handle the game over state.

        This method disables all buttons and displays "GAME OVER" in the middle of the board.
        '''
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

    def reveal_adjacent_blanks(self, coords: list[list[int]]) -> None:
        '''
        Reveal adjacent blank squares recursively.

        Args:
            coords (list[list[int]]): The coordinates of the blank square to reveal.
        '''
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
        '''
        Reveal the value of a square on the game board.

        Args:
            row (int): The row position of the square.
            col (int): The column position of the square.
        '''
        match self._board.get_value_at([row, col]):
            case 0:
                self.reveal_adjacent_blanks([row, col])
            case 9:
                self.game_over()
            case _:
                self.buttons[row][col].configure(text=f"{self._board.get_value_at([row,col])}")
                self.disable_button(row, col)
