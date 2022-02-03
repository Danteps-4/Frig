from tkinter import ttk
import tkinter as tk
from Frig.UserDAO import UserDAO
from Frig.User import User

class MyUser:
    def __init__(self, master):
        self._master = master

        #Create the frame
        self._myuser_frame = tk.Frame(self._master)

        # Add the frame to the master
        self._master.add(self._myuser_frame, text="My User")


    def myuser_components(self):
        # Get user data
        user_data = self._get_user_data()
        self._create_top_frame(user_data)
        self._create_bottom_frame()

    def _create_top_frame(self, user_data):
        self.top_frame = tk.Frame(self._myuser_frame, width=800)
        self.top_frame.pack()

        # Id user
        user_id_data = user_data[0]
        label_user_id = ttk.Label(self.top_frame, text=f"User ID: {user_id_data}", font=("Arial", 14))
        label_user_id.pack(pady=8)

        # Username
        username_data = user_data[1]
        label_username = ttk.Label(self.top_frame, text=f"Username: {username_data}", font=("Arial", 14))
        label_username.pack(pady=8)

        # Password
        password_data = user_data[2]
        password_list = []
        # Converting the password into a string fill with *
        for word in password_data:
            password_list.append("*")
        password = " ".join([str(item) for item in password_list])

        label_password = ttk.Label(self.top_frame, text=f"Password: {password}", font=("Arial", 14))
        label_password.pack(pady=8)

        # Games played
        games_played_data = user_data[3]
        label_games_played = ttk.Label(self.top_frame, text=f"Games played: {games_played_data}", font=("Arial", 14))
        label_games_played.pack(pady=8)

        # Win games
        win_games_data = user_data[4]
        label_win_games = ttk.Label(self.top_frame, text=f"Win games: {win_games_data}", font=("Arial", 14))
        label_win_games.pack(pady=8)

        # Lost games
        lost_games_data = user_data[5]
        label_lost_games = ttk.Label(self.top_frame, text=f"Lost games: {lost_games_data}", font=("Arial", 14))
        label_lost_games.pack(pady=8)

        # Draws
        draws_data = self._get_draws(games_played_data, win_games_data, lost_games_data)
        label_draws = ttk.Label(self.top_frame, text=f"Draws: {draws_data}", font=("Arial", 14))
        label_draws.pack(pady=8)

        # Win percentage
        win_percentage_data = self._get_wins_percentage(games_played_data, win_games_data, draws_data)
        label_win_percentage = ttk.Label(self.top_frame, text=f"Win percentage: {round(win_percentage_data, 2)}%", font=("Arial", 14))
        label_win_percentage.pack(pady=8)


    def _create_bottom_frame(self):
        self.bottom_frame = tk.Frame(self._myuser_frame, width=800, height=300)
        self.bottom_frame.pack()

        # Buttons
        # Refresh
        refresh_button = tk.Button(self.bottom_frame, text="Refresh", width=15, command=self._refresh)
        refresh_button.grid(row=0, column=0, pady=15, padx=15)
        # Settings
        # settings_button = tk.Button(self.bottom_frame, text="Settings", width=15)
        # settings_button.grid(row=0, column=1, pady=15, padx=15)


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

    def _refresh(self):
        self.top_frame.destroy()
        self.bottom_frame.destroy()
        user_data = self._get_user_data()
        self._create_top_frame(user_data)
        self._create_bottom_frame()