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

    def bind_mouse_clicks(self, left_click_handler, right_click_handler) -> None:
        '''
        Bind left and right mouse click events to their handlers.

        Parameters:
        left_click_handler (function): The handler function for left mouse clicks.
        right_click_handler (function): The handler function for right mouse clicks.
        '''
        self.bind("<Button-1>", left_click_handler)
        self.bind("<Button-2>", right_click_handler)
        self.bind("<Button-3>", right_click_handler)