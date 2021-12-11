from tkinter import ttk
import tkinter as tk
from Frig.UserDAO import UserDAO
from Frig.User import User

class MyUser:
    def __init__(self, master):
        self._master = master

        #Create the frame
        self._myuser_frame = ttk.Frame(self._master)

        # Add the frame to the master
        self._master.add(self._myuser_frame, text="My User")


    def myuser_components(self):
        # Get user data
        user_data = self._get_user_data()

        # Username
        label_username = ttk.Label(self._myuser_frame, text="User: ")
        label_username.grid(row=0, column=0)
        username_data = user_data[1]
        username = ttk.Label(self._myuser_frame, text=username_data)
        username.grid(row=0, column=1)

        # Id user
        label_user_id = ttk.Label(self._myuser_frame, text="User ID:")
        label_user_id.grid(row=1, column=0)
        user_id_data = user_data[0]
        user_id = ttk.Label(self._myuser_frame, text=user_id_data)
        user_id.grid(row=1, column=1)

        # Games played
        label_games_played = ttk.Label(self._myuser_frame, text="Games played: ")
        label_games_played.grid(row=2, column=0)
        games_played_data = user_data[3]
        games_played = ttk.Label(self._myuser_frame, text=user_data[3])
        games_played.grid(row=2, column=1)

        # Win games
        label_win_games = ttk.Label(self._myuser_frame, text="Win games: ")
        label_win_games.grid(row=3, column=0)
        win_games_data = user_data[4]
        win_games = ttk.Label(self._myuser_frame, text=user_data[4])
        win_games.grid(row=3, column=1)

        # Lost games
        label_lost_games = ttk.Label(self._myuser_frame, text="Lost games: ")
        label_lost_games.grid(row=4, column=0)
        lost_games_data = user_data[5]
        lost_games = ttk.Label(self._myuser_frame, text=user_data[5])
        lost_games.grid(row=4, column=1)

        # User stats
        label_stats = ttk.Label(self._myuser_frame, text=f"{user_data[1]}'s stats:")
        label_stats.grid(row=5, column=0)

        # Create a table
        treeview = ttk.Treeview(self._myuser_frame, columns=(1,2,3,4,5),show="headings", height="1")
        treeview.grid(row=6, column=0)
        treeview.heading(1, text="Games played")
        treeview.heading(2, text="Wins")
        treeview.heading(3, text="Losts")
        treeview.heading(4, text="Draws")
        treeview.heading(5, text="Wins %")
        treeview.column(1, minwidth=50, width=100, anchor=tk.CENTER)
        treeview.column(2, minwidth=50, width=100, anchor=tk.CENTER)
        treeview.column(3, minwidth=50, width=100, anchor=tk.CENTER)
        treeview.column(4, minwidth=50, width=100, anchor=tk.CENTER)
        treeview.column(5, minwidth=50, width=100, anchor=tk.CENTER)

        # Get the draws
        draws = self._get_draws(games_played_data, win_games_data, lost_games_data)

        # Get the win_percentage
        wins_percentage = self._get_wins_percentage(games_played_data, win_games_data, draws)

        # Insert the data on the treeview
        treeview.insert("", tk.END, values=(games_played_data, win_games_data, lost_games_data, draws, wins_percentage))


    def _get_user_data(self):
        user = User(id_user=1)
        user_data = UserDAO.select_one(user)
        return user_data

    def _get_wins_percentage(self, games_played, win_games, draws):
        wins_percentage = (win_games*100)/(games_played-draws)
        return wins_percentage

    def _get_draws(self, games_played, win_games, lost_games):
        draws = games_played - (win_games + lost_games)
        return draws
