import random
import sys
from enum import Enum

import numpy


class GridTypes(Enum):
    INT = {
        "data_type": int,
        "initial_value": 0
    }
    
    STRING = {
        "data_type": str,
        "initial_value": ''
    }


class Grid:
    def __init__(self, length: int, width: int, grid_type: GridTypes) -> None:
        if self.is_valid_dimension(length, width):
            self._is_initialized = False
            self._length = length
            self._width = width

            self._grid = numpy.full((length, width), grid_type.value["initial_value"], dtype=grid_type.value["data_type"])
        else:
            sys.exit(
                "Invalid Grid Dimensions.\n \
                     Length And Width Must Be Larger Than 0."
            )

    """
    Property Getters / Setters
    """

    @property
    def grid(self) -> object:
        return self._grid

    @grid.setter
    def grid(self, grid: object) -> None:
        self.grid = grid

    @property
    def length(self) -> int:
        return self._length

    @length.setter
    def length(self, length: int) -> None:
        self.length = length

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, width: int) -> None:
        self.width = width

    @property
    def is_initialized(self) -> bool:
        return self._is_initialized

    @is_initialized.setter
    def is_initialized(self, is_intialized: bool) -> None:
        self.is_initialized = is_intialized

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
            value_at_index = self._grid[row_col_position[0]][row_col_position[1]]

        return value_at_index

    def set_value_at(self, row_col_position: list[int], value: int) -> None:
        if self.is_valid_position(row_col_position):
            self._grid[row_col_position[0], row_col_position[1]] = value

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

        if (
            self.min_horizontal_boundary
            <= row_col_position[0]
            <= self.max_horizontal_boundary
        ) and (
            self.min_vertical_boundary
            <= row_col_position[1]
            <= self.max_vertical_boundary
        ):
            is_valid_position = True

        return is_valid_position

    def gen_random_coordinate(self, num_coords: int) -> list[int]:
        random_coords = []

        for _ in range(num_coords):
            random_coords.insert(
                random.randint(
                    self.min_horizontal_boundary, self.max_horizontal_boundary
                ),
                random.randint(
                    self.min_horizontal_boundary, self.max_horizontal_boundary
                ),
            )

        return random_coords

    def reset_values(self) -> None:
        for row, row_val in enumerate(self._grid):
            for col in row_val:
                self._grid[row][row_val[col]] = 0

    def print_coordinates(self) -> None:
        padding = len(
            str(max(self.max_horizontal_boundary, self.max_vertical_boundary))
        )

        for row, row_val in enumerate(self._grid):
            for col_val in row_val:
                print(f"[{row:0{padding}},{col_val:0{padding}}] ", end="")
            print()
        print()

    def print_values(self, values: list[list[int]], no_new_line: bool = True) -> None:
        if len(values) > 0:
            print(f"{values[0]}", end="")

            if len(values) > 1:
                if no_new_line:
                    print(" ", end="")
                else:
                    print()
            else:
                print("\n")

            self.print_values(values[1:], no_new_line)
