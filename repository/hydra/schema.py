from .column import Column
from .connection import Connection
from .database import Database
from .row import Row
from .table import Table


class Schema:
    def __init__(self, name=None, location=None):

        # aggregate the Connection object
        self.__con = Connection(name, location)

        # aggregate the Row object
        self.__row = Row(self.__con)

        # aggregate the Column object
        self.__col = Column(self.__con)

        # aggregate the Table object
        self.__tbl = Table(self.__con, self.__row, self.__col)

        # aggregate the database object
        self.__db = Database(self.__con, self.__tbl)

    def execute(self, query):
        self.__con.execute(query)

    def fetch(self, query):
        return self.__con.fetch(query)

    def insert_row(self, table, **data):
        self.__row.insert(table, **data)

    def delete_row(self, table, row_id):
        self.__row.delete(table, row_id)

    def update_row(self, table, row_id, **data):
        self.__row.update(table, row_id, **data)

    def fetch_cell(self, table, row_id, column):
        return self.__row.cell(table, row_id, column)

    def fetch_row(self, table, row_id):
        return self.__row.fetch(table, row_id)

    def filter_row(self, table, row_id, *columns):
        return self.__row.filter(table, row_id, *columns)

    def count_rows(self, table, **col_val):
        return self.__row.count(table, **col_val)

    def add_columns(self, table, **columns):
        self.__col.add(table, **columns)

    def add_fk_column(self, table, column, reference_tbl, reference_col):
        self.__col.add_fk(table, column, reference_tbl, reference_col)

    def rename_column(self, table, current_name, new_name):
        self.__col.rename(table, current_name, new_name)

    def fetch_column_names(self, table):
        return self.__col.fetch_names(table)

    def fetch_columns(self, table, *columns):
        return self.__col.fetch(table, *columns)

    def filter_columns(self, table, **col_val):
        return self.__col.filter(table, **col_val)

    def add_tables(self, *tables):
        self.__tbl.add(*tables)

    def drop_tables(self, *tables):
        self.__tbl.drop(*tables)

    def rename_table(self, old_name, new_name):
        self.__tbl.rename(old_name, new_name)

    def form_table(self, table, **columns):
        self.__tbl.form(table, **columns)

    def copy_table(self, origin_tbl, new_tbl, **columns):
        self.__tbl.copy(origin_tbl, new_tbl, **columns)

    def fetch_table(self, table):
        return self.__tbl.fetch(table)

    def drop_col(self, table, **columns):
        self.__db.drop_col(table, **columns)
