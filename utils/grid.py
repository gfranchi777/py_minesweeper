class Grid:
    #
    # Variables
    #
    length: int
    width: int

    initial_element_value = 0

    grid = []
    is_initialized: bool

    #
    # Functions
    #
    def __init__(self, length: int, width: int):
        self.initializeGrid(length, width)

    def getGrid(self):
        return self.grid

    def getLength(self):
        return self.length

    def getWidth(self):
        return self.width

    def getInitialElementValue(self):
        return self.initial_element_value

    @staticmethod
    def getMinHorizontalBoundary():
        return 0

    @staticmethod
    def getMinVerticalBoundary():
        return 0

    def getMaxHorizontalBoundary(self):
        return self.length - 1

    def getMaxVerticalBoundary(self):
        return self.width - 1

    def getMinIndex(self):
        return [self.getMinHorizontalBoundary(), self.getMinVerticalBoundary()]
    
    def getMaxIndex(self):
        return [self.getMaxHorizontalBoundary(), self.getMaxVerticalBoundary()]

    def getValueAtIndex(self, row_col_position: []):
        element_at_index = 0

        if self.isValidGridPosition(row_col_position):
            element_at_index = self.grid[row_col_position[0]][row_col_position[1]]

        return element_at_index

    def setValueAtIndex(self, row_col_position: [], val: int):
        if self.isValidGridPosition(row_col_position):
            self.grid[row_col_position[0]][row_col_position[1]] = val

    def isGridInitialized(self):
        return self.is_initialized

    def isValidGridPosition(self, row_col_position: []):
        is_valid_gird_position = False

        if (self.getMinHorizontalBoundary() <= row_col_position[0] <= self.getMaxHorizontalBoundary()) and \
           (self.getMinVerticalBoundary() <= row_col_position[1] <= self.getMaxVerticalBoundary()):
            is_valid_gird_position = True

        return is_valid_gird_position

    def initializeGrid(self, length: int, width: int):
        self.is_initialized = False

        if length != 0 and width != 0:
            self.length = length
            self.width = width

            for row in range(length):
                self.grid.append([])
                for col in range(width):
                    self.grid[row].append(self.initial_element_value)

            self.is_initialized = True

    def resetGridValues(self):
        for row in range(self.getLength()):
            for col in range(self.getWidth()):
                self.grid[row][col] = self.initial_element_value

    def printGrid(self):
        print('Current Grid Coordinates:', end='\n\n')

        for row in range(self.getLength()):
            for col in range(self.getWidth()):
                print('[', end='')

                if row < 10:
                    print('0', end='')

                print(str(row) + ',', end='')

                if col < 10:
                    print('0', end='')

                print(str(col) + '] ', end='')
            print()
        print()
