from .sqliteconnection import SQLiteConnection


class Connection:
    def __init__(self, name=None, location=None):
        self.__con = SQLiteConnection(name, location)

    def execute(self, query):
        self.__con.execute(query)

    def fetch(self, query):
        return self.__con.fetch(query)
