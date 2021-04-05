from .sqlitecolumn import SQLiteColumn


class Column:
    def __init__(self, connection):
        self.__col = SQLiteColumn(connection)

    def add(self, table, **columns):
        self.__col.add(table, **columns)

    def add_fk(self, table, column, reference_tbl, reference_col):
        self.__col.add_fk(table, column, reference_tbl, reference_col)

    def rename(self, table, current_name, new_name):
        self.__col.rename(table, current_name, new_name)

    def fetch(self, table, *columns):
        return self.__col.fetch(table, *columns)

    def fetch_names(self, table):
        return self.__col.fetch_names(table)

    def filter(self, table, **col_val):
        return self.__col.filter(table, **col_val)
