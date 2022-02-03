import tkinter as tk
from tkinter import ttk
from random import randint
from Frig.UserDAO import UserDAO
from Frig.User import User
from Frig.widgets.Colors import Colors

class Game:
    def __init__(self, master):
        self._master = master

        # Create the frame
        self._game_frame = tk.Frame(self._master)

        # Config the frame
        self._game_frame.columnconfigure(0, weight=1)
        self._game_frame.columnconfigure(1, weight=1)
        self._game_frame.columnconfigure(2, weight=1)


        # Add the frame
        self._master.add(self._game_frame, text="Game")

        self._wins = 0
        self._losses = 0
        self._draws = 0

    def game_components(self):
        # Title
        game_title = tk.Label(self._game_frame, text="Rock Paper Scissors", font=("Arial", 25))
        game_title.grid(row=0, column=1, pady=(5, 0))

        game_subtitle = tk.Label(self._game_frame, text="Make your choice", font=("Arial", 18))
        game_subtitle.grid(row=1, column=1, pady=(10, 40))

        # Buttons
        rock_button = tk.Button(self._game_frame, text="Rock", command= lambda:self._played(0), width=25, height=3, bd=0, cursor="hand2", bg=Colors.GREY, font=("Arial", 12))
        rock_button.grid(row=2, column=0, pady=20)

        paper_button = tk.Button(self._game_frame, text="Paper", command= lambda:self._played(1), width=25, height=3, bd=0, cursor="hand2", bg=Colors.GREY, font=("Arial", 12))
        paper_button.grid(row=2, column=1, pady=20)

        scissors_button = tk.Button(self._game_frame, text="Scissors", command= lambda:self._played(2), width=25, height=3, bd=0, cursor="hand2", bg=Colors.GREY, font=("Arial", 12))
        scissors_button.grid(row=2, column=2, pady=20)


        # Selected
        self.you_selected_label = ttk.Label(self._game_frame, text="You selected:", font=("Arial", 12))
        self.you_selected_label.grid(row=3, column=0)

        self.computer_selected_label = ttk.Label(self._game_frame, text="Computer selected:", font=("Arial", 12))
        self.computer_selected_label.grid(row=3, column=1)

        self.win_label = ttk.Label(self._game_frame, font=("Arial", 18))
        self.win_label.grid(row=4, column=1, pady=25)


        # Scoreboard
        scoreboard_label = ttk.Label(self._game_frame, text="Scoreboard", font=("Arial", 16))
        scoreboard_label.grid(row=5, column=1, pady=(50, 10))

        self.user_wins = ttk.Label(self._game_frame, text="You:", font=("Arial", 12))
        self.user_wins.grid(row=6, column=0, pady=10)

        self.computer_wins = ttk.Label(self._game_frame, text="Computer:", font=("Arial", 12))
        self.computer_wins.grid(row=6, column=1)

        self.draws = ttk.Label(self._game_frame, text="Draws:", font=("Arial", 12))
        self.draws.grid(row=6, column=2)

        # Restart game
        restart_game = ttk.Button(self._game_frame, text="Restart game", command=self._restart_game)
        restart_game.grid(row=7, column=1, pady=(40, 0))

    def _played(self, option):
        computer = randint(0, 2)

        if option == 0:
            self.you_selected_label.config(text="You selected: Rock")
        elif option == 1:
            self.you_selected_label.config(text="You selected: Paper")
        else:
            self.you_selected_label.config(text="You selected: Scissors")

        if computer == 0:
            self.computer_selected_label.config(text="Computer selected: Rock")
        elif option == 1:
            self.computer_selected_label.config(text="Computer selected: Paper")
        else:
            self.computer_selected_label.config(text="Computer selected: Scissors")

        if option == computer:
            self._draws += 1
            self.draws.config(text=f"Draws: {self._draws}")
            self.win_label.config(text="It is a draw!!!")
            self._update_data("draw")
        elif (option == 0 and computer == 1) or (option == 1 and computer == 2) or (option == 2 and computer == 0):
            self._losses += 1
            self.computer_wins.config(text=f"Computer: {self._losses}")
            self.win_label.config(text="Computer wins!!!")
            self._update_data("lost")
        else:
            self._wins += 1
            self.user_wins.config(text=f"You: {self._wins}")
            self.win_label.config(text="You win!!!")
            self._update_data("win")

    def _update_data(self, condition):
        user_data = self._get_user_data()
        if condition == "win":
            user = User(id_user=1, games_played=user_data[3]+1,win_games=user_data[4]+1, lost_games=user_data[5])
            updated = UserDAO.update(user)
        elif condition == "lost":
            user = User(id_user=1, games_played=user_data[3]+1, win_games=user_data[4], lost_games=user_data[5]+1)
            updated = UserDAO.update(user)
        else:
            user = User(id_user=1, games_played=user_data[3]+1, win_games=user_data[4], lost_games=user_data[5])
            updated = UserDAO.update(user)

    def _get_user_data(self):
        user = User(id_user=1)
        user_data = UserDAO.select_one(user)
        return user_data

    def _restart_game(self):
        self.you_selected_label.config(text="You selected:")
        self.computer_selected_label.config(text="Computer selected:")
        self.win_label.config(text="")
        self.user_wins.config(text="You:")
        self.computer_wins.config(text="Computer:")
        self.draws.config(text="Draws:")