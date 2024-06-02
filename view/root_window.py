'''
Module: root_window

This module contains the RootWindow class, which is responsible for creating the main window
of the Minesweeper game using customtkinter.
'''

import customtkinter as ctk

class RootWindow(ctk.CTk):
    '''
    RootWindow class creates the main window for the Minesweeper game.

    This class handles the initialization of the main window with specific appearance
    settings and properties.
    '''
    def __init__(self) -> None:
        '''
        Initialize the RootWindow.

        This method sets the appearance mode, color theme, and window properties.
        '''
        super().__init__()

        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("dark-blue")

        self.resizable(True, True)
        self.title("Minesweeper")
