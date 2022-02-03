from User import User
from Connection import Connection

class UserDAO:
    _SELECT_ONE = "SELECT * FROM usuarios WHERE id_user=%s"
    _SELECT_ALL_ID = "SELECT * FROM usuarios ORDER BY id_user"
    _SELECT_ALL_GAMES = "SELECT * FROM usuarios ORDER BY games_played"
    _SELECT_ALL_WINS = "SELECT * FROM usuarios ORDER BY win_games"
    _SELECT_ALL_LOSSES = "SELECT * FROM usuarios ORDER BY lost_games"
    _SELECT_ALL_WIN_PERCENTAGE = "SELECT * FROM usuarios ORDER BY win_percentage"
    _UPDATE = "UPDATE usuarios SET games_played=%s, win_games=%s, lost_games=%s WHERE id_user=%s"

    @classmethod
    def select_one(cls, user):
        with Connection.get_connection() as connection:
            with connection.cursor() as cursor:
                values = (user.id_user, )
                cursor.execute(cls._SELECT_ONE, values)
                register = cursor.fetchone()
                return register

    @classmethod
    def select_all(cls, query):
        with Connection.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                registers = cursor.fetchall()
                users = []
                for register in registers:
                    user = User(register[0], register[1], register[2], register[3], register[4], register[5], register[6])
                    users.append(user)
                return users

    @classmethod
    def update(cls, user):
        with Connection.get_connection() as connection:
            with connection.cursor() as cursor:
                values = (user.games_played, user.win_games, user.lost_games,user.id_user)
                cursor.execute(cls._UPDATE, values)
                return cursor.rowcount


if __name__ == "__main__":
    # Select
    users = UserDAO.select_all("SELECT * FROM usuarios ORDER BY id_user")
    print(users)

    # Update
    # user = User(id_user=1, games_played=10, win_games=5, lost_games=5)
    # updated = UserDAO.update(user)
    # print(updated)

