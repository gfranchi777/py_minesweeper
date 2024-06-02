'''
Module: controller

This module contains the controller for the Minesweeper game, which coordinates
the interactions between the model and the view components. It initializes the game,
handles user interactions, and starts the main application loop.

Attributes:
    None
'''
import platform

from py_minesweeper.model.minesweeper_model import MinesweeperModel
from py_minesweeper.view.board_frame import BoardFrame
from py_minesweeper.view.root_window import RootWindow
from py_minesweeper.view.game_controls_frame import GameControlsFrame
from py_minesweeper.model.enums import GameModes

class MinesweeperController:
    '''
    MinesweeperController is responsible for managing the Minesweeper game.

    This class initializes the game model and view components, handles user interactions
    such as left and right clicks, and runs the main application loop.

    Attributes:
        board (MinesweeperModel): The game model representing the Minesweeper board.
        root_window (RootWindow): The main application window.
        game_controls_frame (GameControlsFrame): The frame containing game control buttons.
        board_frame (BoardFrame): The frame displaying the Minesweeper board.
    '''

    def __init__(self):
        '''
        Initializes the MinesweeperController with game mode, root window, game controls frame,
        and board frame.
        '''
        self.board = MinesweeperModel(GameModes.CLASSIC)

        self.root_window = RootWindow()
        self.game_controls_frame = GameControlsFrame(master=self.root_window)
        self.board_frame = BoardFrame(master=self.root_window, board=self.board)

        self.bind_mouse_clicks()

    def bind_mouse_clicks(self) -> None:
        '''
        Bind mouse click events to their respective handlers based on the operating system.
        '''
        self.root_window.bind("<Button-1>", self.on_left_click)

        if platform.system() == "Darwin":
            self.root_window.bind("<Button-2>", self.on_right_click)
        else:
            self.root_window.bind("<Button-3>", self.on_right_click)

    def on_right_click(self, event):
        '''
        Handles the right-click event on the Minesweeper board.

        This method processes the right-click action performed by the user,
        used for flagging a cell as containing a mine.
        '''

    def on_left_click(self, event):
        '''
        Handles the left-click event on the Minesweeper board.

        This method processes the left-click action performed by the user,
        typically used for revealing a cell on the Minesweeper board.
        '''

    def run(self):
        '''
        Runs the main application loop.

        This method starts the Tkinter main loop, which keeps the application running
        and responsive to user interactions.
        '''
        self.root_window.mainloop()
