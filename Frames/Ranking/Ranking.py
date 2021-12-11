from tkinter import ttk
import tkinter as tk
from Frig.UserDAO import UserDAO

class Ranking:
    def __init__(self, master):
        self._master = master

        # Create the frame
        self._ranking_frame = ttk.Frame(self._master)

        #Add the frame
        self._master.add(self._ranking_frame, text="Ranking")

    def ranking_components(self):
        # Create a table
        treeview = ttk.Treeview(self._ranking_frame, columns=(1, 2, 3, 4, 5, 6), show="headings")
        treeview.pack()
        treeview.heading(1, text="ID")
        treeview.heading(2, text="Username")
        treeview.heading(3, text="Games played")
        treeview.heading(4, text="Wins")
        treeview.heading(5, text="Losts")
        treeview.heading(6, text="Wins %")
        treeview.column(1, minwidth=50, width=100, anchor=tk.CENTER)
        treeview.column(2, minwidth=50, width=100, anchor=tk.CENTER)
        treeview.column(3, minwidth=50, width=100, anchor=tk.CENTER)
        treeview.column(4, minwidth=50, width=100, anchor=tk.CENTER)
        treeview.column(5, minwidth=50, width=100, anchor=tk.CENTER)

        # Get the users
        users = self._get_users_data()

        # Insert the users in the table
        for user in users:
            treeview.insert("", tk.END, values=(user.id_user, user.username, user.games_played, user.win_games, user.lost_games))

    def _get_users_data(self):
        users = UserDAO.select_all()
        return users

    def _get_users_win_percentage(self):
        pass