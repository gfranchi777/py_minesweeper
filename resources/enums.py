'''
Module: enums

This module defines various enumerations used in the Minesweeper game, including coordinate
modifiers, game modes, and UI data.

Classes:
    CoordinateModifiers: Enumeration for coordinate modifiers around a cell.
    GameModes: Enumeration for different game modes with specific board sizes and mine counts.
    UiData: Enumeration for UI-related data.
'''
from enum import Enum

class CoordinateModifiers(Enum):
    '''
    CoordinateModifiers enumeration provides the coordinate modifiers for adjacent cells.

    This enumeration defines the relative positions of the adjacent cells in an 8-directional
    grid layout around a given cell.
    '''
    COORD_MODS = [
        [-1, -1], # Above To The Left
        [-1, 0],  # Above
        [-1, 1],  # Above To The Right
        [0, -1],  # Left
        [0, 1],   # Right
        [1, -1],  # Under To The Left
        [1, 0],   # Under
        [1, 1]    # Under To The Right
    ]

class GameModes(Enum):
    '''
    GameModes enumeration defines the different game modes for Minesweeper.

    Each game mode specifies the dimensions of the game board and the number of mines.

    Attributes:
        CLASSIC (dict): Classic game mode with an 8x8 board and 9 mines.
        EASY (dict): Easy game mode with a 9x9 board and 12 mines.
        MEDIUM (dict): Medium game mode with a 16x16 board and 15 mines.
        HARD (dict): Hard game mode with a 30x16 board and 50 mines.
    '''
    CLASSIC = {
        "board_length": 8, 
        "board_width": 8,
        "num_mines": 9
    }

    EASY = {
        "board_length": 9, 
        "board_width": 9,
        "num_mines": 12
    }

    MEDIUM = {
        "board_length": 16, 
        "board_width": 16,
        "num_mines": 15
    }

    HARD = {
        "board_length": 30, 
        "board_width": 16,
        "num_mines": 50
    }

class UiData(Enum):
    '''
    UiData enumeration defines UI-related data for the Minesweeper game.

    This enumeration includes the background colors for enabled and disabled states of buttons,
    and the text color for UI elements.

    Attributes:
        BUTTON (dict): Contains background colors for enabled and disabled states, and text color.
    '''
    BUTTON = {
        "bgcolor_disabled": "",
        "bgcolor_enabled": "",
        "text_color": ""
    }
