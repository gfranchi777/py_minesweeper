import customtkinter as ctk

class RootWindow(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()

        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("dark-blue")
        
        self.resizable(True, True)
        self.title("Minesweeper")

