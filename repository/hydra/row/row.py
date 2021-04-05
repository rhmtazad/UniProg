from .sqliterow import SQLiteRow


class Row:
    def __init__(self, connection):
        self.__row = SQLiteRow(connection)

    def insert(self, table, **data):
        self.__row.insert(table, **data)

    def delete(self, table, row_id):
        self.__row.delete(table, row_id)

    def update(self, table, row_id, **data):
        self.__row.update(table, row_id, **data)

    def cell(self, table, row_id, column):
        return self.__row.cell(table, row_id, column)

    def fetch(self, table, row_id):
        return self.__row.fetch(table, row_id)

    def filter(self, table, row_id, *columns):
        return self.__row.filter(table, row_id, *columns)

    def count(self, table, **col_val):
        return self.__row.count(table, **col_val)
