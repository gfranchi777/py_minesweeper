'''
Module: game_controls_frame

This module contains the GameControlsFrame class, which is responsible for creating and managing the
user interface for the game controls in the Minesweeper game using customtkinter.
'''

from PIL import Image

import customtkinter as ctk

class NewGameInputDialog(ctk.CTkToplevel):
    '''
    Custom input dialog for selecting a new game mode.
    '''
    def __init__(self, master=None) -> None:
        super().__init__(master)
        self.title("New Game Selection")

        self.option_values = ["Classic", "Easy", "Medium", "Hard"]
        self.selected_option = ctk.StringVar(value=self.option_values[0])

        self.label = ctk.CTkLabel(self, text="Select Game Mode:")
        self.label.pack(padx=20, pady=(20, 5))

        self.option_menu = ctk.CTkOptionMenu(self, variable=self.selected_option, values=self.option_values)
        self.option_menu.pack(padx=20, pady=(5, 20))

        self.confirm_button = ctk.CTkButton(self, text="Confirm", command=self.on_confirm)
        self.confirm_button.pack(padx=20, pady=(0, 20))

        self.transient(master)
        self.grab_set()
        self.master.wait_window(self)
        
    def on_confirm(self):
        '''
        Handle the confirm button click.
        '''
        self.result = self.selected_option.get()
        self.destroy()

    def get_selected_option(self):
        '''
        Get the selected game mode option.
        '''
        return self.result

class GameControlsFrame(ctk.CTkFrame):
    '''
    GameControlsFrame class creates and manages the Minesweeper game control UI.

    This class handles the creation of the game mode selection combo box, the new game button,
    and the game timer display.
    '''
    def __init__(self, master, **kwargs) -> None:
        '''
        Initialize the GameControlsFrame.

        Args:
            master: The parent widget.
            **kwargs: Additional keyword arguments for the CTkFrame.
        '''
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.pack(side="top", pady=0, padx=0, fill="both")

        self._seconds = 0
        self._after_id = None

        self.create_new_game_button()
        self.create_remaining_flag_label()
        self.create_game_timer()

    def create_new_game_button(self) -> None:
        '''
        Create the new game button.

        This method initializes the button used to start a new game.
        '''
        self._new_game_button = ctk.CTkButton(self)
        self._new_game_button.configure(width=5)
        self._new_game_button.configure(height=10)
        self._new_game_button.configure(text="New Game")
        self._new_game_button.configure(command=self.start_new_game)

        self._new_game_button.grid(row=0, column=0, pady=10, padx=10, sticky="w")

    def create_remaining_flag_label(self) -> None:
        '''
        a
        '''
        flag_image = ctk.CTkImage(
            light_image=Image.open("./resources/images/bomb.png"),
            dark_image=Image.open("./resources/images/bomb.png"),
            size=(50, 50))

        self._remaining_flag_label = ctk.CTkLabel(self)
        self._remaining_flag_label.configure(image=flag_image)
        self._remaining_flag_label.configure(text="= ?")
        self._remaining_flag_label.configure(compound="left")
        self._remaining_flag_label.configure(font=("Courier New", 20))

        self._remaining_flag_label.grid(row=0, column=1, pady=10, padx=0)

    def create_game_timer(self) -> None:
        '''
        Create the game timer display.

        This method initializes the label used to display the game timer.
        '''
        self._game_timer_label = ctk.CTkLabel(self)
        self._game_timer_label.configure(text="00:00")
        self._game_timer_label.configure(font=("Courier New", 20))

        self._game_timer_label.grid(row=0, column=2, pady=10, padx=10, sticky="e")

    def start_new_game(self) -> None:
        '''
        Start a new game.

        This method resets the game timer and prepares the game for a new session.
        '''
        dialog = NewGameInputDialog(master=self)
        self.wait_window(dialog)
        selected_option = dialog.get_selected_option()
        print(f"Selected Option: {selected_option}")

        self.reset_game_timer()

    def update_flag_label(self, remaining_flags) -> None:
        '''
        a
        '''
        self._remaining_flag_label.configure(text=f" = {remaining_flags}")

    def update_game_timer(self) -> None:
        '''
        Update the game timer.

        This method increments the game timer by one second and updates the display.
        '''
        self._seconds += 1

        mins, secs = divmod(self._seconds, 60)

        self._game_timer_label.configure(text=f"{mins:02}:{secs:02}")

        self._after_id = self.after(1000, self.update_game_timer)

    def reset_game_timer(self) -> None:
        '''
        Reset the game timer.

        This method stops the current timer, resets the timer to zero, and starts it again.
        '''
        if self._after_id:
            self.after_cancel(self._after_id)

        self._seconds = 0

        self._game_timer_label.configure(text="00:00")

        self.update_game_timer()
