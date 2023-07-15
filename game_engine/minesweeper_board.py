"""
Module: minesweeper_board
"""
from minesweeper.game_engine.enums import CoordinateModifiers
from minesweeper.game_engine.enums import GameModes
from python_utils.math_utils.grid.int_grid import IntGrid

class MinesweeperBoard(IntGrid):
    """
    Class: MinesweeperBoard
    """
    MINE_SQUARE_VALUE = 9

    def __init__(self, game_mode: GameModes) -> None:    
        self._blanks_coords = []
        self._mine_coords = []

        super().__init__(game_mode.value['board_length'], game_mode.value['board_width'])

        self.new_game(game_mode)

    @property
    def mine_coords(self) -> list[list[int]]:
        """
        Property: mine_coords
        """
        return self._mine_coords

    @property
    def blank_coords(self) -> list[list[int]]:
        """
        Property: blank_coords
        """
        return self._blanks_coords

    @property
    def coord_mods(self) -> list[list[int]]:
        """
        Property: coord_mods
        """
        return CoordinateModifiers.COORD_MODS.value

    def is_not_mine(self, coords: list[int]) -> bool:
        """
        Function: is_not_mine
        """
        is_mine = True

        if self.get_value_at(coords) == self.MINE_SQUARE_VALUE:
            is_mine = False

        return is_mine

    def place_mines(self, num_mines) -> None:
        """
        Function: place_mines
        """
        num_mines_placed = 0

        while num_mines_placed != num_mines:
            random_coords = self.gen_random_coordinate(2)

            if self.is_not_mine(random_coords):
                self.mine_coords.append(random_coords)
                self.set_value_at(random_coords, self.MINE_SQUARE_VALUE)

                num_mines_placed += 1

        self.mine_coords.sort()

    def calc_mine_adj_values(self) -> None:
        """
        Function: calc_mine_adj_values
        """
        for mine_coord in self.mine_coords:
            for coord_mod in self.coord_mods:
                adj_coord = [(mine_coord[0] + coord_mod[0]),
                             (mine_coord[1] + coord_mod[1])]

                if self.is_valid_position(adj_coord):
                    if self.is_not_mine(adj_coord):
                        self.set_value_at(adj_coord, 
                                          self.get_value_at(adj_coord) + 1)

    def discover_blanks(self) -> None:
        """
        Function: discover_blanks
        """
        for row_index, row_val in enumerate(self.grid):
            for col_index, col_val in enumerate(row_val):
                if col_val == self.type.value["initial_value"]:
                    self.blank_coords.append([row_index, col_index])

        self.blank_coords.sort()

    def expose_adj_blanks(self) -> None:
        """
        Function: expose_adj_blanks
        """

    def new_game(self, game_mode: GameModes) -> None:
        """
        Function: new_game
        """
        self.place_mines(game_mode.value['num_mines'])
        self.calc_mine_adj_values()
        self.discover_blanks()
