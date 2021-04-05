from .sqlitedatabase import SQLiteDatabase


class Database:
    def __init__(self, connection, table):
        self.__db = SQLiteDatabase(connection, table)

    def drop_col(self, table, **columns):
        self.__db.drop_col(table, **columns)
