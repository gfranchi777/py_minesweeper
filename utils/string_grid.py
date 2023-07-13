from .grid import Grid
from .grid import GridTypes

class StringGrid(Grid):
    def __init__(self, length: int, width: int) -> None:
        self._grid_type = GridTypes.STRING
        
        super().__init__(length, width, self._grid_type)

    @property
    def grid_type(self) -> type:
        return self._grid_type
    
    @property
    def initial_value(self) -> int:
        return self._grid_type.value["initial_value"]