from minesweeper.game_engine.enums import GameModes
from minesweeper.game_engine.minesweeper_board import MinesweeperBoard

def main() -> None:
    game_mode = GameModes.CLASSIC
    
    board = MinesweeperBoard(game_mode)
    print(f'Current Board Status:\n')
    board.print_values()
    
    print(f'Mine Coordinates: ', end='')
    board.print_mine_coords()

    print(f'Blank Coordinates: ', end='')
    board.print_blank_coords()
    
if __name__ == '__main__':
    main()
