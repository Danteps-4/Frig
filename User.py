class User:
    def __init__(self, id_user=None, username=None, password=None, games_played=None, win_games=None, lost_games=None):
        self._id_user = id_user
        self._username = username
        self._password = password
        self._games_played = games_played
        self._win_games = win_games
        self._lost_games = lost_games

    def __str__(self):
        return f"ID user: {self._id_user}, Username: {self._username}, Password: {self._password}, Games played: {self._games_played}, Games won: {self._win_games}, Games lost: {self._lost_games}"

    @property
    def id_user(self):
        return self._id_user

    @id_user.setter
    def id_user(self, id_user):
        self._id_user = id_user

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def games_played(self):
        return self._games_played

    @games_played.setter
    def games_played(self, games_played):
        self._games_played = games_played

    @property
    def win_games(self):
        return self._win_games

    @win_games.setter
    def win_games(self, win_games):
        self._win_games = win_games

    @property
    def lost_games(self):
        return self._lost_games

    @lost_games.setter
    def lost_games(self, lost_games):
        self._lost_games = lost_games

if __name__ == "__main__":
    user = User(1, "dante", "dante123", 10, 5, 5)
    print(user)
