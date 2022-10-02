import random
import sys

from utils.grid import Grid


class MinesweeperBoard(Grid):
    #
    # Variables
    #
    mine_square_value = 9
    mine_coordinates = []
    num_mines: int

    adjacent_coordinates = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

    game_modes = {"CLASSIC": [8, 8, 9],
                  "EASY": [9, 9, 12],
                  "MEDIUM": [16, 16, 15],
                  "HARD": [30, 16, 20]}

    #
    # Functions
    #

    def __init__(self, game_mode: str):
        if self.isValidGameMode(game_mode):
            super().__init__(self.game_modes[game_mode][0], self.game_modes[game_mode][1])
            self.initializeBoard(self.game_modes[game_mode][2])
        else:
            print('[ERROR] MinesweeperBoard.__init__() - Game Mode ' + game_mode + ' Is Invalid.')
            sys.exit(1)

    def getGameModes(self):
        return self.game_modes

    def getMineSquareValue(self):
        return self.mine_square_value

    def getNumMines(self):
        return self.num_mines

    def getMineCoordinates(self):
        return self.mine_coordinates

    def placeMinesOnBoard(self, num_mines):
        if self.isGridInitialized():
            num_mines_placed = 0

            while num_mines_placed != num_mines:
                random_horizontal_mine_position = random.randint(self.getMinHorizontalBoundary(),
                                                                 self.getMaxHorizontalBoundary())

                random_vertical_mine_position = random.randint(self.getMinVerticalBoundary(),
                                                               self.getMaxVerticalBoundary())

                if self.getValueAtIndex([random_horizontal_mine_position, random_vertical_mine_position]) != \
                        self.getMineSquareValue():
                    self.mine_coordinates.insert(num_mines_placed,
                                                 [random_horizontal_mine_position, random_vertical_mine_position])

                    self.setValueAtIndex(self.mine_coordinates[num_mines_placed], self.getMineSquareValue())

                    num_mines_placed += 1

                self.mine_coordinates.sort()

    def calculateBombAdjacentValues(self):
        mine_adjacent_coordinate = []

        for mine_coordinate_index in range(self.getNumMines()):
            mine_coordinate = self.getMineCoordinates()[mine_coordinate_index]

            for adjacent_coordinate_index in range(len(self.adjacent_coordinates)):
                adjacent_coordinate = [(mine_coordinate[0] + self.adjacent_coordinates[adjacent_coordinate_index][0]),
                                       (mine_coordinate[1] + self.adjacent_coordinates[adjacent_coordinate_index][1])]

                if self.isValidGridPosition(adjacent_coordinate):
                    if self.getValueAtIndex(adjacent_coordinate) != self.getMineSquareValue():
                        self.setValueAtIndex(adjacent_coordinate, self.getValueAtIndex(adjacent_coordinate) + 1)

    def initializeBoard(self, num_mines: int):
        if self.isValidNumMines(num_mines):
            self.num_mines = num_mines
            self.placeMinesOnBoard(num_mines)
            self.calculateBombAdjacentValues()

    def isValidGameMode(self, game_mode: str):
        is_valid_game_mode = False

        for key in self.game_modes:
            if game_mode == key:
                is_valid_game_mode = True
                break

        return is_valid_game_mode

    def isValidNumMines(self, num_mines: int):
        is_valid_num_mines = False

        if num_mines < self.getLength() * self.getWidth():
            is_valid_num_mines = True

        return is_valid_num_mines

    def printBoard(self):
        print('Current Board Status:', end='\n\n')

        for row in range(self.getLength()):
            for col in range(self.getWidth()):
                print(str(self.grid[row][col]) + ' ', end='')
            print()
        print()

    def printMineCoordinates(self):
        print('Current Bomb Coordinates:', end='\n\n')

        for mine_coordinate_index in range(self.getNumMines()):
            current_mine_coordinates = self.getMineCoordinates()[mine_coordinate_index]

            print('Element [' + str(current_mine_coordinates[0]) + ',' + str(current_mine_coordinates[1]) +
                  '] Is A Bomb.')
