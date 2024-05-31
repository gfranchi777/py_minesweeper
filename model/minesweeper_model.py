'''
Minesweeper Model Module

This module defines the MinesweeperModel class, which extends the IntGrid class to manage the
state and logic of the Minesweeper game, including mine placement, adjacent mine calculation,
and blank cell discovery.

Classes:
    MinesweeperModel: Manages the Minesweeper game board and game logic.
'''
from py_utils.math_utils.grid.int_grid import IntGrid
from py_minesweeper.resources.enums import CoordinateModifiers
from py_minesweeper.resources.enums import GameModes

class MinesweeperModel(IntGrid):
    '''
    MinesweeperModel manages the Minesweeper game board and game logic.

    This class handles the initialization of the game board, placing of mines, calculation
    of adjacent mine values, and discovery of blank cells.

    Attributes:
        MINE_SQUARE_VALUE (int): The value representing a mine in the game grid.
        _blanks_coords (list[list[int]]): Coordinates of blank cells.
        _mine_coords (list[list[int]]): Coordinates of cells containing mines.
    '''
    MINE_SQUARE_VALUE = 9

    def __init__(self, game_mode: GameModes) -> None:
        '''
        Initializes the MinesweeperModel with the specified game mode.

        Args:
            game_mode (GameModes): The mode of the game, which determines the board dimensions
                                   and number of mines.
        '''
        self._blanks_coords = []
        self._mine_coords = []

        super().__init__(game_mode.value['board_width'], game_mode.value['board_length'])

        self.new_game(game_mode)

    @property
    def mine_coords(self) -> list[list[int]]:
        '''
        Gets the coordinates of the mines on the board.

        Returns:
            list[list[int]]: A list of coordinates where mines are located.
        '''
        return self._mine_coords

    @property
    def blank_coords(self) -> list[list[int]]:
        '''
        Gets the coordinates of the blank cells on the board.

        Returns:
            list[list[int]]: A list of coordinates where blank cells are located.
        '''
        return self._blanks_coords

    @property
    def coord_mods(self) -> list[list[int]]:
        '''
        Gets the coordinate modifiers for adjacent cells.

        Returns:
            list[list[int]]: A list of coordinate modifications for adjacent cells.
        '''
        return CoordinateModifiers.COORD_MODS.value

    def is_not_mine(self, coords: list[int]) -> bool:
        '''
        Checks if the cell at the given coordinates is not a mine.

        Args:
            coords (list[int]): The coordinates to check.

        Returns:
            bool: True if the cell is not a mine, False otherwise.
        '''
        is_mine = True

        if self.get_value_at(coords) == self.MINE_SQUARE_VALUE:
            is_mine = False

        return is_mine

    def place_mines(self, num_mines) -> None:
        '''
        Places the specified number of mines randomly on the board.

        Args:
            num_mines (int): The number of mines to place on the board.
        '''
        num_mines_placed = 0

        while num_mines_placed != num_mines:
            random_coords = self.gen_random_coordinate(2)

            if self.is_not_mine(random_coords):
                self.mine_coords.append(random_coords)
                self.set_value_at(random_coords, self.MINE_SQUARE_VALUE)

                num_mines_placed += 1

        self.mine_coords.sort()

    def calc_mine_adj_values(self) -> None:
        '''
        Calculates the number of adjacent mines for each cell and updates the board accordingly.
        '''
        for mine_coord in self.mine_coords:
            for coord_mod in self.coord_mods:
                adj_coord = [(mine_coord[0] + coord_mod[0]),
                             (mine_coord[1] + coord_mod[1])]

                if self.is_valid_position(adj_coord):
                    if self.is_not_mine(adj_coord):
                        self.set_value_at(adj_coord,
                                          self.get_value_at(adj_coord) + 1)

    def discover_blanks(self) -> None:
        '''
        Discovers and records the coordinates of all blank cells on the board.
        '''
        for row_index, row_val in enumerate(self.grid):
            for col_index, col_val in enumerate(row_val):
                if col_val == self.type.value["initial_value"]:
                    self.blank_coords.append([row_index, col_index])

        self.blank_coords.sort()

    def new_game(self, game_mode: GameModes) -> None:
        '''
        Initializes a new game with the specified game mode.

        This method places mines, calculates adjacent mine values, and discovers blank cells.

        Args:
            game_mode (GameModes): The mode of the game, which determines the board dimensions
                                   and number of mines.
        '''
        self.place_mines(game_mode.value['num_mines'])
        self.calc_mine_adj_values()
        self.discover_blanks()
