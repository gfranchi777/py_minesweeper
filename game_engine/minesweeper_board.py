from minesweeper.game_engine.enums import CoordinateModifiers
from minesweeper.game_engine.enums import GameModes
from minesweeper.utils.grid import Grid

class MinesweeperBoard(Grid):
    #
    # Variables
    #
    MINE_SQUARE_VALUE = 9
    
    #
    # Functions
    #

    def __init__(self, game_mode: GameModes) -> None:    
        self._blanks_coords = []
        self._mine_coords = []
        self._game_mode = game_mode
        
        super().__init__(self.game_mode['board_length'], self.game_mode['board_width'])
    
        self.place_mines(self.game_mode['num_mines'])
        self.calc_mine_adj_values()
        self.discover_blanks()

    @property
    def game_mode(self) -> dict:
        return self._game_mode.value
    
    @game_mode.setter
    def game_mode(self, game_mode: GameModes) -> None:
        self.game_mode = game_mode
        
    @property
    def mine_coords(self) -> list[list[int]]:
        return self._mine_coords

    @property
    def blank_coords(self) -> list[list[int]]:
        return self._blanks_coords
    
    @property
    def coord_mods(self) -> list[list[int]]:
        return CoordinateModifiers.COORD_MODS.value
    
    def is_not_mine(self, coords: int) -> bool:
        is_mine = True
        
        if self.get_value_at(coords) == self.MINE_SQUARE_VALUE:
            is_mine = False
        
        return is_mine
    
    def place_mines(self, num_mines):
        num_mines_placed = 0

        while num_mines_placed != num_mines:
            random_coords = self.gen_random_coordinate(2)
                
            if self.is_not_mine(random_coords):
                self.mine_coords.append(random_coords)
                self.set_value_at(random_coords, self.MINE_SQUARE_VALUE)

                num_mines_placed += 1

        self.mine_coords.sort()

    def calc_mine_adj_values(self) -> None:
        for mine_coord in self.mine_coords:
            for coord_mod in self.coord_mods:
                adj_coord = [(mine_coord[0] + coord_mod[0]),
                             (mine_coord[1] + coord_mod[1])]

                if self.is_valid_position(adj_coord):
                    if self.is_not_mine(adj_coord):
                        self.set_value_at(adj_coord, 
                                          self.get_value_at(adj_coord) + 1)

    def discover_blanks(self) -> None:        
        for row_index, row_val in enumerate(self.grid):
            for col_index, col_val in enumerate(row_val):
                if col_val == self.initial_value:
                    self.blank_coords.append([row_index, col_index])
        
        self.blank_coords.sort()
        
    def expose_adj_blanks(self) -> None:
        pass
    
    def reset(self) -> None:
        super().reset_values()
        self.place_mines(self.game_mode['num_mines'])
        self.calc_mine_adj_values()
        
    def print_coord_values(self, coords: list[list[int]]) -> None:
        if coords:
            print(f'{coords[0]}', end='')
            
            if len(coords) > 1:
                print(', ', end='')
            else:
                print()
                
            self.print_coord_values(coords[1:])
