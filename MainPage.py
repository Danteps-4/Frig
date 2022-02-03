import tkinter as tk
import webbrowser
from tkinter import ttk, Menu, scrolledtext
import sys
from Frames.Instructions.Instructions import Instructions
from Frames.MyUser.MyUser import MyUser
from widgets.Colors import Colors
from Frames.AboutUs.AboutUs import AboutUs
from Frames.Ranking.Ranking import Ranking
from Frames.Game.Game import Game

class MainPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title("Frig (Rock-Paper-Scissors)")
        self.iconbitmap("images/ico/rock-paper-scissor.ico")
        # self.resizable(0, 0)

        self._create_components()

    def _create_components(self):
        # Notebook pages
        notebook_control = ttk.Notebook(self)

        # Game page (on process)
        game_frame = Game(notebook_control)
        game_frame.game_components()

        # Ranking page (done)
        ranking_frame = Ranking(notebook_control)
        ranking_frame.ranking_components()

        # My user page (partly done)
        user_frame = MyUser(notebook_control)
        user_frame.myuser_components()

        # Instructions page (done)
        instructions_frame = Instructions(notebook_control)
        instructions_frame.instructions_components()

        # About us page (on process)
        about_us_frame = AboutUs(notebook_control)
        about_us_frame.about_us_components()

        # Add notebook to the window
        notebook_control.pack(fill="both", expand=True)


if __name__ == "__main__":
    window = MainPage()
    window.mainloop()
