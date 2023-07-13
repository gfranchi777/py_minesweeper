"""
Module: enums
"""
from enum import Enum

class GameModes(Enum):
    """
    Class: GameModes
    """
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
        "num_mines": 20
    }

class CoordinateModifiers(Enum):
    """
    Class: CoordinateModifiers
    """
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
    