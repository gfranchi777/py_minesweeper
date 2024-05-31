"""
Module: game_controls_frame

This module contains the GameControlsFrame class, which is responsible for creating and managing the
user interface for the game controls in the Minesweeper game using customtkinter.
"""

import customtkinter as ctk

from py_minesweeper.resources.enums import GameModes

class GameControlsFrame(ctk.CTkFrame):
    """
    GameControlsFrame class creates and manages the Minesweeper game control UI.

    This class handles the creation of the game mode selection combo box, the new game button,
    and the game timer display.
    """
    def __init__(self, master, **kwargs) -> None:
        """
        Initialize the GameControlsFrame.

        Args:
            master: The parent widget.
            **kwargs: Additional keyword arguments for the CTkFrame.
        """
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=1)

        self.pack(side="top", pady=0, padx=0, fill="both")

        self._game_mode_choices = ctk.CTkComboBox(self)
        self._new_game_button = ctk.CTkButton(self)
        self._game_timer_label = ctk.CTkLabel(self)

        self._seconds = 0
        self._after_id = None

        self.create_game_mode_choices()
        self.create_new_game_button()
        self.create_game_timer()

    def create_game_mode_choices(self) -> None:
        """
        Create the game mode selection combo box.

        This method initializes the combo box with the available game modes.
        """
        game_modes = [mode.name.title() for mode in GameModes]

        self._game_mode_choices.configure(width=100)
        self._game_mode_choices.configure(height=10)
        self._game_mode_choices.configure(state="readonly")
        self._game_mode_choices.configure(values=game_modes)
        self._game_mode_choices.set(game_modes[0])

        self._game_mode_choices.grid(row=0, column=0, pady=10, padx=10, sticky="w")

    def create_new_game_button(self) -> None:
        """
        Create the new game button.

        This method initializes the button used to start a new game.
        """
        self._new_game_button.configure(width=5)
        self._new_game_button.configure(height=10)
        self._new_game_button.configure(text="New Game")
        self._new_game_button.configure(command=self.start_new_game)

        self._new_game_button.grid(row=0, column=1, pady=10)

    def create_game_timer(self) -> None:
        """
        Create the game timer display.

        This method initializes the label used to display the game timer.
        """
        self._game_timer_label.configure(text="00:00")
        self._game_timer_label.configure(font=("Courier New", 20))

        self._game_timer_label.grid(row=0, column=2, pady=10, padx=10, sticky="e")

    def start_new_game(self) -> None:
        """
        Start a new game.

        This method resets the game timer and prepares the game for a new session.
        """
        self.reset_game_timer()

    def update_game_timer(self) -> None:
        """
        Update the game timer.

        This method increments the game timer by one second and updates the display.
        """
        self._seconds += 1

        mins, secs = divmod(self._seconds, 60)

        self._game_timer_label.configure(text=f"{mins:02}:{secs:02}")

        self._after_id = self.after(1000, self.update_game_timer)

    def reset_game_timer(self) -> None:
        """
        Reset the game timer.

        This method stops the current timer, resets the timer to zero, and starts it again.
        """
        if self._after_id:
            self.after_cancel(self._after_id)

        self._seconds = 0

        self._game_timer_label.configure(text="00:00")

        self.update_game_timer()
