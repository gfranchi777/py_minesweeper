from enum import Enum

import random

import numpy as np


class GridValues(Enum):
    INITIAL_VALUE = 0

class Grid:

    def __init__(self, length: int, width: int) -> None:
        self._initial_value = GridValues.INITIAL_VALUE.value
        self._is_initialized: bool
        self._length = length
        self._width = width

        self.initialize(length, width)

    """
    Property Getters / Setters
    """
    @property
    def grid(self) -> np.ndarray:
        return self._grid

    @grid.setter
    def grid(self, grid: np.ndarray) -> None:
        self._grid = grid

    @property
    def length(self) -> int:
        return self._length

    @length.setter
    def length(self, length: int) -> None:
        self._length = length

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, width: int) -> None:
        self._width = width

    @property
    def initial_value(self) -> None:
        return self._initial_value
    
    @property
    def is_initialized(self) -> bool:
        return self._is_initialized

    @is_initialized.setter
    def is_initialized(self, is_intialized: bool) -> None:
        self._is_initialized = is_intialized

    @property
    def min_horizontal_boundary(self) -> int:
        return self.length - self.length

    @property
    def min_vertical_boundary(self) -> int:
        return 0

    @property
    def max_horizontal_boundary(self) -> int:
        return self.length - 1

    @property
    def max_vertical_boundary(self) -> int:
        return self.width - 1

    @property
    def min_index(self) -> list[int]:
        return [self.min_horizontal_boundary, self.min_vertical_boundary]

    @property
    def max_index(self) -> list[int]:
        return [self.max_horizontal_boundary, self.max_vertical_boundary]

    def get_value_at(self, row_col_position: list[int]) -> int:
        value_at_index = 0

        if self.is_valid_position(row_col_position):
            value_at_index = self.grid[row_col_position[0]][row_col_position[1]]

        return value_at_index

    def set_value_at(self, row_col_position: list[int], value: int) -> None:
        if self.is_valid_position(row_col_position):
            self.grid[row_col_position[0], row_col_position[1]] = value

    """
    Custom Functions
    """
    def is_valid_dimension(self, length: int, width: int) -> bool:
        is_valid_dimension = False

        if length > 0 and width > 0:
            is_valid_dimension = True

        return is_valid_dimension

    def is_valid_position(self, row_col_position: list[int]) -> bool:
        is_valid_position = False

        if (self.min_horizontal_boundary <= row_col_position[0] <= self.max_horizontal_boundary) and \
           (self.min_vertical_boundary <= row_col_position[1] <= self.max_vertical_boundary):
            is_valid_position = True

        return is_valid_position

    def initialize(self, length: int, width: int) -> None:
        self.is_initialized = False

        if self.is_valid_dimension(length, width):
            self.grid = np.full((length, width), GridValues.INITIAL_VALUE.value, dtype = int)

        if self.length > 0:
            self.is_initialized = True

    def gen_random_coordinate(self, num_coords: int) -> list[int]:
        random_coords = []
        
        for index in range(num_coords):
            random_coords.insert(random.randint(self.min_horizontal_boundary, 
                                                self.max_horizontal_boundary),
                                 random.randint(self.min_horizontal_boundary, 
                                                self.max_horizontal_boundary))
                
        return random_coords
        
    def reset_values(self) -> None:
        for row, row_val in enumerate(self.grid):
            for col_val in range(row_val):
                self.set_value_at([row, col_val], GridValues.INITIAL_VALUE.value)

    def print_information(self) -> None:
        pass

    def print_coordinates(self) -> None:
        padding = len(str(max(self.max_horizontal_boundary, self.max_vertical_boundary)))

        for row, row_val in enumerate(self.grid):
            for col_val in range(row_val):
                print(f'[{row:0{padding}},{col_val:0{padding}}] ', end='')
            print()
        print()

    def print_values(self) -> None:
        for row_enum in enumerate(self.grid):
            for col_val in row_enum[1]:
                print(f'{col_val} ', end='')
            print()
        print()
