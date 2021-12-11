import psycopg2 as bd
import sys

class Connection:
    _DB = "usuarios"
    _USERNAME = "postgres"
    _HOST = "127.0.0.1"
    _PASSWORD = "admin"
    _PORT = "5432"
    _connection = None

    @classmethod
    def get_connection(cls):
        if cls._connection is None:
            try:
                cls._connection = bd.connect(database=cls._DB, user=cls._USERNAME, host=cls._HOST, password=cls._PASSWORD, port=cls._PORT)
                print("Succesful connection")
                return cls._connection
            except Exception as e:
                print(f"Error: {e}")
                sys.exit()
        else:
            return cls._connection

if __name__ == "__main__":
    Connection.get_connection()