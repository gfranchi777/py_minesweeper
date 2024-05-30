from resources.enums import GameModes
from model.minesweeper_model import MinesweeperModel
from view.board_frame import BoardFrame
from view.root_window import RootWindow
from view.game_controls_frame import GameControlsFrame

import customtkinter

def main() -> None:
    board = MinesweeperModel(GameModes.CLASSIC)

    root_window = RootWindow()

    game_controls_frame = GameControlsFrame(master=root_window)

    board_frame = BoardFrame(master=root_window, board=board)

    root_window.mainloop()

if __name__ == '__main__':
    main()

