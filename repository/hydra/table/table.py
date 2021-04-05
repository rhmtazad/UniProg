from .sqlitetable import SQLiteTable


class Table:
    def __init__(self, connection, row, column):
        self.__tbl = SQLiteTable(connection, row, column)

    def add(self, *tables):
        self.__tbl.add(*tables)

    def drop(self, *tables):
        self.__tbl.drop(*tables)

    def rename(self, old_name, new_name):
        self.__tbl.rename(old_name, new_name)

    def form(self, table, **columns):
        self.__tbl.form(table, **columns)

    def copy(self, origin_tbl, new_tbl, **columns):
        self.__tbl.copy(origin_tbl, new_tbl, **columns)

    def fetch(self, table):
        return self.__tbl.fetch(table)
