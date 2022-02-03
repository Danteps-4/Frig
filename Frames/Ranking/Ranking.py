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

        # Combobox variable
        self._selected = tk.StringVar()

    def ranking_components(self):
        # Order the users by
        order_by_label = ttk.Label(self._ranking_frame, text="Order by:", font=("Arial", 12))
        order_by_label.pack()

        self.order_by_combobox = ttk.Combobox(self._ranking_frame, state="readonly", textvariable=self._selected)
        self.order_by_combobox["values"] = ("ID", "Games played", "Wins", "Losses", "Wins Percentage")
        self.order_by_combobox.pack(pady=5)
        self.order_by_combobox.bind('<<ComboboxSelected>>', self._get_users_data)

        # Create a table
        self.treeview = ttk.Treeview(self._ranking_frame, columns=(1, 2, 3, 4, 5, 6), show="headings", height=24)
        self.treeview.pack()
        self.treeview.heading(1, text="ID")
        self.treeview.heading(2, text="Username")
        self.treeview.heading(3, text="Games played")
        self.treeview.heading(4, text="Wins")
        self.treeview.heading(5, text="Losses")
        self.treeview.heading(6, text="Wins %")
        self.treeview.column(1, minwidth=50, width=100, anchor=tk.CENTER)
        self.treeview.column(2, minwidth=50, width=100, anchor=tk.CENTER)
        self.treeview.column(3, minwidth=50, width=100, anchor=tk.CENTER)
        self.treeview.column(4, minwidth=50, width=100, anchor=tk.CENTER)
        self.treeview.column(5, minwidth=50, width=100, anchor=tk.CENTER)

    def _get_users_data(self, selected):
        selected = self._selected.get()
        users = None

        # Clear the data in the table
        for i in self.treeview.get_children():
            self.treeview.delete(i)

        if selected == "ID":
            users = UserDAO.select_all("SELECT * FROM usuarios ORDER BY id_user")
        elif selected == "Games played":
            users = UserDAO.select_all("SELECT * FROM usuarios ORDER BY games_played DESC")
        elif selected == "Wins":
            users = UserDAO.select_all("SELECT * FROM usuarios ORDER BY win_games DESC")
        elif selected == "Losses":
            users = UserDAO.select_all("SELECT * FROM usuarios ORDER BY lost_games DESC")
        elif selected == "Wins Percentage":
            users = UserDAO.select_all("SELECT * FROM usuarios ORDER BY wins_percentage DESC")

        # Insert the data in the table
        for user in users:
            self.treeview.insert("", tk.END, values=(user.id_user, user.username, user.games_played, user.win_games, user.lost_games, user.wins_percentage))